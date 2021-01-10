#!/usr/bin/env python

# Authors: Juan G Victores
# CopyPolicy: released under the terms of the LGPLv2.1
# URL: https://github.com/roboticslab-uc3m/webots-tools

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

outFile = open('map.wbt', 'w')
outFile.write(myStr)
outFile.close()
