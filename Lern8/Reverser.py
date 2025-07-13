# задание 8.1
n = int(input("Введите длинну массива от 0 до 100000 :"))
ar =[]
for i in range(n):
    ar.append(int(input(f"введите {i} элемент массива : ")))
print("Ваш массив")
print(*ar)
print("Обратный массив")
ar.reverse()
print(*ar)