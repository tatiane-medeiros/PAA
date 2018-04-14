import queue

def dijkstra(start, graph, dist):
    dist[start] = 0
    pq = queue.PriorityQueue()
    pq.put([0, start])
    while not pq.empty():
        node = pq.get()
        if  node[0] > dist[node[1]]:
            continue
        for v in graph[node[1]]:
            if dist[v[0]] > node[0] + v[1]:
                dist[v[0]] = node[0] + v[1]
                pq.put([dist[v[0]], v[0]])
    return dist

# n é a quantidade de vértices e m é a quantidade de arestas
# O grafo é bidirecionado
n, m = map(int, input().split())
graph = {}
for j in range(m):
    u, v, c = map(int, input().split())
    if u not in graph:
        graph[u] = [[v, c]]
    else:
        graph[u].append([v, c])
    if v not in graph:
        graph[v] = [[u, c]]
    else:
        graph[v].append([u, c])
dist = [2 ** 10 for l in range(n + 1)]
dist = dijkstra(1, graph, dist)
