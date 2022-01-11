'''
生成随机采样和最远点采样的示例图片
'''

import numpy as np
import open3d as o3d
from open3d import *


rabbit = './rabbit.pcd'
# data = np.load(rabbit)
# print(len(data))
#
# pcd = o3d.io.read_point_cloud(rabbit)
#
# o3d.visualization.draw_geometries([pcd])

data = PointCloud()
data.points = Vector3dVector(np.load(rabbit))
draw_geometries([data])