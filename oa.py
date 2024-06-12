import pulp

# 定义问题
pb = pulp.LpProblem("pb", pulp.LpMinimize)
'''
n = 1-10  人
m = 1-7  天
w = 1-3 时段
'''
# 初始化变量
# 使用字典表示多维决策变量
X = pulp.LpVariable.dicts("X", ((i,j,w) for i in range(10) for j in range(7) for w in range(3)), cat=pulp.LpBinary)
t = pulp.LpVariable.dicts("t", (i for i in range(10)), cat=pulp.LpInteger)
b = pulp.LpVariable("b", lowBound=0)

# 目标函数：
pb += pulp.lpSum((t[i]-b) for i in range(10))

# 约束条件1：每人每日只能上一个班
for i in range(10):
    for j in range(7):
        for w in range(3):
            pb += pulp.lpSum(X[i,j,w] for w in range(3)) <= 1

# 约束条件2：每人每周工作小于5天
for i in range(10):
    pb += pulp.lpSum(X[i,j,w] for j in range(7) for w in range(3)) <= 5

# 约束条件3：每班有两人值班
for j in range(7):
    for w in range(3):
        pb += pulp.lpSum(X[i,j,w] for i in range(10)) == 2

# 4 t[i]为每人工作总时长
for i in range(10):
    pb += t[i] == pulp.lpSum(8*X[i,j,w] for j in range(7) for w in range(3))

# 5 b为所有人平均工作时长
pb += b == pulp.lpSum(0.125*t[i] for i in range(10))

# 求解问题
pb.solve()

# 输出结果，只输出为1的x值
print("Status:", pulp.LpStatus[pb.status])
print("Objective value:", pulp.value(pb.objective))
for v in pb.variables():
    if v.varValue != 0:
        print(v.name, "=", v.varValue)
