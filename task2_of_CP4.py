n, m = map(int, input("Введите размеры первого и второго массивов: ").split())
ans = []
a = [int(i) for i in input("Введите значения первого массива: ").split()]
b = [int(i) for i in input("Введите значения второго массива: ").split()]
for i in a:
    if i in b and i not in ans:
        ans.append(i)
print("Общие элементы этих двух массивов: ", ans)