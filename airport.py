import queue


def mst(v,a):
    cost = 0
    vr(v)
    while not q.empty():
        f = q.get()
        u = (-1)*f[1]
        w = (-1)*f[0]

        if oc[u] == 0:
            if a <= w:
                while not q.empty():
                    q.get()
                break;
            else:
                cost += w
            vr(u)
    return cost
        
 
def vr(u):
    oc[u] = 1    
    for i in range(len(graph[u])):
        v = graph[u][graph[u].keys()[i]]
        if oc[v[1]] == 0:
            q.put([v[1]*(-1), v[1]*(-1)])

            

t = int(input())
while t > 0:
    n,m,a = map(int, input().split())
    q = queue.PriorityQueue()
    cost, r = 0, 0
    graph = {}
    for i in range(m):
        u,v,c =  map(int, input().split())
        try :
                graph[u][v] = c
        except :
                graph[u] = {}
                graph[u][v] = c
        try :
                graph[v][u] = c
        except :
                graph[v] = {}
                graph[v][u] = c

    oc = [0 for i in range(n)]
    for i in range(n):
        if oc[i] == 0:
            cost += mst(i,a) + a
            r +=1
            

    t -=1
