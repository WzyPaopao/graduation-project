import cv2
import numpy as np
import os
import glob


def scan_all_pic():
    path = "./pic"
    files = os.listdir(path)
    for file in files:
        image = cv2.imread(path + "/" + file)
        res = cv2.findChessboardCorners(image, (9, 6))
        cv2.cornerSubPix(image, res)
        print(file + '\n------------------------------------------------')
        print(res)


def scan_one_pic():
    # 读取图片
    image = cv2.imread("./pic/IMG_2633.JPG")

    # 寻找角点
    ret, corners = cv2.findChessboardCorners(image, (9, 6), None)

    # 精细化角点坐标
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    cv2.cornerSubPix(image, corners, (5, 5), (-1, -1), criteria)

    # 创建可变尺寸窗口，并显示图片
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return None


def standard(path, corner_shape):
    """
    使用原版的寻找角点函数，显式进行精细化，速度快
    :return:
    """
    # 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
    criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)
    h, w = corner_shape
    # 获取标定板角点的位置
    objp = np.zeros((h * w, 3), np.float32)
    objp[:, :2] = np.mgrid[0:w, 0:h].T.reshape(-1, 2)  # 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y
    obj_points = []  # 存储3D点
    img_points = []  # 存储2D点
    images = glob.glob(path)
    for fname in images:
        img = cv2.imread(fname)
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.imshow('img', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        size = gray.shape[::-1]
        ret, corners = cv2.findChessboardCorners(gray, (h, w))
        # print(ret)
        # print(corners.shape)
        if ret:
            obj_points.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)  # 在原角点的基础上寻找亚像素角点
            # print(corners2)
            if [corners2]:
                img_points.append(corners2)
            else:
                img_points.append(corners)

            cv2.drawChessboardCorners(img, (w, h), corners, ret)  # 记住，OpenCV的绘制函数一般无返回值
            cv2.imshow('img', img)
            # cv2.waitKey(0)

    print(len(img_points))
    cv2.destroyAllWindows()
    # 标定
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, size, None, None)
    # print("ret:", ret)
    # print("mtx:\n", mtx)  # 内参数矩阵
    # print("dist:\n", dist)  # 畸变系数  distortion cofficients = (k_1,k_2,p_1,p_2,k_3)
    # print("rvecs:\n", rvecs)  # 旋转向量 # 外参数
    # print("tvecs:\n", tvecs)  # 平移向量 # 外参数
    # print("-----------------------------------------------------")
    return ret, mtx, dist, rvecs, tvecs


def find_corner_v2():
    """
    直接使用SB升级版函数，没有显式进行角点精细化，速度较慢
    :return:
    """
    images = glob.glob("./pic/*.JPG")
    patter_size = (6, 9)
    for fname in images:
        img = cv2.imread(fname)
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)
        cv2.imshow('img', img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, corner = cv2.findChessboardCornersSB(gray, patter_size)
        if ret:
            cv2.drawChessboardCorners(img, patter_size, corner, ret)
            cv2.imshow('img', img)
            cv2.waitKey(10)


def correct_image(pic_path, out_path, mtx, dist):
    print(pic_path)
    img = cv2.imread(pic_path)
    h, w = img.shape[:2]
    new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 0, (w, h))

    # 校正
    dst = cv2.undistort(img, mtx, dist, None, new_camera_mtx)  # 裁切图像
    x, y, w, h = roi
    dst = dst[y:y + h, x:x + w]
    cv2.imwrite(out_path, dst)


def main():
    path = "./even/右1/*.jpg"
    sret, mtx, dist, rvecs, tvec = standard(path, (8, 11))
    images = glob.glob(path)
    for image in images:
        print(image)
        paths = image.split('/')
        prefix = paths[:-1]
        image_names = paths[-1].split('_')
        image_name = image_names[0] + '_fix_' + image_names[1]
        correct_image(image, "./test_pic/右1/{}".format(image_name), mtx, dist)
    # correct_image(, mtx, dist)
    # find_corner_v2()


if __name__ == '__main__':
    main()
