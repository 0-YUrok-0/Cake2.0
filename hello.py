'''
На квадратном торте размером N×N расставлено M свечей. 
Определить, можно ли одним прямолинейным разрезом разделить торт на две части, равные по площади, так, 
чтобы все свечи оказались на одной половине. Свечи считаем точками. Разрез не может проходить через свечу. 
in.txt - N x1 y1 x2 y2 ... xM yM.
'''

import copy  

def candles():
    file1 = open("in.txt", "r")
    line = file1.readline().strip()
    args = line.split(' ') # Список с входящими данными
    N = int(args.pop(0))
    if len(args) % 2 != 0:
        return("Не хватает yM?")
    if N % 2 != 0:
        return("Введите чётное поле") 
    x1 = N / 2
    y1 = N / 2
    args_bass = copy.copy(args)
    for i in range(0, len(args), 2):
        x2 = int(args.pop(i))
        y2 = int(args.pop(i))
        if x2 == 0 or y2 == 0 or x2 >= N or y2 >= N:
            return("Свеча не может стоять на краю") 
        if x1 == x2 and y1 == y2:
            return("Нет")
        if x2 == x1:
            x2 += 1
            y2 = 0
        if y2 == y1:
            x2 = 0
            y2 += 1
        sign = set() 
        zero = list()
        for k in range(0, len(args), 2):
            x = int(args[k])
            y = int(args[k+1])
            if x1 == x and y1 == y:
                return("Нет, свеча в геометрическом центре")
            delta = (x - x1)/(x2 - x1) - (y - y1)/(y2 - y1)
            if delta > 0:
                sign.add("+")
            elif delta < 0:
                sign.add("-")
            elif delta == 0:
                zero.append(x)
                zero.append(y)
        if len(sign) <= 1 and len(zero) == 0:
            return("Можно!")
        if len(sign) <= 1 and len(zero) != 0:
            zero.append(x2)
            zero.append(y2)
            if (x2 < x1 and y2 < y1) or (x2 > x1 and y2 > y1):
                xn = N
                yn = 0
            else:
                xn = 0
                yn = 0
            sign = set()
            for j in range(0, len(zero), 2):
                x = zero[j]
                y = zero[j+1]
                delta = (x - x1)/(xn - x1) - (y - y1)/(yn - y1)
                if delta > 0:
                    sign.add("+")
                else:
                    sign.add("-")
            if len(sign) != 1:
                return("Увы и Ах!")
            else:
                return("Можно!")
        args = copy.copy(args_bass)
    return("Увы и Ах!")
print(candles())
