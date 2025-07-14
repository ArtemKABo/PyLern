#задача 11.1

def factorial(n):
    res = 1
    if(n==0):
        return res

    for i in range(1,n+1):
        res *= i
    return res

fs = list()
for i in range(6,0,-1):
    fs.append(factorial(i))

print(fs)