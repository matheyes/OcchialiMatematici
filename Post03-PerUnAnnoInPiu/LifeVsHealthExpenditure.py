# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:55:15 2021

@author: carlo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#load data into a DataFrame object:

#leggere da FILE

LifeHealthExp = pd.read_csv('LifeVsHealthExpenditureData.csv')

Countries=np.unique(LifeHealthExp.Entity.astype(str))
i=0
for country in Countries:
    i+=1
    Expences=LifeHealthExp[LifeHealthExp["Entity"]==country]["HealthExpenditurePerCapita"].values
    Life=LifeHealthExp[LifeHealthExp["Entity"]==country]["LifeExpectancy"].values
    plt.plot(Expences,Life,label=country)
    plt.title("Spesa sanitaria e aspettativa di vita")
    plt.xlabel("Spesa sanitaria procapite ($)")
    plt.ylabel("Asp. vita alla nascita")
    #plt.tight_layout()
    plt.xlim([0,13000])
    plt.ylim([50,86])
    plt.legend()
    #print(i)
    
    if i%5==0:
        plt.grid()
        plt.show()
        #print("---",i%4)

plt.grid()
plt.show()
#print("---",i%4)

# GRAFICO COMPLESSIVO

LifeHealthExp2 = pd.read_csv('life-expectancy-vs-health-expenditure.csv')

Countries=np.unique(LifeHealthExp2.Entity.astype(str))

for country in Countries:
    Expences=LifeHealthExp2[LifeHealthExp2["Entity"]==country]["HealthExpenditurePerCapita"].values
    Life=LifeHealthExp2[LifeHealthExp2["Entity"]==country]["LifeExpectancy"].values
    plt.plot(Expences,Life)
    plt.xlim([0,13000])
    plt.ylim([50,86])


plt.title("Spesa sanitaria e aspettativa di vita (59 paesi)")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.grid()
plt.show()
#-----------------------------divisi per anni------------------------
for country in Countries:
    Expences=LifeHealthExp2[LifeHealthExp2["Entity"]==country][LifeHealthExp2["Year"]<=2000]["HealthExpenditurePerCapita"].values
    Life=LifeHealthExp2[LifeHealthExp2["Entity"]==country][LifeHealthExp2["Year"]<=2000]["LifeExpectancy"].values
    plt.plot(Expences,Life,'.r')
    plt.xlim([0,13000])
    plt.ylim([50,86])
for country in Countries:
    Expences=LifeHealthExp2[LifeHealthExp2["Entity"]==country][LifeHealthExp2["Year"]>2000]["HealthExpenditurePerCapita"].values
    Life=LifeHealthExp2[LifeHealthExp2["Entity"]==country][LifeHealthExp2["Year"]>2000]["LifeExpectancy"].values
    plt.plot(Expences,Life,'.b')
    plt.xlim([0,13000])
    plt.ylim([50,86])

plt.title("Spesa sanitaria e aspettativa di vita (1970-2000)")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.grid()
plt.show()

#---------Fit a mano con logistica-----------------------------
def logistic(t):
    # y=k/(1+exp(-r(t-t0)))
    t0=-1800
    k=81.5
    r=0.0008
    y=k/(1+np.exp(-r*(t-t0)))
    return y

def logarithmic(t):
    #y=alpha + beta log(t)
    alpha=45
    beta=4.2
    y=alpha + beta * np.log(t)
    return y

def hyperbolic(t):
    #y=kh/(t-t0)+y0
    kh=-20000
    t0=-1000
    y0=84
    y=kh/(t-t0)+y0
    return y

ageTh1=[] #logistica
ageTh2=[] #logaritmica
ageTh3=[] #iperbolica
times=np.linspace(0,11000,200)
for t in times:
    ageTh1.append(logistic(t))
    ageTh2.append(logarithmic(t))
    ageTh3.append(hyperbolic(t))
ageTh1=np.array(ageTh1)
ageTh2=np.array(ageTh2)
ageTh3=np.array(ageTh3)

for country in Countries:
    Expences=LifeHealthExp2[LifeHealthExp2["Entity"]==country]["HealthExpenditurePerCapita"].values
    Life=LifeHealthExp2[LifeHealthExp2["Entity"]==country]["LifeExpectancy"].values
    plt.plot(Expences,Life,'.r')
    
    plt.xlim([0,13000])
    plt.ylim([50,86])

plt.plot(times,ageTh1,'b',label="logistic")
plt.plot(times,ageTh2,'g',label="logarithmic")
plt.plot(times,ageTh3,'y',label="hyperbolic")
plt.legend()
plt.title("Spesa sanitaria e aspettativa di vita")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.grid()
plt.show()

LifeHealthExp3 = pd.read_csv('LifeVsHealthExpenditureDataNoOutliers.csv')

spesaPasso=200
ExpenceDots=[]
LifeDots=[]
yerror=[]
for spesa in range(0,8000,spesaPasso):
    Expences=LifeHealthExp3[LifeHealthExp3["HealthExpenditurePerCapita"]<=spesa+spesaPasso/2][LifeHealthExp3["HealthExpenditurePerCapita"]>spesa-spesaPasso/2]["HealthExpenditurePerCapita"].values
    Life=LifeHealthExp3[LifeHealthExp3["HealthExpenditurePerCapita"]<=spesa+spesaPasso/2][LifeHealthExp3["HealthExpenditurePerCapita"]>spesa-spesaPasso/2]["LifeExpectancy"].values
    ExpenceDots.append(spesa)
    LifeDots.append(np.mean(Life))
    Lifemax=np.max(Life)
    Lifemin=np.min(Life)
    dLife=(Lifemax-Lifemin)/2
    yerror.append(dLife)
    
plt.errorbar(ExpenceDots,LifeDots,yerr=yerror, fmt='.',color='r')
plt.xlim([0,13000])
plt.ylim([50,86])
plt.title("Spesa sanitaria e aspettativa di vita")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.grid()
plt.show()

plt.errorbar(ExpenceDots,LifeDots,yerr=yerror, fmt='.',color='r')
plt.plot(times,ageTh1,'b',label="logistic")
plt.xlim([0,13000])
plt.ylim([50,86])
plt.title("Spesa sanitaria e aspettativa di vita")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.legend()
plt.grid()
plt.show()

plt.errorbar(ExpenceDots,LifeDots,yerr=yerror, fmt='.',color='r')
plt.plot(times,ageTh2,'g',label="logarithmic")
plt.xlim([0,13000])
plt.ylim([50,86])
plt.title("Spesa sanitaria e aspettativa di vita")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.legend()
plt.grid()
plt.show()

plt.errorbar(ExpenceDots,LifeDots,yerr=yerror, fmt='.',color='r')
plt.plot(times,ageTh3,'y',label="hyperbolic")
plt.xlim([0,13000])
plt.ylim([50,86])
plt.title("Spesa sanitaria e aspettativa di vita")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.legend()
plt.grid()
plt.show()

plt.errorbar(ExpenceDots,LifeDots,yerr=yerror, fmt='.',color='r')
plt.plot(times,ageTh1,'b',label="logistic")
plt.plot(times,ageTh2,'g',label="logarithmic")
plt.plot(times,ageTh3,'y',label="hyperbolic")
plt.xlim([0,13000])
plt.ylim([50,86])
plt.title("Spesa sanitaria e aspettativa di vita")
plt.xlabel("Spesa sanitaria procapite ($)")
plt.ylabel("Asp. vita alla nascita")
plt.legend()
plt.grid()
plt.show()


