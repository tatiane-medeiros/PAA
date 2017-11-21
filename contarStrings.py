def letter(st):
    for i in st:
        if ord(i) > 64 and ord(i) < 91:
            return True
        elif ord(i) > 96 and ord(i) < 123:
            return True

    return False


aux = input().split(' ')
count = int(0)
for i in range(len(aux)):
    if letter(aux[i]):
        count = count+1

print(count)
