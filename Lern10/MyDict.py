#задача 10.2
my_dict = dict()

for i in range(10, -6, -1):
    my_dict[i] = i**i

for key, value in my_dict.items():
    print(f"{key}:{value}")


