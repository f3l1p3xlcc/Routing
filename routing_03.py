from pulp import *
# icpc 2018 World Finals
# Problem C
# Conquer the World
# Felipe Gatica Ramírez
# 04 Octubre 2019

# cantidad total de ciudades
#n = 3
# ciudades
#nations = ["1", "2", "3"]
# ejercitos en la nacion i
#supply = {"1": 2, "2": 5, "3":1} 
#demand = {"1": 1, "2": 0, "3":3}
#costs = [[0,5,5], [5,0,100000],[5,100000,0]]

n = 6
nations = ["1", "2", "3", "4", "5", "6"]
supply = {"1": 0, "2": 1, "3":2, "4":3, "5":0, "6":0} 
demand = {"1": 0, "2": 0, "3":1, "4":1, "5":1, "6":1}
costs = [[0,2,5,1,100000, 100000], [2,0,100000, 100000,5,1], [5,100000,0,100000,100000,100000],[1,100000,100000,0,100000,100000],[100000,5,100000,100000,0,100000],[100000,1,100000,100000,100000,0]]

costs = makeDict([nations,nations],costs,0)
prob = LpProblem("Conquer the World", LpMinimize)
Routes = [(w,b) for w in nations for b in nations]
vars = LpVariable.dicts("Route",(nations, nations),0,None,LpInteger)
prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Transporting_Costs"

for w in nations:
    prob += lpSum([vars[w][b] for b in nations])<=supply[w], "Sum_of_costs_out_of_nations_%s"%w
for b in nations:
    prob += lpSum([vars[w][b] for w in nations])>=demand[b], "Sum_of_costs_into_nations%s"%b
for xi in nations:
	prob += lpSum([vars[w][b] for xi2 in nations]) <= 1000000, "Sum_total_of_costs%s"%xi
for xi in nations:
	prob += lpSum([vars[w][b] for xi2 in nations]) >= demand[xi], "Sum_demand%s"%xi
	
    
prob.solve()
print("Total Cost of Transportation =",value(prob.objective))

