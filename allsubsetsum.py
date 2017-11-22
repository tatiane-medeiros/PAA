def printlist(l):
    for i in l: print(i, end = ' ')
    print('')


def allsub(array, n, soma):
    if n==0 or soma<0:
        return
    global dp
    dp = [[True]*(soma+1) for i in range(n)]
    if array[0] <= soma:
        dp[0][array[0]] = True
    for i in range(n):
        for j in range(soma+1):
            dp[i][j] = (dp[i-1][j] or dp[i-1][j- array[i]]) if (array[i] <=j) else (dp[i-1][j])
            
    if dp[n-1][soma] == False:
        print("none")

    p = []
    subsets(array, n-1, soma, p)

def subsets(array, i,soma,p):
    if (i==0) and  soma and dp[0][soma]:
        p.append(array[i])
        if soma <=1: printlist(p)
        return 
    elif i==0 and soma == 0:
        printlist(p)
        return 
    elif dp[i-1][soma]:
        b = []
        b.extend(p)
        subsets(array, i-1, soma, b)
    if soma >= array[i] and dp[i-1][soma- array[i]]:
        p.append(array[i])
        subsets(array, i-1, soma - array[i],p)
   # printlist(p)



array = [1,2,3,4,5,6,7,8,9,10]
d = 10
m = 3

allsub(array, 10, d)


