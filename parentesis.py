
n = int(input())
while n>0:
    st = input()
    pilha = []
    for x in st:
        if x == '(' or x == '[':
            pilha.append(x)
        elif x == ')':
            if pilha:
                c = pilha.pop()
                if c != '(':
                    pilha.append(c)
                    break
            else:
                pilha.append(x)
                break
        elif x == ']':
            if pilha:
                c = pilha.pop()
                if c != '[':
                    pilha.append(c)
                    break
            else:
                pilha.append(x)
                break
    if pilha: print("No")
    else: print("Yes")
            
    
    n -= 1;
