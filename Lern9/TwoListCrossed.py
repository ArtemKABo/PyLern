#задача 9.2

l1 = set(map(int, input("Enter the first list of numbers : ").split()))
l2 = set(map(int, input("Enter the second list of numbers : ").split()))
li = l1.intersection(l2)
print(f"{len(li)} digits crossed")