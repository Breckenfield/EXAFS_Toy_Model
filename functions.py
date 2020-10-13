import scipy
import numpy
import json
import plotly.graph_objs as go

def LoadMaterialInfo(fileName):
    with open(fileName, "r") as json_file:
        materialInfo = json.load(json_file)
    print("These are the materials present in Material.json:")
    for material in materialInfo:
        print("- " + material)
    return materialInfo

def EXAFSCal(num, i, K, R, sig):
    value = num[i]*((((numpy.sin(2.0*K*R[i]))/(K*R[i]**2.0))*(numpy.exp((-2.0)*(sig)*(K**2.0)))))*K**2
    return value

def SigmaCal(materialTemp, einsteinTemp, atomicMass):
    hbar = 1.05e-34
    boltzmannConstant = 1.38e-23
    u = (atomicMass/2)*1.66e-27
    sigmaTemp = ((hbar**2)/(2*einsteinTemp*boltzmannConstant*u))*(numpy.cosh(einsteinTemp/(2*materialTemp))/numpy.sinh(einsteinTemp/(2*materialTemp)))*1e20 #sigma squared
    sigma = (sigmaTemp*4 + sigmaTemp*2 + sigmaTemp)/4 #linear multiple scattering effect
    return sigma

def RfCal(samplePoints):
    Nhalf = int(samplePoints/2)
    Rf = numpy.linspace(0, 15.7201257862 , Nhalf)
    return Rf

def FourierTransformCal(samplePoints, Xk, radius):
    Nhalf = int(samplePoints/2)
    Xk_total = numpy.zeros(samplePoints)
    for j in range(len(radius)):
        Xk_total = Xk_total + Xk[j]
        # Fourier transform of Xk
        Xkf = scipy.fft.fft(Xk_total)
    Xkf_act = (2/samplePoints * numpy.abs(Xkf[0:Nhalf]))*100
    return Xkf_act

def CheckMaterialInput(radius, numberOfAtoms, atomicMass, einsteinTemp):
    checkLength = len(radius)
    check = True
    if checkLength > 0:
        if len(numberOfAtoms) != checkLength:
            print("The Number of Atoms list length in the Material.json file is different to the Radius list")
            check = False
        if len(atomicMass) != checkLength:
            print("The Atomic Mass list length in the Material.json file is different to the Radius list")
            check = False
        if len(einsteinTemp) != checkLength:
            print("The Einstein Tempurature list length in the Material.json file is different to the Radius list")
            check = False
    else:
        print("The Radius list has no content")
        check = False
    return(check)

def K_RangeCal(sampleSpacing, samplePoints):
    K = numpy.linspace(sampleSpacing, samplePoints*sampleSpacing, samplePoints)
    return K

def PlotResults(Rf, Xkf_act):
    print("Plotting Result")
    fig = go.Figure(data=go.Scatter(x=Rf, y=Xkf_act))
    fig.write_html('EXAFS_Graph.html', auto_open=True)
    return True
