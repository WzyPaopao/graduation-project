"""
展示原始点云,随机下采样点云,最远点采样点云
"""

import numpy as np
from open3d import *
import open3d as o3d


def main():
    point_number = 256
    data = np.loadtxt('../rabbit_2048.txt')
    # draw_from_data(data, color=False)

    random_idx = np.random.randint(0, 2048, (point_number,))
    random_sample_data = data[random_idx]
    # draw_from_data(random_sample_data, color=False)

    _, farthest_sample_data = farthest_point_sample(data, point_number)
    # draw_from_data(farthest_sample_data, color=False)

    save_ply('./rabbit_2048.ply', data)
    save_ply('./random_rabbit_256.ply', random_sample_data)
    save_ply('./farthest_rabbit_256.ply', farthest_sample_data)


def save_ply(path, data):
    point_cloud = PointCloud()
    point_cloud.points = Vector3dVector(data)
    o3d.io.write_point_cloud(path, point_cloud)


def draw_from_data(points, color=True):
    point_cloud = PointCloud()
    point_cloud.points = Vector3dVector(points)
    if color:
        point_cloud.paint_uniform_color([0, 0, 0])
    draw_geometries([point_cloud])


def draw_from_file(path, color=True):
    points = np.loadtxt(path)
    draw_from_data(points, color)


def farthest_point_sample(xyz, npoint):
    """
    Input:
        xyz: pointcloud data, [B, N, 3]
        npoint: number of samples
    Return:
        centroids: sampled pointcloud index, [B, npoint]
    """
    N, C = xyz.shape

    # 初始化一个centroids矩阵，用于存储npoint个采样点的索引位置，大小为npoint
    # 其中B为BatchSize的个数
    centroids = np.zeros(npoint, dtype=np.long)

    # distance矩阵(N)记录所有点到某一个点的距离，初始化的值很大，后面会迭代更新
    distance = np.ones(N) * 1e10

    # farthest表示当前最远的点，也是随机初始化，范围为0~N，初始化B个；每个batch都随机有一个初始最远点
    farthest = np.random.randint(0, N, (1,), dtype=np.long)
    farthest = farthest[0]

    # 直到采样点达到npoint，否则进行如下迭代：
    for i in range(npoint):
        # 设当前的采样点centroids为当前的最远点farthest
        centroids[i] = farthest

        # 取出该中心点centroid的坐标
        centroid = xyz[farthest]

        # 求出所有点到该centroid点的欧式距离，存在dist矩阵中
        dist = np.sum((xyz - centroid) ** 2, -1)

        # 建立一个mask，如果dist中的元素小于distance矩阵中保存的距离值，则更新distance中的对应值
        # 随着迭代的继续，distance矩阵中的值会慢慢变小，
        # 其相当于记录着某个Batch中每个点距离所有已出现的采样点的最小距离
        mask = dist < distance  # 确保拿到的是距离所有已选中心点最大的距离。比如已经是中心的点，其dist始终保持为	 #0，二在它附近的点，也始终保持与这个中心点的距离
        distance[mask] = dist[mask]

        # 从distance矩阵取出最远的点为farthest，继续下一轮迭代
        farthest = np.argmax(distance)
    return centroids, xyz[centroids]


if __name__ == '__main__':
    main()