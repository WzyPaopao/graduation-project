from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import vtk
from PyQt5 import QtCore, QtGui, QtWidgets
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from testvtkgui import Ui_MainWindow
# import pcl.pcl_visualization
import open3d as o3d
import numpy as np


class Mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Mywindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('test_gui')

        self.frame = QtWidgets.QFrame()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.formLayout.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        # Create source
        # fileName = "D:\\rabbit.pcd";  # 注意更换自己的pcd点云文件
        # cloud = pcl.load_XYZRGB(fileName)
        fileName = './rabbit.pcd'
        pcd = o3d.io.read_point_cloud(fileName)
        # cloud = pcl.load_XYZRGB(fileName)
        cloud = np.asarray(pcd.points)

        poins = vtk.vtkPoints()
        for i in range(cloud.shape[0]):
            dp = cloud[i]
            poins.InsertNextPoint(dp[0], dp[1], dp[2])

        polydata = vtk.vtkPolyData()
        polydata.SetPoints(poins)

        glyphFilter = vtk.vtkVertexGlyphFilter()
        glyphFilter.SetInputData(polydata)
        glyphFilter.Update()

        dataMapper = vtk.vtkPolyDataMapper()
        dataMapper.SetInputConnection(glyphFilter.GetOutputPort())

        # Create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(dataMapper)

        actor1 = vtk.vtkActor()
        actor1.SetMapper(dataMapper)

        self.ren.AddActor(actor)
        self.ren.AddActor(actor1)

        self.ren.ResetCamera()

        # self.frame.setLayout(self.formLayout)
        # self.setCentralWidget(self.frame)

        self.show()
        self.iren.Initialize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())



