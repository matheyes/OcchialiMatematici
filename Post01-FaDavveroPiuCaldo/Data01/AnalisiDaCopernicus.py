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

df = pd.read_csv('OceanoPacificoSud1940-2026hourly.csv')

#If you have a large DataFrame with many rows, 
#Pandas will only return the first 5 rows, and the last 5 rows:
print(df) 
print(" ")

df.info() #specifica che colonne ci sono, di che tipo e quanti dati non nulli per ciascuna

DesDes=df.describe() # per ogni colonna media, devst e descrizione a 5 parametri
print(DesDes)
print(DesDes.loc["mean"]["t2m"])

Temp2m=df["t2m"].values
Time=df["valid_time"].values


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


