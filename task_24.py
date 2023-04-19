import random
n = int(input("Введите число  больше 3: "))
list_1 = list()
for i in range(n):
    # m = int(input())
    m = random.randint(1, 10)
    list_1.append(m)
print(*list_1)
x = 0

for i in range (0, n - 1):
    if (list_1[i] + list_1[i+1] + list_1[i-1] > x):
      x = list_1[i] + list_1[i+1] + list_1[i-1]
print(x)