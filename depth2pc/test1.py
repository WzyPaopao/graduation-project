import numpy as np
import cv2
import open3d as o3d
from open3d import *


def show_pcl(pcl):
    # pt = o3d.geometry.PointCloud()
    # pt.points = o3d.utility.Vector3dVector(pcl)
    # o3d.visualization.draw_geometries([pt])

    rabbit = '../rabbit.pcd'
    # pcl = np.load(rabbit, allow_pickle=True)
    # print(len(data))
    #
    pcd = o3d.io.read_point_cloud(rabbit)
    print(pcd)
    # o3d.visualization.draw_geometries([pcd])
    # #
    # data = PointCloud()
    # data.points = Vector3dVector(pcl)
    # draw_geometries([data])


def depth2xyz(depth_map, depth_cam_matrix, flatten=False, depth_scale=1000):
    fx, fy = depth_cam_matrix[0, 0], depth_cam_matrix[1, 1]
    cx, cy = depth_cam_matrix[0, 2], depth_cam_matrix[1, 2]
    h, w = np.mgrid[0:depth_map.shape[0], 0:depth_map.shape[1]]
    z = depth_map / depth_scale
    x = (w - cx) * z / fx
    y = (h - cy) * z / fy
    xyz = np.dstack((x, y, z)) if flatten is False else np.dstack((x, y, z)).reshape(-1, 3)
    # xyz = cv2.rgbd.depthTo3d(depth_map, depth_cam_matrix)
    return xyz


if __name__ == '__main__': 
    # 随便生成一个 分辨率为(1280, 720)的深度图, 注意深度图shape为(1280, 720)即深度图为单通道, 维度为2
    # 而不是类似于shape为(1280, 720, 3)维度为3的这种
    depth_map = np.random.randint(0,10000,(1280, 720))

    # depth_img_path = '../depth_img/depth_screenshot_05.01.2022.png'
    # depth_img = cv2.imread(depth_img_path, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("window", depth_img)
    # cv2.waitKey(0)
    # print(depth_img.shape)
    # quit()

    depth_cam_matrix = np.array([[220, 0, 320],
                                 [0, 220, 320],
                                 [0, 0, 1]])
    pcl = depth2xyz(depth_map, depth_cam_matrix)
    print(pcl)
    show_pcl(np.array(pcl))
