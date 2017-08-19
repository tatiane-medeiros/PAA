import math
#calcula raiz quadrada
def raiz(x):
    r = 1
    e = False
    while(e == False):
        res = r + ((x - (r*r))/(2*r))
        rp = res*res
        if (float(rp-x) == 0) or (math.fabs(rp-x)< 0.000000000000001) or ( r == res):
            e = True
        else:
            r = res
    return res

n = float(input())
print(raiz(n))
