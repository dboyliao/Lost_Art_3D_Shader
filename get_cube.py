#!/usr/bin/env python
#-*- coding: utf-8 -*-
from __future__ import print_function, absolute_import
from utils import setPixel, saveImage
from threeD_objects import Vertex, Triangle

def make_cube(radius = 10, color = (255, 0, 0, 1)):
    triangles = []

    # 1st
    triangles.append(Triangle([Vertex((-radius, -radius, radius), color, (0, 0, 1)),
                               Vertex((-radius, radius, radius), color, (0, 0, 1)),
                               Vertex((radius, -radius, radius), color, (0, 0, 1))]))
    # 2nd
    triangles.append(Triangle([Vertex((-radius, radius, radius), color, (0, 0, 1)),
                               Vertex((radius, -radius, radius), color, (0, 0, 1)),
                               Vertex((radius, radius, radius), color, (0, 0, 1))]))

    # 3rd
    triangles.append(Triangle([Vertex((-radius, -radius, -radius), color, (0, 0, -1)),
                               Vertex((radius, -radius, -radius), color, (0, 0, -1)),
                               Vertex((radius, radius, -radius), color, (0, 0, -1))]))

    # 4th
    triangles.append(Triangle([Vertex((-radius, -radius, -radius), color, (0, 0, -1)),
                               Vertex((radius, radius, -radius), color, (0, 0, -1)),
                               Vertex((-radius, radius, -radius), color, (0, 0, -1))]))

    # 5th
    triangles.append(Triangle([Vertex((-radius, radius, -radius), color, (0, 1, 0)),
                               Vertex((-radius, radius, radius), color, (0, 1, 0)),
                               Vertex((radius, radius, -radius), color, (0, 1, 0))]))

    # 6th
    triangles.append(Triangle([Vertex((-radius, radius, radius), color, (0, 1, 0)),
                               Vertex((radius, radius, -radius), color, (0, 1, 0)),
                               Vertex((radius, radius, radius), color, (0, 1, 0))]))

    # 7th
    triangles.append(Triangle([Vertex((-radius, -radius, -radius), color, (0, -1, 0)),
                               Vertex((radius, -radius, -radius), color, (0, -1, 0)),
                               Vertex((-radius, -radius, radius), color, (0, -1, 0))]))

    # 8th
    triangles.append(Triangle([Vertex((-radius, -radius, radius), color, (0, -1, 0)),
                               Vertex((radius, -radius, radius), color, (0, -1, 0)),
                               Vertex((radius, -radius, -radius), color, (0, -1, 0))]))

    # 9th
    triangles.append(Triangle([Vertex((radius, -radius, -radius), color, (1, 0, 0)),
                               Vertex((radius, -radius, radius), color, (1, 0, 0)),
                               Vertex((radius, radius, -radius), color, (1, 0, 0))]))

    # 10th
    triangles.append(Triangle([Vertex((radius, -radius, radius), color, (1, 0, 0)),
                               Vertex((radius, radius, -radius), color, (1, 0, 0)),
                               Vertex((radius, radius, radius), color, (1, 0, 0))]))

    # 11th
    triangles.append(Triangle([Vertex((-radius, -radius, -radius), color, (-1, 0, 0)),
                               Vertex((-radius, radius, -radius), color, (-1, 0, 0)),
                               Vertex((-radius, -radius, radius), color, (-1, 0, 0))]))

    # 12th
    triangles.append(Triangle([Vertex((-radius, -radius, radius), color, (-1, 0, 0)),
                               Vertex((-radius, radius, radius), color, (-1, 0, 0)),
                               Vertex((-radius, radius, -radius), color, (-1, 0, 0))]))

    return triangles

# make an oridinary simple cube
cube = make_cube()

# setup cube to meet the Swift implementation
## 3th
triangle = cube[2]
triangle.vertices[0].color = (0, 0, 255, 1) # blue
triangle.vertices[1].color = (0, 255, 0, 1) # green

## 4th
triangle = cube[3]
triangle.vertices[0].color = (0, 255, 255, 1)
triangle.vertices[1].color = (255, 255, 0, 1)
triangle.vertices[2].color = (255, 0, 255, 1)

## 5th
triangle = cube[4]
triangle.vertices[0].color = (0, 0, 255, 1)
triangle.vertices[1].color = (0, 0, 255, 1)
triangle.vertices[2].color = (0, 0, 255, 1)

## 6th
triangle = cube[5]
triangle.vertices[0].color = (0, 0, 255, 1)
triangle.vertices[1].color = (0, 0, 255, 1)
triangle.vertices[2].color = (0, 0, 255, 1)

## 7th
triangle = cube[6]
triangle.vertices[0].color = (255, 255, 255, 1)
triangle.vertices[1].color = (255, 255, 255, 1)
triangle.vertices[2].color = (255, 255, 255, 1)

## 8th
triangle = cube[7]
triangle.vertices[0].color = (255, 255, 255, 1)
triangle.vertices[1].color = (255, 255, 255, 1)
triangle.vertices[2].color = (255, 255, 255, 1)

## 9th
triangle = cube[8]
triangle.vertices[0].color = (0, 255, 0, 1)
triangle.vertices[1].color = (0, 255, 0, 1)
triangle.vertices[2].color = (0, 255, 0, 1)

## 10th
triangle = cube[9]
triangle.vertices[0].color = (0, 255, 0, 1)
triangle.vertices[1].color = (0, 255, 0, 1)
triangle.vertices[2].color = (0, 255, 0, 1)

## 11th
triangle = cube[10]
vertex = triangle.vertices[0]
vertex.nx, vertex.ny, vertex.nz = -0.577, -0.577, -0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[1]
vertex.nx, vertex.ny, vertex.nz = -0.577, 0.577, -0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[2]
vertex.nx, vertex.ny, vertex.nz = -0.577, -0.577, 0.577
vertex.color = (0, 255, 255, 1)

## 12th
triangle = cube[11]
vertex = triangle.vertices[0]
vertex.nx, vertex.ny, vertex.nz = -0.577, -0.577, 0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[1]
vertex.nx, vertex.ny, vertex.nz = -0.577, 0.577, 0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[2]
vertex.color = (0, 255, 255, 1)
vertex.nx, vertex.ny, vertex.nz = -0.577, 0.577, -0.577
