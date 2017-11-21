import queue
def dijkstra(start,end, graph, dist, second):
    dist[start] = 0
    second[start] = 0
    pq = queue.PriorityQueue()
    pq.put([0, start])
    while not pq.empty():
        #0 prori, 1 vertice 
        node = pq.get()
        if int(node[0]) > dist[(node[1])]:
            continue                                                                   
        for v in graph[node[1]]:
            aux = dist[v[0]]           
            if aux > int(node[0]) + v[1] :
                if v[0] == end and aux != 2**20:
                    second[int(v[0])] = aux                    
                #priori + dist adjacente               
                dist[v[0]] = int(node[0]) + v[1]
                if v[0] == end or node[1] == start :
                    v[2] = 1
                    if end == 1: break                
                pq.put([dist[v[0]], v[0]])
    #print(dist)               
    pq.put([0, start])
    while not pq.empty():
        node = pq.get()
        if int(node[0]) > second[(node[1])]:
            continue                                                                   
        for v in graph[node[1]]:
            if v[2] == 0:
                aux = second[v[0]]      
                if aux > int(node[0]) + v[1] :                     
                    second[v[0]] = int(node[0]) + v[1]
                    pq.put([second[v[0]], v[0]])
                    
    #print(second)
        
    if second[end] != 2**20: return second[end]
    else: return -1
n,m = 1,1
while(n != 0 and m != 0):          
    n,m = map(int, input().split())
    if n==0 and m==0: break
    s,d = map(int, input().split())
    graph = {}
    for i in range(n): graph[i] = []
    dist = [2**20]*n
    second = [2**20]*n
    for i in range(m):
        u,v,c = map(int,input().split())
        #direcionado
        graph[u].append([v, c, 0])

    a = dijkstra(s,d,graph,dist, second)
    print(a)
