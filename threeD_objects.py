#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Vertex(object):

    def __init__(self, position, color, normal):
        self.x, self.y, self.z = position
        self.nx, self.ny, self.nz = normal
        self.color = color

    def __repr__(self):

        return "loc: ({0.x}, {0.y}, {0.z}), color: {0.color}, normal: ({0.nx}, {0.ny}, {0.nz})".format(self)

class Triangle(object):

    def __init__(self, vertices):
        assert len(vertices) == 3, "number of vertices should be 3"
        assert all(map(lambda x: isinstance(x, Vertex), vertices)), "all elements should be of type Vertex"

        self.vertices = vertices

    def __repr__(self):

        return "v0: {vertices[0]}, v1: {vertices[1]}, v2: {vertices[2]}".format(vertices = self.vertices)
