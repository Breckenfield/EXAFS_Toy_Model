# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6 13:18 2015

@author: Connor Breckenfield
First step to build EXAFS scattering model
Capable of calculating for multiple R values, Disorder over multiple scattering paths
using the Einstine model for temperature.
"""
import functions

print("#-------------------------#")
print("#-----EXAFS Toy Model-----#")
print("#-------------------------#")

materialInfo = functions.LoadMaterialInfo("Material.json")
materialName = input("Pick a Material to simulate: ")
try:
    print(materialInfo[materialName])
except KeyError:
    print("Material Not Found")
    exit()

radius = materialInfo[materialName]["RadiusDistance"]
num = materialInfo[materialName]["NumberOfAtoms"]
temp = materialInfo[materialName]["Temperature"]
atomicMass = materialInfo[materialName]["AtomicMass"]
einsteinTemp = materialInfo[materialName]["EinsteinTemperature"]

#Checks Json input
print("Checking Material Details")
materialCheck = functions.CheckMaterialInput(radius, num, atomicMass, einsteinTemp)
    
if materialCheck == False:
    print("The material check has failed")
    exit()
else:
    print("The material check has passed")

# Number of samplepoints
samplePoints = 10000
# Sample spacing
sampleSpacing = 0.1
# Computation of K value range
K = functions.K_RangeCal(sampleSpacing, samplePoints)
# X-axis for fourier transform
Rf = functions.RfCal(samplePoints)
# Simplified EXAFS equation with K^2 weighting for all R values
Xk = []
for i in range(len(radius)):
    sig = functions.SigmaCal(temp, einsteinTemp[i], atomicMass[i])
    X = functions.EXAFSCal(num, i, K, radius, sig)
    Xk.append(X)

Xkf_act = functions.FourierTransformCal(samplePoints, Xk, radius)
#graph plot
functions.PlotResults(Rf,Xkf_act)
