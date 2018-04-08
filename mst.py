import queue

def prim(graph): 
    vstd, tree = {},{}
    edges = []
    for i in list(graph.keys()):
        v = i
        tree[i]= {}
    
    vstd[v] = True
    q = queue.PriorityQueue()
    for i in graph[v]:
        q.put( ( graph[v][i] , i, v ) )

    cost = 0
    while not q.empty():
        e = q.get()
        if e[1] in vstd : continue
        vstd[e[1]] = True
        cost += e[0]
        edges.append((e[1],e[2]))
        tree[e[1]][e[2]] = e[0]
        tree[e[2]][e[1]] = e[0]
        for v in graph[e[1]]:
            if v not in vstd:
                q.put((graph[e[1]][v], v, e[1]))

    return cost, tree

def dfs(graph, v, i, color, connected):
    color[v] = i
    connected[i].append(v)
    for u in graph[v] :
        if u not in color:
            dfs(graph, u, i, color, connected)


t = int(input())
while t > 0:
    graph = {}
    n,m = map( int , input().split() )
    for i in range(m):
        u, v, c = map( int , input().split() )
        try :
                graph[u][v] = c*(-1)
        except :
                graph[u] = {}
                graph[u][v] = c*(-1)
        try :
                graph[v][u] = c*(-1)
        except :
                graph[v] = {}
                graph[v][u] = c*(-1)

    p = prim(graph)
    print(p[0]*(-1))
    t -= 1
 
