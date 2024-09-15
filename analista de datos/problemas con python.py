from pulp import *

pelotaFutbol = LpVariable("pelotaFutbol", 0, 400)#son sus restricciones 0<=x1 <=400
pelotaBasquet = LpVariable("pelotaBasquet", 0, 300)#0<=x2 <=300

#declaramos constantes y variables que usaremos para delimitar el problema
materialUnidadF = 100
materialUnidaB = 125

materialDisponible = 50000

gananciaF = 5
gananciaB = 4

#agregamos la variable problema
problema = LpProblem("problema", LpMaximize)#se debe especificar si va a ser de maximizacion o minimizacion

#agregamos las restricciones faltantes al problema
problema += (materialUnidadF*pelotaFutbol) + (materialUnidaB*pelotaBasquet) <= materialDisponible

#agregamos al problema la funcion objetivo
problema += (pelotaFutbol*gananciaF) + (pelotaBasquet*gananciaB)

status = problema.solver(GLPK(msg=0))#las status que puede arrojar son optimal, not solve, undefined
print(LpStatus)
print(value(pelotaFutbol))
print(value(pelotaBasquet))