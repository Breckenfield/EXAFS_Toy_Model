# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6 13:18 2015
Updated on Thur Feb 6 10:56 2020

@author: Connor Breckenfield
First step to build EXAFS scattering model
Capable of calculating for multiple R values, Disorder over multiple scattering paths
using the Einstine model for temperature.
"""
import numpy
import json
import Functions

print("#-------------------------#")
print("#-----EXAFS Toy Model-----#")
print("#-------------------------#")

materialName = input("Pick a Material to simulate: ")

with open("Material.json", "r") as json_file:
    materialInfo = json.load(json_file)
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
Functions.CheckMaterialInput(radius, num, atomicMass, einsteinTemp)

# Number of samplepoints
samplePoints = 10000
# Sample spacing
sampleSpacing = 1.0/10

# Computation of K value range
K = numpy.linspace(sampleSpacing, samplePoints*sampleSpacing, samplePoints)

# X-axis for fourier transform
Rf = Functions.RfCal(samplePoints)

# Simplified EXAFS equation with K^2 weighting for all R values
Xk = []
for i in range(len(radius)):
    u = Functions.ConvertAtomicMass(atomicMass[i])
    sig = Functions.SigmaCal(temp, einsteinTemp[i], u)
    X = Functions.EXAFSCal(num, i, K, radius, sig)
    Xk.append(X)
    Xk[i] = X
    #Ajusts for number of R values

result = Functions.FourierTransformCal(samplePoints, Xk, radius)
Xkf_act = result[0]
Xktot = result[1]

#graph plots
Functions.PlotResults(Rf,Xkf_act)