n = int(input("Введите размер массива: "))
array = [float(i) for i in input("Введите сами элементы этого массива: ").split()]
imax = 0
for i in range(1, n):
    if (array[i] >= array[imax]):
        imax = i
for i in range (imax + 1, n):
    array[i] = 0
print(array)