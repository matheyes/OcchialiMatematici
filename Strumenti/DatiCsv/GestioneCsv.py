# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 18:27:54 2026

@author: carlo
"""
import pandas as pd
import numpy as np

df = pd.read_csv('Tabella.csv')



Pesi=df["Peso"].values

Distanza=np.array([0.39, 0.72, 1.0, 1.52]) #distanza dal Sole in U.A.
Periodo=np.array([0.24,0.62, 1.0,1.88]) #periodo orbitale in anni
Pianeti=np.array(["Mercurio","Venere","Terra","Marte"])

SistemaSolare=pd.DataFrame({
    "Pianeta":Pianeti,
    "Distanza":Distanza,
    "Periodo":Periodo})

SistemaSolare.to_csv("DatiSS.csv",index=False) #index=False serve per non numerare le righe
