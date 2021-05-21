text = input()  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == first:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)

'''L = input('Введите последовательноcть символов:\n')
n = 0
first = L[0]
res = ''

for i in L:
    if i == first:
        n += 1
    else:
        res += first + str(n)
        n = 1
        first = i
print(res)'''