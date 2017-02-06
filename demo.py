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

cube = make_cube()
triangle = cube[-2]
vertex = triangle.vertices[0]
vertex.nx, vertex.ny, vertex.nz = -0.577, -0.577, 0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[1]
vertex.nx, vertex.ny, vertex.nz = -0.577, 0.577, -0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[2]
vertex.nx, vertex.ny, vertex.nz = -0.577, -0.577, 0.577
vertex.color = (0, 255, 255, 1)

triangle = cube[-1]
vertex = triangle.vertices[0]
vertex.nx, vertex.ny, vertex.nz = -0.577, -0.577, 0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[1]
vertex.nx, vertex.ny, vertex.nz = -0.577, 0.577, 0.577
vertex.color = (0, 255, 255, 1)
vertex = triangle.vertices[2]
vertex.color = (0, 255, 255, 1)
vertex.nx, vertex.ny, vertex.nz = -0.577, 0.577, -0.577


