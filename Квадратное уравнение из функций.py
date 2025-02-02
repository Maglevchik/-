import math
def discr(a,b,c):
    return b ** 2 - 4 * a * c
def solf(a, b, c):
    d = discr(a, b, c)
    print(f'Формула Дискриминанта:\nD = b^2 - 4ac\nДискриминант = {b ** 2} - 4({a})({c}) = {d}')

    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(f'Два корня:\nx1 = {x1}\nx2 = {x2}')
    elif d == 0:
        x = -b / (2 * a)
        print(f'Один корень:\nx = {x}')
    else:
        print('Корней нет')

abc = input('Введите коэффициенты квадратного уравнения ax^2 + bx + c = 0 (например, 1 25/49 3): ').split()
a = float(abc[0])
b = float(abc[1])
c = float(abc[2])
solf(a, b, c)
