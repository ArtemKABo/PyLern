 # задание 6.1
lenx = int(input("Скольло у вас чисел : "))

zeroCount = 0

while lenx > 0:

    x = int(input("Введите целое число: "))
    lenx -= 1 
    if x == 0 :
        zeroCount += 1

print(f" {zeroCount} чисел ровных нолю")


