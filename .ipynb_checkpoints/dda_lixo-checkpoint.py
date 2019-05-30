# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import math
import random

DIFICULDADE_MAX = 9 
DIFICULDADE_MIN = 0

def DefineDensidade(dificuldade):
    dif = (dificuldade)*0.8 + 2.7
    return math.floor((dif - 1.9)/0.8)

def AcresceDificuldade(dificuldade, quant):
    if (dificuldade + quant > DIFICULDADE_MAX):        
        return DIFICULDADE_MAX
    elif (dificuldade + quant < DIFICULDADE_MIN):
        return DIFICULDADE_MIN
    else:
        return dificuldade + quant

def CalculaDesempenho(tirosAcertados, tirosGastos, vidaRestante, inimigosDerrotados, numInimigos, reloadAuto, reloadManual):
    grandezaR = reloadManual/reloadAuto
    if(grandezaR > 1):
        grandezaR = 1        
    
    return ( vidaRestante/5 + inimigosDerrotados/numInimigos + grandezaR)/3

desempenho = 0
dificuldade = 5
densidade = DefineDensidade(dificuldade)
fase = 1

for i in range(0,10):
    print("Fase", fase)
    
    tirosGastos = random.randint(1,300)
    tirosAcertados = random.randint(1,tirosGastos)
    
    vidaRestante = 0
    if(random.randint(0,1) == 0):        
        vidaRestante = random.randint(1,5)
        
    numInimigos = random.randint(1,32)
    inimigosDerrotados = numInimigos
    if(vidaRestante == 0 ):        
        inimigosDerrotados = random.randint(1,numInimigos)
    else:
        fase= fase +1
    reloadAuto = random.randint(1,21)
    reloadManual = random.randint(1,21)
    desempenho = CalculaDesempenho(tirosAcertados, tirosGastos, vidaRestante, inimigosDerrotados, numInimigos, reloadAuto, reloadManual)
        
    dificuldadeTemp = dificuldade
    
    if(desempenho >= 0.7):
        dificuldade = AcresceDificuldade(dificuldade, 1)        
    elif(desempenho < 0.3):
        dificuldade = AcresceDificuldade(dificuldade, -1)
    
    print("TG:", tirosGastos,"TA:", tirosAcertados,"HP:", vidaRestante,"INIMIGOS:", numInimigos,"INIMIGOS_D:", inimigosDerrotados,"R_AUTO:", reloadAuto,"R_MANUAL:", reloadManual)
    print("Desempenho:",desempenho)
    print("Dificuldade", dificuldadeTemp, "->", dificuldade)
    densidade = DefineDensidade(dificuldade)
    print("Densidade", densidade)