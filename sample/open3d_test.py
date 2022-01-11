import os
import numpy as np
from open3d import *
import open3d


path = '../rabbit.txt'  # (35947, 3))
points = np.loadtxt(path)

idx = np.random.randint(0, 35947, [2048])
random_points = points[idx]
np.savetxt('./rabbit_2048.txt', random_points)
point_cloud = PointCloud()
point_cloud.points = Vector3dVector(random_points)
# point_cloud.paint_uniform_color([0, 0, 0])
# point_cloud.scale(0.6)
draw_geometries([point_cloud])

# pcd_file_path = './rabbit.pcd'
# pcd = open3d.io.read_point_cloud(pcd_file_path)
# pcd.scale(0.5)
# open3d.draw_geometries([pcd])
# open3d.io.write_point_cloud("filename.pcd", pcd)
#
# mesh = open3d.io.triange_mesh(mesh_file_path)
# open3d.io.write_triange_mesh("filename.ply", mesh)
