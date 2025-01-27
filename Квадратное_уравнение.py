import math

from test.test_descrtut import defaultdict

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))


D = b**2 - 4*a*c
if D > 0:
    x1 = (-b - math.sqrt(D)) / (2*a)
    x2 = (-b + math.sqrt(D)) / (2*a)
    print(f'x1 =', x1)
    print(f'x2 =', x2)
elif D == 0:
    x = -b / (2 * a)
    print('x =', x)
else:
    print('Решений нет')

match D:
    case _ if D > 0:
        x1 = (-b - math.sqrt(D)) / (2*a)
        x2 = (-b + math.sqrt(D)) / (2*a)
        print('x1 =', x1)
        print('x2 =', x2)
    case _ if D < 0:
        print('Решений нет')
    case _:
        x = -b / 2 / a
        # альтернативная запись:
        x = -b / (2 * a)
        print('x =', x)


