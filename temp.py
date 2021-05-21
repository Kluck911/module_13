print(round(2.53*5.36, 2))

'''
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10, 0, -1)]
# 10 9 8 7 6 5 4 3 2 1

for a, b in zip(L,M):
    print('| a =', a, 'b =', b, '|  a * b = ', a * b)

# ИЛИ N = [a*b for a, b in zip(L,M)]
# print(N)


нужно записать логическое выражение, используя all([ ]) 
и any([ ]) над списком четности, если его результат будет 
истинным тогда и только тогда, когда в списке есть хотя бы 
один четный и хотя бы один нечетный элемент.

L = [int(input()) % 2 == 0 for i in range(5)]
print(L)
print(any(L) and not all(L))

---
L = list(map(int, input().split()))
print(L)
print(any(L))

a = int(input())

if all([type(a) == int,
       100 <= a <= 999,
       a % 2 == 0,
       a % 3 == 0]):
    print("Число удовлетворяет условиям")


n = int(input("Введите число\n"))

while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3 + 1) // 2
    print(n)

    if n == 1:
        print("Done")
        break



list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
    if value < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)'''