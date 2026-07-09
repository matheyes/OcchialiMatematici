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

dfSv4041 = pd.read_csv('Svalbard2yr1940-41.csv')
TempSv4041=dfSv4041["temp"].values
dfSv8283 = pd.read_csv('Svalbard2yr1982-83.csv')
TempSv8283=dfSv8283["temp"].values
dfSv2425 = pd.read_csv('Svalbard2yr2024-25.csv')
TempSv2425=dfSv2425["temp"].values

dfPP4041 = pd.read_csv('PianuraPadana2yr1940-41.csv')
TempPP4041=dfSv4041["temp"].values
dfPP8283 = pd.read_csv('PianuraPadana2yr1982-83.csv')
TempPP8283=dfPP8283["temp"].values
dfPP2425 = pd.read_csv('PianuraPadana2yr2024-25.csv')
TempPP2425=dfPP2425["temp"].values

dfCE4041 = pd.read_csv('CongoEquatore2yr1940-41.csv')
TempCE4041=dfCE4041["temp"].values
dfCE8283 = pd.read_csv('CongoEquatore2yr1982-83.csv')
TempCE8283=dfCE8283["temp"].values
dfCE2425 = pd.read_csv('CongoEquatore2yr2024-25.csv')
TempCE2425=dfCE2425["temp"].values

dfOP4041 = pd.read_csv('OceanoPacificoSud2yr1940-41.csv')
TempOP4041=dfOP4041["temp"].values
dfOP8283 = pd.read_csv('OceanoPacificoSud2yr1982-83.csv')
TempOP8283=dfOP8283["temp"].values
dfOP2425 = pd.read_csv('OceanoPacificoSud2yr2024-25.csv')
TempOP2425=dfOP2425["temp"].values

TutteTemp=np.concatenate((TempSv4041,TempSv8283,TempSv2425,TempPP4041,TempPP8283,TempPP2425,TempCE4041,TempCE8283,TempCE2425,TempOP4041,TempOP8283,TempOP2425))
TempMax=np.max(TutteTemp)
TempMin=np.min(TutteTemp)

plt.plot(TempSv4041,"b",label="1940-41")
plt.plot(TempSv8283,"m",label="1982-83")
plt.plot(TempSv2425,"r",label="2024-25")

plt.ylim(TempMin,TempMax)
plt.title("Svalbard")
plt.legend()
plt.xlabel("t(d)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

plt.plot(TempPP4041,"b",label="1940-41")
plt.plot(TempPP8283,"m",label="1982-83")
plt.plot(TempPP2425,"r",label="2024-25")

plt.ylim(TempMin,TempMax)
plt.title("Pianura Padana")
plt.legend()
plt.xlabel("t(d)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

plt.plot(TempCE4041,"b",label="1940-41")
plt.plot(TempCE8283,"m",label="1982-83")
plt.plot(TempCE2425,"r",label="2024-25")

plt.ylim(TempMin,TempMax)
plt.title("Congo Equatore")
plt.legend()
plt.xlabel("t(d)")
plt.ylabel("T(K)")
plt.grid()
plt.show()

plt.plot(TempOP4041,"b",label="1940-41")
plt.plot(TempOP8283,"m",label="1982-83")
plt.plot(TempOP2425,"r",label="2024-25")

plt.ylim(TempMin,TempMax)
plt.title("Oceano Pacifico Sud")
plt.legend()
plt.xlabel("t(d)")
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

