#s = '(2(лп(3л)в)4(н))'
def init()->str:
    while 1:
        s = input('Введите команду для спутника')
        if s.count(')')==s.count('('):
            return s
        print('Данные введины не корректно!')


def decoder(s:str)->None:
    while 1:
        for e, x in enumerate(s):
            if x == ')':
                for y in range(e-1, -1, -1):
                    if s[y] == '(':
                        b = y
                        break
                temp = s[b:e+1].replace('(', '').replace(')', '')
                if s[b+1].isdigit():
                    temp = temp[1:]*int(temp[0])
                if s[b-1].isdigit():
                    b = b-1
                    temp*= int(s[b])
                s = s[:b] + temp + s[e+1:]

                break
        if s.count(')') == 0:
            break
    print(s)


if __name__ == '__main__':
    s = init()
    decoder(s)