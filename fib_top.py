def fib(x):
    if x <= 2:
        memo[x-1] = 1
        return 1
    if(memo[x-1]):
        a = memo[x-1]
    else: 
        a = fib(x-1)
        memo[x-1] = a
    if(memo[x-2]):
        b = memo[x-2]
    else: 
        b = fib(x-2)
        memo[x-2] = b
    return a+b

n = 1
while(n != 0):    
    n = int(input())
    if n == 0:
        break
    i = 0
    memo = [0]*n
    fib(n)
    print(memo)
