a, b = map(int, input("Введите размеры первого и второго массивов: ").split())
com_elements = []
n = [int(i) for i in input("Введите значения первого массива: ").split()]
m = [int(i) for i in input("Введите значения второго массива: ").split()]
for i in n:
    if i in m and i not in com_elements:
        com_elements.append(i)
print("Общие элементы этих двух массивов: ", com_elements)