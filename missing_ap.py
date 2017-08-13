def div(b, e):
    mid = int((b+e)/2)
    an = int(a[0] + mid*r)
    #para quando tiver 1 ou menos elemento
    if (e-b) <= 1:
        if a[mid] == an:
            return (a[mid]+r)
        else:
            return (a[mid]-r)

    else:
        if a[mid] == an:
            return div(mid+1, e)
        else:
            return div(b, mid)

a = []
t = int(input())

while(t > 0):
    n = int(input())
    for i in range(n):
        new = int(input())
        a.append(new)
    r = int((a[n-1] - a[0]) / n)
    aux = div(0, n)
    print(aux)
    r = 0
    del a[:]
    t = t-1
