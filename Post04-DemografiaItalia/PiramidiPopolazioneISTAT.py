# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:55:15 2021

@author: carlo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



#load data into a DataFrame object:
DatiMaschi = pd.read_csv('TavolaIstat1861-2021Maschi.csv')
DatiFemmine = pd.read_csv('TavolaIstat1861-2021Femmine.csv')

Anni=DatiMaschi["anno"].values
#leggere da FILE
AgeClasses = DatiMaschi.columns[1:].to_numpy()

for censim in range(16):
    anno=str(DatiMaschi.iloc[censim,0])
    MaleTot = DatiMaschi.iloc[censim, 1:].to_numpy()/5
    FemaleTot = DatiFemmine.iloc[censim, 1:].to_numpy()/5
     
    plt.barh(AgeClasses, -MaleTot, align='center',alpha=0.9, color = 'b',label="Maschi")
    
    plt.barh(AgeClasses, FemaleTot, align='center', alpha=0.6, color = 'r',label="Femmine")
    plt.title("Italia "+anno)
    plt.xlim([-500,500])
    
    ticks = plt.xticks()[0]
    plt.xticks(ticks, [abs(int(x)) for x in ticks])
    
    plt.xlabel("popolazione per anno (migliaia)")
    plt.ylabel("Età")
    plt.legend()
    plt.grid()
    plt.show() 


