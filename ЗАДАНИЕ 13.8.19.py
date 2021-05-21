tickets_number = int(input('Введите кол-во билетов: '))
total = 0

for c in range(1, tickets_number + 1):
    age = int(input(f'Введите возраст посетителя №{c}: '))
    if 18 <= age <= 24:
        total += 990
        print(f'Стоимость билета для поситителя №{c} = 990руб')
    elif age >= 25:
        total += 1390
        print(f'Стоимость билета для поситителя №{c} = 1390руб')
    elif age < 18:
        print(f'Для поситителя №{c} предоставляется бесплатный билет')
if tickets_number <= 3:
    print(f'Сумма к оплате: {total}')
else:
    print('---')
    print(f'Общая стоимость билеток: {total}')
    print(f'Сумма к оплате с учетом скидки 10%: {round(total * 1.1, 2)}')
