import cv2
import os

def save_result(image, path):
    cv2.imwrite(path, image)
    return path
