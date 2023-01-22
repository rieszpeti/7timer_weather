import numpy as np

#Apparent Temparature calculating
#AT = Ta + 0.33e - 0,7v - 4
#Ta = dry bulb temperature (°C)
#e = water vapour pressure (hPa)
#v = wind speed (m/s) at an elevation of 10 m
#e=RH/100⋅6.105⋅exp(17.27⋅Ta237.7+Ta)

def e(df):
    eLeft = np.multiply(np.divide(df['rh2m', 'mean'].astype(float), 100), 6.105)
    numerator = np.multiply(df['temp2m', 'mean'].astype(float), 17.27)
    denominator = np.add(df['temp2m', 'mean'].astype(float), 237.7)
    insideExp = np.divide(numerator, denominator)
    eRight = np.exp(insideExp)
    return np.multiply(eLeft, eRight)

def apparentTemp(df):
    multiplyE = np.multiply(e(df), 0.33)
    multiplyV = np.multiply(df['windspeed', 'mean'], 0.7)
    taSumE = np.add(df['temp2m', 'mean'], multiplyE)
    vSumScal = np.subtract(multiplyV, 4)
    return np.subtract(taSumE, vSumScal)

