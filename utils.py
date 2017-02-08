#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import print_function
from copy import deepcopy
import cv2

def setPixel(img, x, y, color, verbose = False):
    if verbose:
        print("set {} to ({}, {})".format(color, x, y))
    img[x, y] = color

def saveImage(name, img):
    return cv2.imwrite(name, img)

