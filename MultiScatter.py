<<<<<<< HEAD
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
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6 13:18 2015
Updated on Thur Feb 6 10:56 2020

@author: Connor Breckenfield
First step to build EXAFS scattering model
Capable of calculating for multiple R values, Disorder over multiple scattering paths
using the Einstine model for temperature.
"""
import scipy
import numpy
import matplotlib.pyplot as plt
import json
import Functions

# Distance between center and local atom (Example Cu: [2.2, 3.3, 4.1, 4.7, 5.3, 5.8])
#R = [2.2, 3.3, 4.1, 4.7, 5.3, 5.8]
# Number of atoms at each radius (Example Cu: [12, 6, 24, 32, 12, 8])
#num = [12, 6, 24, 32, 12, 8]
#Temperature
#temp = 300 #In kelvin no lower than 1
#Atomic mass (Example Cu: 63.546)
#Da = 63.546 
#Einstein temperature (Example Cu: 343.5)
#Oe = 343.5

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
N = 100000
# Sample spacing
T = 1.0/10

# Computation of K value range
K = numpy.linspace(T, N*T, N)

# X-axis for fourier transform
Rf = Functions.RfCal(N)

# Simplified EXAFS equation with K^2 weighting for all R values
Xk = []
for i in range(len(radius)):
    u = Functions.ConvertAtomicMass(atomicMass[i])
    sig = Functions.SigmaCal(temp, einsteinTemp[i], u)
    X = Functions.EXAFSCal(num, i, K, radius, sig)
    Xk.append(X)
    Xk[i] = X
    #Ajusts for number of R values

result = Functions.FourierTransformCal(N, Xk, radius)
Xkf_act = result[0]
Xktot = result[1]

#graph plots
Functions.PlotResults(K, Xktot, Rf, Xkf_act, radius)
>>>>>>> 74dbc5617633e31937701271eef442d80d1747bd
