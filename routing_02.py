from pulp import *

Warehouses = ["A", "B"]
supply = {"A": 1000, "B": 4000}
Bars = ["1", "2", "3", "4", "5"]
demand = {"1":500, "2":900, "3":1800, "4":200, "5":700,}

costs = [[2,4,5,2,1], [3,1,3,2,3]]
costs = makeDict([Warehouses,Bars],costs,0)
prob = LpProblem("Beer Distribution Problem",LpMinimize)
Routes = [(w,b) for w in Warehouses for b in Bars]
vars = LpVariable.dicts("Route",(Warehouses,Bars),0,None,LpInteger)
prob += lpSum([vars[w][b]*costs[w][b] for (w,b) in Routes]), "Sum_of_Transporting_Costs"

for w in Warehouses:
    prob += lpSum([vars[w][b] for b in Bars])<=supply[w], "Sum_of_Products_out_of_Warehouse_%s"%w

for b in Bars:
    prob += lpSum([vars[w][b] for w in Warehouses])>=demand[b], "Sum_of_Products_into_Bar%s"%b

prob.solve()
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Cost of Transportation = ", value(prob.objective))
