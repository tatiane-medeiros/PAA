n = 1
while(n != 0):    
    n = int(input())
    if n == 0:
        break
    i = 0
    x1=0
    while(i<=1 and i<(n-1)):
        print(x1, end=" ")
        x1 = 1 
        i = i+1
    x2 = 0
    while(i<(n-1)):
        f = x1 + x2
        print(f, end=" ")
        x2 = x1
        x1 = f
        i = i+1
    else:
        f = x1 + x2
        print(f)
