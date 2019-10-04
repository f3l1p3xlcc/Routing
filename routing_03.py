from pulp import *
# icpc 2018 World Finals
# Problem C
# Conquer the World
# Felipe Gatica Ramírez
# 04 Octubre 2019

# cantidad total de ciudades
n = 3
# ciudades
nations = ["1", "2", "3"]
# ejercitos en la nacion i
supply = {"1": 2, "2": 5, "3":1} 
demand = {"1": 1, "2": 0, "3":3}

costs = [[0,5,5], [5,0,0], [5,0,0]]
costs = makeDict([nations,nations],costs,0)
prob = LpProblem("Conquer the World", LpMinimize)
Routes = [(w,b) for w in nations for b in nations]
vars = LpVariable.dicts("Route",(nations, nations),0,None,LpInteger)
prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Transporting_Costs"

prob.solve()
print("Total Cost of Transportation =",value(prob.objective))

