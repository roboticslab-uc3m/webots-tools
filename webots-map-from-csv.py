#!/usr/bin/env python

# Authors: Juan G Victores
# CopyPolicy: released under the terms of the LGPLv2.1
# URL: https://github.com/roboticslab-uc3m/webots-tools

# Alternatively, could use the Supervisor API:
# - https://github.com/cyberbotics/webots/blob/master/tests/api/controllers/supervisor_save_world/supervisor_save_world.c

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
nZ = inFile.shape[1]
print("lines = X =",inFile.shape[0])
print("columns = Z =",inFile.shape[1])

Ey = boxHeight

Ex = meterPerPixel
Ez = meterPerPixel

myStr = '#VRML_SIM R2021a utf8\n\
WorldInfo {\n\
  coordinateSystem "NUE"\n\
}\n\
Viewpoint {\n\
  orientation -0.7 0.7 0.2 0.75\n\
  position 13.0 10.0 18.0\n\
}\n\
TexturedBackground {\n\
}\n\
TexturedBackgroundLight {\n\
}\n'

#-- Create Floor

floorEx = meterPerPixel * nX # x is x
floorEy = meterPerPixel * nZ # y is y but placed on world z (world y up)

floorStr = 'Floor {\n\
  translation $floorX 0 $floorZ\n\
  size $floorEx $floorEy\n\
}\n'

floorStr = floorStr.replace('$floorX',str(floorEx/2.0))
floorStr = floorStr.replace('$floorZ',str(floorEy/2.0))
floorStr = floorStr.replace('$floorEx',str(floorEx))
floorStr = floorStr.replace('$floorEy',str(floorEy))
myStr += floorStr

#-- Create Walls

boxStr = 'SolidBox {\n\
  name "$name"\n\
  translation $x $y $z\n\
  size $Ex $Ey $Ez\n\
}\n'

for iX in range(nX):
    #print("iX:",iX)
    for iZ in range(nZ):
        #print("* iY:",iY)

        #-- Skip box if map indicates a 0
        if inFile[iX][iZ] == 0:
            continue

        #-- Add E___/2.0 to each to force begin at 0,0,0 (centered by default)
        x = Ex/2.0 + iX*meterPerPixel
        z = Ez/2.0 + iZ*meterPerPixel
        y = Ey/2.0  # Add this to raise to floor level (centered by default)

        #-- Create box
        name = 'box_'+str(iX)+'_'+str(iZ)
        tmpBoxStr = boxStr.replace('$name',name)
        tmpBoxStr = tmpBoxStr.replace('$x',str(x))
        tmpBoxStr = tmpBoxStr.replace('$y',str(y))
        tmpBoxStr = tmpBoxStr.replace('$z',str(z))
        tmpBoxStr = tmpBoxStr.replace('$Ex',str(Ex))
        tmpBoxStr = tmpBoxStr.replace('$Ey',str(Ey))
        tmpBoxStr = tmpBoxStr.replace('$Ez',str(Ez))
        myStr += tmpBoxStr

outFile = open('map.wbt', 'w')
outFile.write(myStr)
outFile.close()
