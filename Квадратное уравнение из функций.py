import math
def discr(a,b,c):
    return b ** 2 - 4 * a * c
def solf(a,b,c,discr):
    print(f'Формула Дискриминанта:\nD = b^2 - 4ac    \nДискриминант = {b**2} - 4({a})({c}) = {discr(a, b, c)}')
    if discr(a, b, c) > 0:
        x1, x2 = (-b - math.sqrt(discr(a, b, c))) / (2 * a), (-b + math.sqrt(discr(a, b, c))) / (2 * a)
        print(f'Он имеет 2 корня    \nx1 = (-({b}) - √D) / 2 * ({a})    \nx2 = (-({b}) + √D) / 2 * ({a})    \nx1 = {x1}\nx2 = {x2}')
    elif discr(a,b,c) == 0:
        x = -b / (2 * a)
        print(f'Он имеет 1 корень    \nx = -({b}) / 2 * ({a})\nx = {x}')
    else:
        print('Он не имеет корней')
abc = []
task = input('Напиши индексы квадратного уравнения ax^2 + bx + c =0 {a b c} "С дробями не работаем!":')
for ind in task.split(): abc.append(ind)
a,b,c = int(abc[0]),int(abc[1]),int(abc[2])
solf(a,b,c,discr)