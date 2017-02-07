#!/usr/bin/env python
# -*- coding: utf-8 -*-
from get_cube import cube # the cube to display

# the model
## position (relative to world origin)
modelX, modelY, modelZ = 0.0, 0.0, 0.0

## scales
modelScaleX, modelScaleY, modelScaleZ = 1.0, 1.0, 1.0

## pitch, yaw, roll
## https://www.grc.nasa.gov/www/k-12/airplane/Images/rotations.gif
modelRotateX, modelRotateY, modelRotateZ = 0.0, 0.0, 0.0

## model origin (relative to local origin, the center of the cube)
modelOriginX, modelOriginY, modelOriginZ = 10.0, 0.0, 10.0

# the camera
## position
cameraX, cameraY, cameraZ = 0.0, 20.0, -20.0

# the light
