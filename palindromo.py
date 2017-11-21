def palindromo(s):
    n = len(s)
    m = [[0 for i in range(n)] for i in range(n)]
    for i in range(n): m[i][i] = 1
    for k in range(1, n):
        for i in range(n - k):
            j = i+k
            if s[i] == s[j]:
                if k == 1: m[i][j] = 2
                else: m[i][j] = m[i+1][j-1] +2
            else:
                m[i][j] = max(m[i][j-1], m[i+1][j])
    return m[0][n-1]

t = int(input())
for i in range(t):
    string = input()
    if string:
        print(palindromo(string))
