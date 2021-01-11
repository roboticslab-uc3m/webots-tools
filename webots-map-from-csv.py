#!/usr/bin/env python

# Authors: Juan G Victores
# CopyPolicy: released under the terms of the LGPLv2.1
# URL: https://github.com/roboticslab-uc3m/webots-tools

#-- User variables
boxHeight = 1.0
inFileStr = 'assets/map1.csv'

resolution = 1.0  # Just to make similar to MATLAB [pixel/meter]
meterPerPixel = 1 / resolution  # [meter/pixel]

#-- Program
from numpy import genfromtxt
inFile = genfromtxt(inFileStr, delimiter=',')
print(inFile)

nX = inFile.shape[0]
nY = inFile.shape[1]
print("lines = X =",inFile.shape[0])
print("columns = Y =",inFile.shape[1])

myStr = '#VRML_SIM R2021a utf8\n\
WorldInfo {\n\
  coordinateSystem "NUE"\n\
}\n\
Viewpoint {\n\
  orientation -0.7 0.7 0.2 0.75\n\
  position 1.2 1.6 2.3\n\
}\n\
TexturedBackground {\n\
}\n\
TexturedBackgroundLight {\n\
}\n'

#Floor {
#  size 2 3
#}

#SolidBox {
#  translation 0 0.05 0
#  size 0.1 0.1 0.1
#}

outFile = open('map.wbt', 'w')
outFile.write(myStr)
outFile.close()
