from random import random
n = int(random() * 10)
i = 1
print("Мы загодали число, попробуй кгадай. У тебя есть 3 попытки")
while i <= 3:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Много')
    elif u < n:
        print('Мало')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы исчерпали 3 попытки. Было загадано', n)