M = [[i+j for j in range(1, 11)] for i in range(1, 11)]

for i1 in range (1, 11):
    print('---')
    for j1 in range(1, 11):
        print(f'{i1}*{j1}={i1 * j1}')