#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 22:24:43 2021
Last edited on May 3, 2021

@author: anu
"""

# import os
import shutil
import random as rand
import numpy as np
import matplotlib.pyplot as plt
    
numNewFiles = 3

# Single source generation files:  
max_location = 2500 #deepest source location desired (meters)   
numSourceFile = numNewFiles


for i in range(0,numSourceFile):
    fileName = "SOURCE" + str(i)
    
    #makes a copy of the file, overwrites it if it exists
    shutil.copy('original_source.txt', fileName + ".txt") 
    
    zs = rand.random()*max_location
    
    #append the file
    f = open(fileName + ".txt", 'a') 
    f.write("zs = " + str(zs))   
    f.close()
    
    
### Generate par files AFTER materials and meshing files are created

numParFile = numNewFiles

title = 'first test'
NOISE_TOMOGRAPHY = 0

#fill in data with the main parameters that we want to modify
#randomly generate?
data = []

# print that the following parameters are specific to this simulation (add this print statement to the file)

for i in range(0,numParFile):
    fileName = "Par_file" + str(i)
    
    #makes a copy of the file, overwrites it if it exists
    shutil.copy('original_par.txt', fileName + ".txt") 
    
    #append the file
    f = open(fileName, 'a') 
    f.writelines(data)   
    f.close()
    
########### RANDOM MATERIALS #############

# geometry of the model (origin lower-left corner = 0,0) and mesh description
xmin                            = 0           # abscissa of left side of the model
xmax                            = 4000        # abscissa of right side of the model
nx                              = 80          # number of elements along X

# define the different regions of the model in the (nx,nz) spectral-element mesh
nbregions                       = 5              # then set below the different regions and model number for each region

# format of each line: nxmin nxmax nzmin nzmax material_number
# 1 80  1 20 1
# 1 59 21 40 2
# 71 80 21 40 2
# 1 80 41 60 3
# 60 70 21 40 4

numSetups = numNewFiles

for i in range(0,numSetups):
    
    fileName = "Model_Geometry" + str(i)
    f = open(fileName + ".txt","w+")

    matArr = np.zeros((nbregions-1, 5)) + 4
    imageArr = np.zeros((nx, nx)) + 4
    xChunks = np.array([0, rand.randint(1,nx-1), rand.randint(1,nx-1), nx])
    yChunks = np.array([0, rand.randint(1,nx-1), rand.randint(1,nx-1), nx])
    xChunks = np.sort(xChunks)
    yChunks = np.sort(yChunks)
    print(xChunks, yChunks)
    
    matArr[0:,] = np.array([xChunks[0], xChunks[1], yChunks[0], yChunks[1], rand.randint(1,3)])
    matArr[1:,] = np.array([xChunks[1], xChunks[3], yChunks[1], yChunks[2], rand.randint(1,3)])
    matArr[2:,] = np.array([xChunks[0], xChunks[3], yChunks[2], yChunks[3], rand.randint(1,3)])
    
    imageArr[xChunks[0]:xChunks[1], yChunks[0]:yChunks[1]] = rand.randint(1,3)
    imageArr[xChunks[1]:xChunks[3], yChunks[1]:yChunks[2]] = rand.randint(1,3)
    imageArr[xChunks[0]:xChunks[3], yChunks[2]:yChunks[3]] = rand.randint(1,3)
    
    #write the matArr to the parFile
    f.writelines(np.array2string(matArr))
    f.close()

plt.imshow(imageArr)
plt.colorbar()
    
    

