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

df01_40 = pd.read_csv('PianuraPadana3ggda01a03-01-1940.csv')
Temp01_40=df01_40["temp"].values
df04_40 = pd.read_csv('PianuraPadana3ggda01a03-04-1940.csv')
Temp04_40=df04_40["temp"].values
df07_40 = pd.read_csv('PianuraPadana3ggda01a03-07-1940.csv')
Temp07_40=df07_40["temp"].values
df10_40 = pd.read_csv('PianuraPadana3ggda01a03-10-1940.csv')
Temp10_40=df10_40["temp"].values

df01_80 = pd.read_csv('PianuraPadana3ggda01a03-01-1980.csv')
Temp01_80=df01_80["temp"].values
df04_80 = pd.read_csv('PianuraPadana3ggda01a03-04-1980.csv')
Temp04_80=df04_80["temp"].values
df07_80 = pd.read_csv('PianuraPadana3ggda01a03-07-1980.csv')
Temp07_80=df07_80["temp"].values
df10_80 = pd.read_csv('PianuraPadana3ggda01a03-10-1980.csv')
Temp10_80=df10_80["temp"].values

df01_20 = pd.read_csv('PianuraPadana3ggda01a03-01-2020.csv')
Temp01_20=df01_20["temp"].values
df04_20 = pd.read_csv('PianuraPadana3ggda01a03-04-2020.csv')
Temp04_20=df04_20["temp"].values
df07_20 = pd.read_csv('PianuraPadana3ggda01a03-07-2020.csv')
Temp07_20=df07_20["temp"].values
df10_20 = pd.read_csv('PianuraPadana3ggda01a03-10-2020.csv')
Temp10_20=df10_20["temp"].values

TutteTemp=np.concatenate((Temp01_40,Temp04_40,Temp07_40,Temp10_40,Temp01_80,Temp04_80,Temp07_80,Temp10_80,Temp01_20,Temp04_20,Temp07_20,Temp10_20))
TempMax=np.max(TutteTemp)
TempMin=np.min(TutteTemp)

plt.plot(Temp01_40,"b",label="01")
plt.plot(Temp04_40,"m",label="04")
plt.plot(Temp07_40,"r",label="07")
plt.plot(Temp10_40,"c",label="10")
plt.ylim(TempMin,TempMax)
plt.title("PianuraPadana 1940")
plt.legend()
plt.xlabel("t(h)")
plt.ylabel("T(K)")
plt.grid()
plt.show()


plt.plot(Temp01_80,"b",label="01")
plt.plot(Temp04_80,"m",label="04")
plt.plot(Temp07_80,"r",label="07")
plt.plot(Temp10_80,"c",label="10")
plt.ylim(TempMin,TempMax)
plt.title("PianuraPadana 1980")
plt.legend()
plt.xlabel("t(h)")
plt.ylabel("T(K)")
plt.grid()
plt.show()


plt.plot(Temp01_20,"b",label="01")
plt.plot(Temp04_20,"m",label="04")
plt.plot(Temp07_20,"r",label="07")
plt.plot(Temp10_20,"c",label="10")
plt.ylim(TempMin,TempMax)
plt.title("PianuraPadana 2020")
plt.legend()
plt.xlabel("t(h)")
plt.ylabel("T(K)")
plt.grid()
plt.show()




#Selezionare un intervallo e salvare su file - ogni ora
"""
TimeA="2020-10-01 00:00:00"
TimeB="2020-10-04 00:00:00"

TimeAB=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["valid_time"].values
TempAB=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["t2m"].values

plt.plot(TempAB)
plt.title("OceanoPacificoSud 1-3/10/2020")
plt.xlabel("t(h)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

df = pd.DataFrame({
    "time": TimeAB,
    "temp": TempAB
})

df.to_csv("OceanoPacificoSud3ggda01a03-10-2020.csv", index=False)
"""

#medie giornaliere in un intervallo e salvare su file
"""
TimeA="2024-01-01 00:00:00"
TimeB="2026-01-01 00:00:00"

TimeABhours=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["valid_time"].values
TempABhours=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["t2m"].values

TimeABdays=[]
TempABdays=[]

for i in range(0,len(TimeABhours),24):
    Date=TimeABhours[i][0:10]
    somma=0
    for j in range(24):
        somma+=TempABhours[i+j]
    Temp=somma/24
    TimeABdays.append(Date)
    TempABdays.append(Temp)
        
    

plt.plot(TempABdays)
plt.title("Svalbard 2024-25")
plt.xlabel("t(d)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

df = pd.DataFrame({
    "time": TimeABdays,
    "temp": TempABdays
})

df.to_csv("Svalbard2yr2024-25.csv", index=False)
"""

#medie mensili in un intervallo e salvare su file
"""
TimeA="1940-01-01 00:00:00"
TimeB="1942-01-01 00:00:00"

TimeABhours=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["valid_time"].values
TempABhours=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["t2m"].values

TimeABmonths=[]
TempABmonths=[]

i=0
while i < len(TimeABhours):
    Date=TimeABhours[i][0:7]
    somma=0
    j=0
    while i+j<len(TimeABhours) and TimeABhours[i+j][0:7]==Date:
        somma+=TempABhours[i+j]
        j+=1
    Temp=somma/j
    TimeABmonths.append(Date)
    TempABmonths.append(Temp)
    i+=j
        
    

plt.plot(TempABmonths)
plt.title("PianuraPadana 1940-41")
plt.xlabel("t(d)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

df = pd.DataFrame({
    "time": TimeABmonths,
    "temp": TempABmonths
})

df.to_csv("PianuraPadana 1940-41.csv", index=False)
"""
#medie annuali in un intervallo e salvare su file
"""
TimeA="1940-01-01 00:00:00"
TimeB="2026-01-01 00:00:00"

TimeABhours=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["valid_time"].values
TempABhours=df[(df["valid_time"]<TimeB) & (df["valid_time"]>=TimeA)]["t2m"].values

TimeAByears=[]
TempAByears=[]

i=0
while i < len(TimeABhours):
    Date=TimeABhours[i][0:4]
    somma=0
    j=0
    while i+j<len(TimeABhours) and TimeABhours[i+j][0:4]==Date:
        somma+=TempABhours[i+j]
        j+=1
    Temp=somma/j
    TimeAByears.append(Date)
    TempAByears.append(Temp)
    i+=j
        
    

plt.plot(TempAByears)
plt.title("OceanoPacificoSud 1940-2025")
plt.xlabel("t(yr)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

df = pd.DataFrame({
    "time": TimeAByears,
    "temp": TempAByears
})

df.to_csv("OceanoPacificoSud1940-2025.csv", index=False)
"""

