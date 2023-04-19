# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые 
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во 
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2 
# 3 6 9 12 15 18
# 6 12
import random
n = int(input("Введите число N: "))
list_1 = list()
for i in range(n):
    #x = int(input())
    x = random.randint(1, 20)
    list_1.append(x)
print(*list_1)
m = int(input("Введите число M: "))
list_2 = list()
for i in range(m):
    #y = int(input())
    y = random.randint(1, 20)
    list_2.append(y)
print(*list_2)
list_3 = list(set(list_1) & set(list_2))
list_3.sort()
print(*list_3)
