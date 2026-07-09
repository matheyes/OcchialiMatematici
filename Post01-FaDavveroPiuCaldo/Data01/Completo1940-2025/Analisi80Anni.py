# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:55:15 2021

@author: carlo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def Regression(X,Y):
    #regressione di y su x
    Covariance=np.cov(X,Y)[0][1]
    VarX=np.cov(X,Y)[0][0]
    VarY=np.cov(X,Y)[1][1]
    XMed=np.mean(X)
    YMed=np.mean(Y)
    m=Covariance/VarX
    q=YMed-m*XMed
    r=Covariance/(np.sqrt(VarX)*np.sqrt(VarY))
    return m,q,r


#leggere da FILE

dfOP4025 = pd.read_csv('OceanoPacificoSud1940-2025.csv')
TempOP4080=dfOP4025[dfOP4025["time"]<1980]["temp"].values
TempOP8125=dfOP4025[dfOP4025["time"]>=1980]["temp"].values
dfSv4025 = pd.read_csv('Svalbard1940-2025.csv')
TempSv4080=dfSv4025[dfSv4025["time"]<1980]["temp"].values
TempSv8125=dfSv4025[dfSv4025["time"]>=1980]["temp"].values
dfPP4025 = pd.read_csv('PianuraPadana1940-2025.csv')
TempPP4080=dfPP4025[dfPP4025["time"]<1980]["temp"].values
TempPP8125=dfPP4025[dfPP4025["time"]>=1980]["temp"].values
dfCE4025 = pd.read_csv('CongoEquatore1940-2025.csv')
TempCE4080=dfCE4025[dfCE4025["time"]<1980]["temp"].values
TempCE8125=dfCE4025[dfCE4025["time"]>=1980]["temp"].values

Time4080=dfOP4025[dfOP4025["time"]<1980]["time"].values
Time8125=dfOP4025[dfOP4025["time"]>=1980]["time"].values
TimeTot=dfOP4025["time"].values


TutteTemp=np.concatenate((TempOP4080, TempOP8125,TempSv4080, TempSv8125,TempPP4080,TempPP8125,TempCE4080,TempCE8125))
TempMax=np.max(TutteTemp)
TempMin=np.min(TutteTemp)


RegrTimeA=np.array([1940,1980])
RegrTimeB=np.array([1981,2025])
RegrTimeAB=np.array([1940,2025])

mOP4080,qOP4080,rOP4080=Regression(Time4080,TempOP4080)
RegrTempA=mOP4080*RegrTimeA+qOP4080
mOP8125,qOP8125,rOP8125=Regression(Time8125,TempOP8125)
RegrTempB=mOP8125*RegrTimeB+qOP8125
TempOP4025=np.concatenate((TempOP4080,TempOP8125))
mOP4025,qOP4025,rOP4025=Regression(TimeTot,TempOP4025)
RegrTempAB=mOP4025*RegrTimeAB+qOP4025

plt.plot(Time4080,TempOP4080,".b",Time8125,TempOP8125,".b")
plt.plot(RegrTimeA,RegrTempA,RegrTimeB,RegrTempB,RegrTimeAB,RegrTempAB,"r--")
plt.xlabel("t(y)")
plt.ylabel("T(K)")
plt.title("Oceano Pacifico")
plt.grid()
plt.show()

mSv4080,qSv4080,rSv4080=Regression(Time4080,TempSv4080)
RegrTempA=mSv4080*RegrTimeA+qSv4080
mSv8125,qSv8125,rSv8125=Regression(Time8125,TempSv8125)
RegrTempB=mSv8125*RegrTimeB+qSv8125
TempSv4025=np.concatenate((TempSv4080,TempSv8125))
mSv4025,qSv4025,rSv4025=Regression(TimeTot,TempSv4025)
RegrTempAB=mSv4025*RegrTimeAB+qSv4025

plt.plot(Time4080,TempSv4080,".m",Time8125,TempSv8125,".m")
plt.plot(RegrTimeA,RegrTempA,RegrTimeB,RegrTempB,RegrTimeAB,RegrTempAB,"r--")
plt.xlabel("t(y)")
plt.ylabel("T(K)")
plt.title("Svalbard")
plt.grid()
plt.show()

mPP4080,qPP4080,rPP4080=Regression(Time4080,TempPP4080)
RegrTempA=mPP4080*RegrTimeA+qPP4080
mPP8125,qPP8125,rPP8125=Regression(Time8125,TempPP8125)
RegrTempB=mPP8125*RegrTimeB+qPP8125
TempPP4025=np.concatenate((TempPP4080,TempPP8125))
mPP4025,qPP4025,rPP4025=Regression(TimeTot,TempPP4025)
RegrTempAB=mPP4025*RegrTimeAB+qPP4025

plt.plot(Time4080,TempPP4080,".r",Time8125,TempPP8125,".r")
plt.plot(RegrTimeA,RegrTempA,RegrTimeB,RegrTempB,RegrTimeAB,RegrTempAB,"r--")
plt.xlabel("t(y)")
plt.ylabel("T(K)")
plt.title("Pianura Padana")
plt.grid()
plt.show()

mCE4080,qCE4080,rCE4080=Regression(Time4080,TempCE4080)
RegrTempA=mCE4080*RegrTimeA+qCE4080
mCE8125,qCE8125,rCE8125=Regression(Time8125,TempCE8125)
RegrTempB=mCE8125*RegrTimeB+qCE8125
TempCE4025=np.concatenate((TempCE4080,TempCE8125))
mCE4025,qCE4025,rCE4025=Regression(TimeTot,TempCE4025)
RegrTempAB=mCE4025*RegrTimeAB+qCE4025

plt.plot(Time4080,TempCE4080,".g",Time8125,TempCE8125,".g")
plt.plot(RegrTimeA,RegrTempA,RegrTimeB,RegrTempB,RegrTimeAB,RegrTempAB,"r--")
plt.xlabel("t(y)")
plt.ylabel("T(K)")
plt.title("Congo Equatore")
plt.grid()
plt.show()

plt.plot(TimeTot,TempOP4025,"b",label="Oceano Pacifico")
plt.plot(TimeTot,TempSv4025,"m",label="Svalbard")
plt.plot(TimeTot,TempPP4025,"r",label="Pianura Padana")
plt.plot(TimeTot,TempCE4025,"g",label="Congo Equatore")

plt.ylim(TempMin,TempMax)
plt.title("1940-2025")
plt.legend()
plt.xlabel("t(y)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

