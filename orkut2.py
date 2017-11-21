from collections import deque

x = 0
n = int(input())
while n > 0:	
	links, falta = {}, {}	
	queue = []
	x += 1	
	names = list(input().split())
	for i in range(n):
		links[names[i]] = []
		falta[names[i]] = 0		

	for i in range(n):
		entrada = input().split()
		src = entrada[0]	
		amigos = entrada[2:]
		
		falta[src] += int(entrada[1])
		for amigo in amigos:
			links[amigo].append(src)

	for i in range(n):
		if falta[names[i]] == 0:
			queue.append(names[i])	

	queue = deque(queue)
	ans = []
	while (len(queue) > 0):
		u = queue.popleft()
		ans.append(u)		
		for k in links[u]:		
			falta[k] -= 1
			if falta[k] == 0:
				queue.append(k)

	print("Teste %d" % x)
	if len(ans) == n:
		print(*ans)
	else:
		print("impossivel")
	print()
	n = int(input())
	
