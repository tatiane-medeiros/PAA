import time

def pot(k):
    i = 0
    while(k>1):
        if k%2: return -1
        k = k/2
        i += 1
    return i
        
k, m = 1,1
while(k != 0):
    k,m = map(int, input().split())
    if k == 0: break
    graph = {}
    adj = []
   
    for i in range(k):
        graph[i] = []
        adj.append(0)
    for i in range(m):
        u, v = map(int, input().split())
        if (u in graph) and (v in graph):
            graph[u].append(v)
            graph[v].append(u)
            adj[u] += 1
            adj[v] += 1

    n = pot(k)
    if n == -1: print("NAO")
    elif (2**(n-1))*n == m:
        chk = 0
        for i in range(1,k):
            if adj[i] != n:
                chk = -1
                break
        if chk != -1: print("SIM")
        else: print("NAO")
    else:
        print("NAO")
        

