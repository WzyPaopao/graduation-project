import open3d as o3d
import numpy as np
# from open3d.open3d.geometry import PointCloud
# from open3d.open3d.utility import Vector3dVector
# from open3d.open3d.visualization import draw_geometries


def main():
    # origin_data = o3d.io.read_point_cloud('../rabbit_2048.txt', format='xyz')
    # o3d.visualization.draw_geometries([origin_data])
    point_number = 512
    origin_data = np.loadtxt('../rabbit_2048.txt')
    origin_pc = o3d.geometry.PointCloud()
    origin_pc.points = o3d.utility.Vector3dVector(origin_data)
    origin_pc.colors = o3d.utility.Vector3dVector(np.zeros_like(origin_data))

    random_data = np.loadtxt('../random_sample_rabbit_{}.txt'.format(point_number))
    random_pc = o3d.geometry.PointCloud()
    random_pc.points = o3d.utility.Vector3dVector(random_data)
    color = o3d.utility.Vector3dVector(np.zeros_like(random_data)) # black color
    # color = o3d.utility.Vector3dVector(np.ones_like(random_data) * [1, 0, 0])  # red color
    random_pc.colors = color

    farthest_data = np.loadtxt('../farthest_sample_rabbit_{}.txt'.format(point_number))
    farthest_pc = o3d.geometry.PointCloud()
    farthest_pc.points = o3d.utility.Vector3dVector(farthest_data)
    farthest_pc.colors = color
    

    o3d.visualization.draw_geometries([origin_pc], width=1000,height=800)
    o3d.visualization.draw_geometries([random_pc], width=1000,height=800)
    o3d.visualization.draw_geometries([farthest_pc], width=1000,height=800)


if __name__ == "__main__":
    main()