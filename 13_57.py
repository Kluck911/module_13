A = int(input(f'Введите двузначное число:\n'))

first = A // 10
second = A % 10

if first == 5 or second == 5:
    print('Входит')
else:
    print('Не входит')
