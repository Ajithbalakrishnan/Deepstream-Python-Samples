#!/usr/bin/env python3
#
#  USB Camera - Simple
#
#  Copyright (C) 2021-22 JetsonHacks (info@jetsonhacks.com)
#
#  MIT License
#

import sys

import cv2 as cv2

window_title = "USB Camera"
import time

def show_camera():
    # ASSIGN CAMERA ADDRESS HERE
    camera_id = "/dev/video0"
    # Full list of Video Capture APIs (video backends): https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
    # For webcams, we use V4L2 cv.CAP_OPENCV_MJPEG  CAP_GSTREAMER

    #VideoCapture cap("v4l2src device=/dev/video1 ! video/x-raw,width=1920,height=1080,format=UYVY,framerate=30/1 ! videoconvert ! video/x-raw,format=BGR ! appsink");

    #video_capture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2) 
    video_capture =cv2.VideoCapture('v4l2src device=/dev/video0 ! image/jpeg, width=640, height=480, framerate=30/1, format=MJPG ! nvv4l2decoder mjpeg=true ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink', cv2.CAP_GSTREAMER)
    # video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # video_capture.set(cv2.CAP_PROP_FPS, 30)
   # video_capture.SetCaptureProperty(capture,cv.CV_CAP_PROP_FOURCC, cv.CV_FOURCC('M', 'J', 'P', 'G'))
    """ 
    # How to set video capture properties using V4L2:
    # Full list of Video Capture Properties for OpenCV: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html
    #Select Pixel Format:
    # video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'YUYV'))
    # Two common formats, MJPG and H264
    # video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    # Default libopencv on the Jetson is not linked against libx264, so H.264 is not available
    # video_capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'H264'))
    # Select frame size, FPS:
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    video_capture.set(cv2.CAP_PROP_FPS, 30)
    """
    if video_capture.isOpened():
        try:
            # window_handle = cv2.namedWindow(
            #     window_title, cv2.WINDOW_AUTOSIZE )
            # Window
            t1 =time.time()
            while True:
                
                ret_val, frame = video_capture.read()
                # Check to see if the user closed the window
                # Under GTK+ (Jetson Default), WND_PROP_VISIBLE does not work correctly. Under Qt it does
                # GTK - Substitute WND_PROP_AUTOSIZE to detect if window has been closed by user
                # if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                #     cv2.imshow(window_title, frame)
                # else:
                #     break
                # keyCode = cv2.waitKey(10) & 0xFF
                # # Stop the program on the ESC key or 'q'
                # if keyCode == 27 or keyCode == ord('q'):
                #     break

                t2 =time.time()
                print("FPS : ",(1/(t2 - t1)))
                t1 = t2


        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":

    show_camera()
