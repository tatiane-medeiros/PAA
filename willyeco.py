def summ(v, b, e, c):
    s = 0
    for i in range(b,e):
        if c < v[i]:
            s += (v[i] - c)
    return s

def cut(v, b, e, m):
    if b == e: return v[b]    
    a = int((e+b)/2)
    s = summ(v,a,len(v), v[a])

    #busca binaria
    if s == m:
        return v[a]
    elif s < m:
        return cut(v,b,a,m)
    else:
        if summ(v,a+1,e,v[a+1]) < m: return v[a]
        else: return cut(v,a+1,e,m)
     


trees =[]
aux = input()
n, m = list(map(int, aux.split()))
aux = input()
trees = list(map(int, aux.split()))
trees.sort()
print(cut(trees,0,len(trees),m))
