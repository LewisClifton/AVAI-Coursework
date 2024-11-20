import numpy as np
from utils.common import *
import cv2

def add_gaussian_noise(image, std=1):
    image = np.clip(image + np.random.normal(scale=std, size=image.shape), 0, 255).astype(np.uint8)
    return image

def add_salt_pepper_noise(image, s=0.01, p=0.01):
    
    salt = np.random.rand(image.shape[0], image.shape[1], image.shape[2]) < s
    pepper = np.random.rand(image.shape[0], image.shape[1], image.shape[2]) < p
    image[salt] = 255
    image[pepper] = 0
    return image

def downsample(image, factor=2, interpolation=cv2.INTER_CUBIC):
    new_size = (image.shape[1] // factor, image.shape[0] // factor)
    return cv2.resize(image, new_size, interpolation=interpolation)