#задание 9.3
m = list(map(int , input("enter list : ").split()))
s = set()
res = ""
for n in m:
    if n in s:
        res += " YES"
    else: res += " NO"
    s.add(n)

print("new numbers:", res)