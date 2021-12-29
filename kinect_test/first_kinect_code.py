from pykinect2 import PyKinectV2, PyKinectRuntime
import cv2
import numpy as np


kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)


def get_last_depth():
    frame = kinect.get_last_depth_frame()
    frame = frame.astype(np.uint8)
    dep_frame = np.reshape(frame, [424, 512])
    return cv2.cvtColor(dep_frame, cv2.COLOR_GRAY2RGB)


while True:
    last_frame = get_last_depth()
    cv2.imshow('test', last_frame)
    cv2.waitKey(1)
