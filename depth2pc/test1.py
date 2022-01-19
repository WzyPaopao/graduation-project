import numpy as np

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def depth2xyz(depth_map,depth_cam_matrix,flatten=False,depth_scale=1000):
    fx,fy = depth_cam_matrix[0,0],depth_cam_matrix[1,1]
    cx,cy = depth_cam_matrix[0,2],depth_cam_matrix[1,2]
    h,w=np.mgrid[0:depth_map.shape[0],0:depth_map.shape[1]]
    z=depth_map/depth_scale
    x=(w-cx)*z/fx
    y=(h-cy)*z/fy
    xyz=np.dstack((x,y,z)) if flatten==False else np.dstack((x,y,z)).reshape(-1,3)
    #xyz=cv2.rgbd.depthTo3d(depth_map,depth_cam_matrix)
    return xyz
 
if __name__ == '__main__': 
    # 随便生成一个 分辨率为(1280, 720)的深度图, 注意深度图shape为(1280, 720)即深度图为单通道, 维度为2
    #而不是类似于shape为(1280, 720, 3)维度为3的这种
    # depth_map = np.random.randint(0,10000,(1280, 720)) 

    depth_img_path = '../depth_img/depth_screenshot_05.01.2022.png'
    depth_map = mpimg.imread(depth_img_path)

    print(depth_map.shape)
    plt.imshow(depth_map, cmap='gray')
    quit()
 
    depth_cam_matrix = np.array([[220, 0,  320],
                                 [0,   220,320],
                                 [0,   0,    1]])
    depth2xyz(depth_map, depth_cam_matrix)