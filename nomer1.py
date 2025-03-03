while 1:
    a = input('Введите начало диапозона:')
    b = input("Введите конец диапозона:")
    if a.isnumeric() == True and b.isnumeric() == True:
        a, b = int(a), int(b)
        break


def prost(a):
    k = 0
    for i in range(2, a//2+1):
        if a % i == 0:
            k+=1
    if k<=0:
        return a


lst = []
for i in range(a, b+1):
    f = prost(i)
    if f != None:
        lst.append(f)
print(lst)