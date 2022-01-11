import os
import numpy as np
from open3d import *


points = np.random.rand(10000, 3)
point_cloud = PointCloud()
point_cloud.points = Vector3dVector(points)
point_cloud.paint_uniform_color([0, 0, 0])
draw_geometries([point_cloud])