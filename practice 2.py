x = int(input('Введите год: '))
if x % 400 == 0 and x % 4 == 0:
    print('Год високосный')
if x % 100 == 0 and x % 400 != 0:
    print('Год невисокосный')