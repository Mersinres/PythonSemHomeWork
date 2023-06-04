# HomeWorkPython
# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

x = int(input('Введите трехзначное число '))
if (x < 100 or x > 999):
    print('Вы ввели не трехзначное число!')
else:
    sum = 0
    i = 0
    while i < 3:
        a = x % 10
        x = x // 10
        sum += a
        i +=1
    print ("Сумма цифр цифр числа ", sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input ('Введите общее кол-во журавликов: '))
x = int(s / 6)

if s % 6 != 0:
    print("Доделай журавликов и спроси снова! ")
else:
    print(f"Петя сделал {x} журавликов, Катя сделала {x * 4} журавликов, Сережа сделал {x} журавликов.")

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется
# написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = input('Введите номер билета: ')
if len(n) != 6:
    print(" Номер билета введен не правильно!")
else:
    i = 0
    sum1 = 0
    sum2 = 0
    while i < 6:
        if i < 3:
            sum1 += int(n[i])
            i += 1
        else:
            sum2 += int (n[i])
            i += 1
    if sum1 == sum2:
        print('Ваш билет счастливый!')
    else:
        print('В этот раз не повезло')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите число долек длины шоколадки '))
m = int(input('Введите число долек ширины шоколадки '))
k = int(input('Сколько долек вы хотите отломить? '))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да, можно разломить по прямой')
else:
    print('Увы, по прямой разломить не получится ')


# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

N = int(input('Введите количество монет '))
obverse = revers = 0              
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        obverse += 1
    else:
        revers += 1
if obverse < revers:
    print(f'Переверните {obverse} монет с орла на решку, их меньше всего')
elif obverse == revers:
    print(f'Количество орлов и решек одинаково, переворачивай что хочешь xD')
else:
    print((f'Переверните {revers} монет с решки на орла, их меньше всего'))


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа
# 4 4 -> 2 2
# 5 6 -> 2 3


s = int(input('Задай сумму двух чисел \n'))
p = int(input('Задай произведение чисел \n'))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'первое число "{x}", второе число "{y}"')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input('Введи число N:'))
i = 0
while 2 ** i <= n:
    print(f' 2 в степени {i} равна {2 ** i}')
    i += 1


# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите размер элементов списка: '))
list_n = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_n))
x = int (input('Введите число х: '))
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается в списке  {count} раз.')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#     5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int(input("Введите количество элементов в массиве "))
list = [random.randint(1, 20) for i in range(N)]
print(list)
x = int(input("Введите искомое число "))
index_element = 0
min_element = abs(x - list[0])
for i in range(1, N):
    buffer_element = abs(x -list[i])
    if buffer_element < min_element:
        min_element = buffer_element
        index_element = i
print(f"Самый близкий по величине элемент к заданному числу {list[index_element]}")

   