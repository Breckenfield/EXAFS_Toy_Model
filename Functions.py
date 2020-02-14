import scipy
import numpy
import matplotlib.pyplot as plt

def EXAFSCal(num, i, K, R, sig):
    X = num[i]*((((numpy.sin(2.0*K*R[i]))/(K*R[i]**2.0))*(numpy.exp((-2.0)*(sig)*(K**2.0)))))*K**2
    return X

def SigmaCal(temp, Oe, hbar, Kb, u):
    sigTemp = ((hbar**2)/(2*Oe*Kb*u))*(numpy.cosh(Oe/(2*temp))/numpy.sinh(Oe/(2*temp)))*1e20 #sigma squared
    sig = (sigTemp*4 + sigTemp*2 + sigTemp)/4 #linear multiple scattering effect
    return sig

def RfCal(N):
    Nhalf = int(N/2)
    Rf = numpy.linspace(0, 15.7201257862 , Nhalf)
    return Rf

def FourierTransformCal(N, Xk, R):
    Nhalf = int(N/2)
    Xktot = numpy.zeros(N)
    for j in range(len(R)):
        Xktot = Xktot + Xk[j]
        # Fourier transform of Xk
        Xkf = scipy.fft.fft(Xktot)
    Xkf_act = (2/N * numpy.abs(Xkf[0:Nhalf]))*100
    return Xkf_act, Xktot

def ConvertAtomicMass(Da):
    u = (Da/2)*1.66e-27
    return u

def PlotResults(K, Xktot, Rf, Xkf_act, R):
    plt.figure(1)
    plt.plot(K,Xktot)
    plt.xlim(0,30)
    plt.ylabel("$X{K^{2}})$|($\AA^{-2}$)")
    plt.xlabel('K $(\AA^{-1})$')

    plt.figure(2)
    plt.plot(Rf, Xkf_act)
    plt.grid()
    plt.ylabel("|FT($X{K^{2}})$|($\AA^{-3}$)")
    plt.xlabel('R $(\AA)$')
    plt.xlim(0.0, R[len(R)-1]+1)
    plt.show()