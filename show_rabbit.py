'''
生成随机采样和最远点采样的示例图片
'''

# import numpy as np
# import open3d as o3d
# from open3d import *


rabbit = './rabbit.pcd'
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


index = 16
pointcloud = np.load(rabbit)
# pointcloud = pointcloud[index]
# print(pointcloud.shape)


# mask_zero = np.zeros(shape=(1024, ))
# mask_index = np.random.randint(low=0, high=1023, size=(200))
# # mask_zero[mask_index] = 1
# mask_zero[100:900:4] = 1
# mask = np.expand_dims(mask_zero, axis=-1)
# print(mask.sum())

# pointcloud = pointcloud * mask

point_cloud = PointCloud()
point_cloud.points = Vector3dVector(pointcloud)
point_cloud.paint_uniform_color([0, 0, 0])

draw_geometries([point_cloud])
