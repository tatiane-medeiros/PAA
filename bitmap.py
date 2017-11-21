col = int(0)

def comp(mat, li,lf,ci,cf):
    x = -1
    for i in range(li,lf+1):
        for j in range(ci,cf+1):
            if mat[i][j] != x:
                if x == -1: x = mat[i][j]
                else: return 'D'
        
    return x

def divide(mat, li,lf,ci,cf):
    if lf==lf or ci==cf: pass
    t = comp(mat, li,lf,ci,cf)
    if t != 'D':
        if t!=-1:
            print(t, end='')
            col.addCol()
            if col.col() >= 50:
                col.reset()
     
    else:
        print('D', end='')
        col.addCol()
        if col.col() >= 50:
            col.reset()
        if (lf-li <= 1) and (cf-ci <= 1): pass
        ml = int((li+lf)/2)
        mc = int((ci+cf)/2)
        #quadrantes
        divide(mat, li,ml,ci,mc)
        divide(mat, li,ml,mc+1,cf)
        divide(mat, ml+1,lf,ci,mc)
        divide(mat, ml+1,lf,mc+1,cf)

class columns:
    def __init__(self):
        self.__col = 0
    def addCol(self):
        self.__col = self.__col + 1
    def col(self):
        return self.__col
    def reset(self):
        print('')
#        print(self.__col)
        self.__col = 0
        
n = int(input())

while(n>0):
    aux = input()
    l,c = list(map(int, aux.split()))
    if l>0 and c>0:
        matrix =[]
        aux =[]
        #lê matriz
        for i in range(l):
            aux = input()
            aux = list(map(int, aux))
            matrix.append(aux)
        col = columns()
        divide(matrix, 0,l-1,0,c-1)
        print('')
    n = n-1
