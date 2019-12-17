a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a > b and a > c:
    print('Первое число наибольшее')
if b > c and b > a:
    print('Второе число наибольшее')
if c > b and c > a:
    print('Третье число наибольшее')
if a == b and a == c:
    print('Числа равны')