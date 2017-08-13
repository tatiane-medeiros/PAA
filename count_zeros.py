def firstZ(b, e):
    mid = int((b+e)/2)
    #para quando encontrar 1 seguido de 0 e retorna a posição do primeiro 0
    if (e-b) <= 1:
        if a[mid] == 1:
            return (mid + 1)
        else:
            return mid
    else:
        if a[mid] == 1:
            return firstZ(mid+1, e)
        else:
            return firstZ(b, mid)

a = []
t = int(input())
while(t > 0):
    n = int(input())
    for i in range(n):
        new = int(input())
        a.append(new)
    aux = firstZ(0, n)
    print(n - aux)
    del a[:]
    t = t-1
