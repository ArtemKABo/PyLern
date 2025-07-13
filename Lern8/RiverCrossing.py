#задача 8.3
m = int(input("Введите грузоподемность лодок : "))
n = int(input("Сколько рыбаков : "))
Ais = []
for ai in range(n):
    Ais.append(int(input(f"Введите вес {ai} рыбака : ")))

Ais.sort()

res = 0

while(len(Ais) > 0):
    res += 1
    if(len(Ais)==1):
        Ais.pop()
    elif((Ais[-1]+Ais[0]<= m)):
        Ais.pop()
        Ais.pop(0)
    else:
        Ais.pop()

print(res)

    