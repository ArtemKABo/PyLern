x = float(input("Введите минимальную сумму инвестирования : "))
A = float(input("Введите сколько средств есть у Майкла : "))
B = float(input("Введите сколько средств есть у Ивана : "))

if (A>=x and B>=x):
    print("2")
elif(A>=x and B<x):
    print("Mike")
elif( A<x and B>=x):
    print("Ivan")
elif( A<x and B<x and A+B>=x):
    print("1")
else:
    print("0")

