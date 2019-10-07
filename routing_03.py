from pulp import *
# icpc 2018 World Finals
# Problem C
# Conquer the World
# Felipe Gatica Ramírez
# 06 Octubre 2019

# cantidad total de ciudades
#n = 3
# ciudades
#nations = ["1", "2", "3"]
# ejercitos en la nacion i
#supply = {"1": 2, "2": 5, "3":1} 
# demanda en la nacion i
#demand = {"1": 1, "2": 0, "3":3}
# costo de mover los ejercitos 
# el costo 100000 significa que es muy alto mucho mayor que la suma de los costos reales, se interpreta como infinito.
#costs = [[0,5,5], [5,0,100000],[5,100000,0]]

n = 6
nations = ["1", "2", "3", "4", "5", "6"]
supply = {"1": 0, "2": 1, "3":2, "4":3, "5":0, "6":0} 
demand = {"1": 0, "2": 0, "3":1, "4":1, "5":1, "6":1}
costs = [[0,2,5,1,100000, 100000], [2,0,100000, 100000,5,1], [5,100000,0,100000,100000,100000],[1,100000,100000,0,100000,100000],[100000,5,100000,100000,0,100000],[100000,1,100000,100000,100000,0]]

# se crea un diccionario con los costos.
costs = makeDict([nations,nations],costs,0)
# se define el problema.
prob = LpProblem("Conquer the World", LpMinimize)
# tupla con todas las rutas posibles.
Routes = [(u,v) for u in nations for v in nations]
# diccionario con todas las variables del problema.
vars = LpVariable.dicts("Route",(nations, nations),0,None,LpInteger)

#Función Objetivo
prob += lpSum([vars[u][v]*costs[u][v] for (u,v) in Routes]), "Suma de los costos de transporte"

# Restricciones

for u in nations:
    prob += lpSum([vars[u][v] for v in nations])<=supply[u], "Sum_of_costs_out_of_nations_%s"%u

for v in nations:
    prob += lpSum([vars[u][v] for u in nations])>=demand[v], "Sum_of_costs_into_nations%s"%v


prob += lpSum([vars[u][v] for (u,v) in Routes]) <= 10000, "Suma total de las demandas: " 

#sumprob1 = lpSum([vars[u] for u in supply])
#sumprob2 = lpSum([vars[u] for u in demand])
#print("sumprob1:",sumprob2)
#print("sumprob2:",sumprob2)
#for u in nations:
#	for v in nations:
#		prob += vars[u][v] >= demand[u], "Numero total de ejercitos"
	
# The problem data is written to an .lp file
prob.writeLP("BeerDistributionProblem.lp")
prob.solve()
print("Total Cost of Transportation =",value(prob.objective))
