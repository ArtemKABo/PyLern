#Задание 8.2
n = int(input("Введите размер массива : "))
m = list( map(int, input("Введите значения массива через пробел : ").split()))

if(n != len(m)):
    print("Размер массива не совпадает с указанным размером")
else:
    res = []
    for i in range(n):
        res.append(m[i-1])
    print("массив сдвинут:")
    print(*res)

