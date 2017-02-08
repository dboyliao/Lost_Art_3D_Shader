#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from math import cos, sin
from get_cube import cube # the cube to display
from utils import setPixel, saveImage
from threeD_objects import Triangle

# the model
## position (relative to world origin)
modelX, modelY, modelZ = 0.0, 0.0, 0.0

## scales
modelScaleX, modelScaleY, modelScaleZ = 1.0, 1.0, 1.0

## pitch, yaw, roll
## https://www.grc.nasa.gov/www/k-12/airplane/Images/rotations.gif
modelRotateX, modelRotateY, modelRotateZ = 0.0, 0.0, 0.0

## model origin (relative to local origin, the center of the cube)
## it is the origin which all transformations apply (such as rotation, translation, scaling..etc)
modelOriginX, modelOriginY, modelOriginZ = 10.0, 0.0, 10.0

# the camera
## position
cameraX, cameraY, cameraZ = 0.0, 20.0, -20.0

# the light
## ambient light: we multiply the vertex colors with ambient light.
##                In this case, we will display the vertex color multiplied by (0.2, 0.2, 0.2)
ambientB = 1.0
ambientG = 1.0
ambientR = 1.0
ambientIntensity = 0.2

## diffuse light: a directed light source
diffuseB = 1.0
diffuseG = 1.0
diffuseR = 1.0
diffuseIntensity = 0.8

## direction of diffuse light
diffuseX = 0.0
diffuseY = 0.0
diffuseZ = 1.0

def render(canvas):
    pass

def clearCanvas(canvas, color = None):
    """
    Equivalent implementation of clearRenderBuffer.
    """
    if color is None:
        canvas[:, :, 0:3] = 255
    else:
        canvas[:, :] = color

def transformAndProject(obj_data):

    transformed_data = [t.copy() for t in obj_data]

    for i, triangle in enumerate(transformed_data):
        new_triangle = Triangle()

        for j, vertex in enumerate(triangle.vertices):
            new_vertex = vertex.copy()

            new_vertex.x -= modelOriginX
            new_vertex.y -= modelOriginY
            new_vertex.z -= modelOriginZ

            new_vertex.x *= modelScaleX
            new_vertex.y *= modelScaleY
            new_vertex.z *= modelScaleZ

            rot_y = cos(modelRotateX)*new_vertex.y + sin(modelRotateX)*new_vertex.z
            rot_z = -sin(modelRotateX)*new_vertex.y + cos(modelRotateX)*new_vertex.z
            new_vertex.y, new_vertex.z = rot_y, rot_z

            rot_x = cos(modelRotateY)*new_vertex.x + sin(modelRoateY)*new_vertex.z
            rot_z = -sin(modelRoateY)*new_vertex.x + cos(modelRoateY)*new_vertex.z
            new_vertex.x, new_vertex.z = rot_x, rot_z

            rot_x = cos(modelRotateZ)*new_vertex.x + sin(modelRotateZ)*new_vertex.y
            rot_y = -sin(modelRoateZ)*new_vertex.x + cos(modelRotateZ)*new_vertex.y
            new_vertex.x, new_vertex.y = rot_x, rot_y

            new_vertex.x += modelX
            new_vertex.y += modelY
            new_vertex.z += modelZ

            rot_y = cos(modelRotateX)*new_vertex.ny + sin(modelRotateX)*new_vertex.nz
            rot_z = -sin(modelRotateX)*new_vertex.ny + cos(modelRotateX)*new_vertex.nz
            new_vertex.ny, new_vertex.nz = rot_y, rot_z

            rot_x = cos(modelRotateY)*new_vertex.nx + sin(modelRoateY)*new_vertex.nz
            rot_z = -sin(modelRoateY)*new_vertex.nx + cos(modelRoateY)*new_vertex.nz
            new_vertex.nx, new_vertex.nz = rot_x, rot_z

            rot_x = cos(modelRotateZ)*new_vertex.nx + sin(modelRotateZ)*new_vertex.ny
            rot_y = -sin(modelRoateZ)*new_vertex.nx + cos(modelRotateZ)*new_vertex.ny
            new_vertex.nx, new_vertex.ny = rot_x, rot_y

            new_triangle.vertices[j] = new_vertex

        transformed_data[i] = new_triangle
