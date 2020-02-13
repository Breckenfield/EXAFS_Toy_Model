# -*- coding: utf-8 -*-
"""
Created on Fri Nov 6 13:18 2015
Updated on Thur Feb 6 10:56 2020

@author: Connor Breckenfield
First step to build EXAFS scattering model
Capable of calculating for multiple R values, Disorder over multiple scattering paths
using the Einstine model for temperature.
"""
import scipy as sp
import numpy as np
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

materialName = input("Pick a Material to simulate: ")

with open("Material.json", "r") as json_file:
    materialInfo = json.load(json_file)

for m in materialInfo["Material"]:
    if m["Name"] == materialName:
        R = m["RadiusDistance"]
        num = m["NumberOfAtoms"]
        temp = m["Temperature"]
        Da = m["AtomicMass"]
        Oe = m["EinsteinTemperature"]

#------------------------------------#
#---No user input below this point---#
#------------------------------------#

# Number of samplepoints
N = 100000
# Sample spacing
T = 1.0/ 10
   
# Constants
hbar = 1.05e-34
Kb = 1.38e-23
u = (Da/2)*1.66e-27

# Sigma calculation
sig = Functions.SigmaCal(temp, Oe, hbar, Kb, u)

# Computation of K value range
K = np.linspace(T, N*T, N)

# Array and list creation
Xk = []

# X-axis for fourier transform
Rf = Functions.RfCal(N)

# Simplified EXAFS equation with K^2 weighting for all R values
for i in range(len(R)):
    X = Functions.EXAFSCal(num, i, K, R, sig)
    Xk.append(X)
    Xk[i] = X
    #Ajusts for number of R values

result = Functions.FourierTransformCal(N, Xk, R)
Xkf_act = result[0]
Xktot = result[1]

#graph plots
Functions.PlotResults(K, Xktot, Rf, Xkf_act, R, materialName)
