from pulp import *
# icpc 2018 World Finals
# Problem C
# Conquer the World
# Felipe Gatica Ramírez
# 06 Octubre 2019

# cantidad total de ciudades
n = 3
# ciudades
nations = ["1", "2", "3"]
# ejercitos en la nacion i
supply = {"1": 2, "2": 5, "3":1} 
demand = {"1": 1, "2": 0, "3":3}
costs = [[0,5,5], [5,0,100000],[5,100000,0]]

#print("demand[u] : " demand[1][0])
#print("demand[v] : " demand[0][1])
#n = 6
#nations = ["1", "2", "3", "4", "5", "6"]
#supply = {"1": 0, "2": 1, "3":2, "4":3, "5":0, "6":0} 
#demand = {"1": 0, "2": 0, "3":1, "4":1, "5":1, "6":1}
#costs = [[0,2,5,1,100000, 100000], [2,0,100000, 100000,5,1], [5,100000,0,100000,100000,100000],[1,100000,100000,0,100000,100000],[100000,5,100000,100000,0,100000],[100000,1,100000,100000,100000,0]]

costs = makeDict([nations,nations],costs,0)
print("costs : ", costs)
prob = LpProblem("Conquer the World", LpMinimize)

Routes = [(u,v) for u in nations for v in nations]
print("Routes : ", Routes)
vars = LpVariable.dicts("Route",(nations, nations),0,None,LpInteger)
print("vars : ", vars)

prob += lpSum([vars[u][v]*costs[u][v] for (u,v) in Routes]), "Sum_of_Transporting_Costs"

for u in nations:
    prob += lpSum([vars[u][v] for v in nations])<=supply[u], "Sum_of_costs_out_of_nations_%s"%u
for v in nations:
    prob += lpSum([vars[u][v] for u in nations])>=demand[v], "Sum_of_costs_into_nations%s"%v

prob += lpSum([vars[u][v] for (u,v) in Routes]) <= 10000, "Sum_total_of_demands: " 

sumyprob = lpSum([vars[u] for u in supply])
prob += lpSum([vars[u][v] for (u,v) in Routes]) >=  sumyprob, "Sum_demand"
	
# The problem data is written to an .lp file
prob.writeLP("BeerDistributionProblem.lp")

prob.solve()
print("Total Cost of Transportation =",value(prob.objective))
