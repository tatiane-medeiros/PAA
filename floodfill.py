comp = 0
def dfs(fr):
    print( "Visited " + str(fr) )
    vstd[fr] = True
    for u in graph[fr]:
        if not vstd[u]:
            dfs(u)
        pass
    pass
# 0 - branco, 1 - cinza, 2 - preto
def flofi(u, color):
    dfs_num[u] = color
    for v in graph[u]:
        if dfs_num[v] == 0: flofi(v, color)
    

graph = {}
vstd = []
dfs_num = []

for i in range(8):
    vstd.append(False)
    dfs_num.append(0)

graph[1] = [2]
graph[2] = [1,3]
graph[3] = [2]
graph[4] = [5]
graph[5] = [4,6]
graph[6] = [5]
graph[7] = []


for u in graph:
    if dfs_num[u] == 0:
        dfs(u)
        comp +=1
        flofi(u, comp)
        
