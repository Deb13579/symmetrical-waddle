import pandas as pd
import csv

df = pd.read_csv("Final2.csv")

Radius = df["Radius"].to_list()
Mass = df["Mass"].to_list()

def planet_mass (Radius, Mass): 
    for i in range(0,len(Radius)-1):
        Mass[i] = float(Mass[i]) * 1.989e+30
        Radius[i] = float(Radius[i]) * 6.957e+8

planet_mass(Radius, Mass)

planet_gravity = []

def gravity(Radius, Mass):
    g = 6.674e-11
    for index in range (0,len(Mass)):
        G = (Mass[index]*g)/((Radius[index])**2)
        planet_gravity.append(G)

gravity(Radius, Mass)

df ["gravity"] = planet_gravity
df.to_csv("Final2.csv")