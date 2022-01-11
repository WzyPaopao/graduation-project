'''
生成随机采样和最远点采样的示例图片
'''

# import numpy as np
# import open3d as o3d
# from open3d import *


# rabbit = './rabbit.pcd'
# # data = np.load(rabbit)
# # print(len(data))
# #
# # pcd = o3d.io.read_point_cloud(rabbit)
# #
# # o3d.visualization.draw_geometries([pcd])

# data = PointCloud()
# data.points = Vector3dVector(np.load(rabbit))
# draw_geometries([data])

# --------------------------------------------------------------------

from open3d import *
import numpy as np
import os


path = '../rabbit_2048.txt'  # (2048, 3))
points = np.loadtxt(path)
idx = np.random.randint(0, 2048, [128])
random_points = points[idx]

point_cloud = PointCloud()
point_cloud.points = Vector3dVector(random_points)
point_cloud.paint_uniform_color([0, 0, 0])
point_cloud.scale(0.6)
draw_geometries([point_cloud])
