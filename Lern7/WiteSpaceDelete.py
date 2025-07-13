# задача 7.2
st = input("Введите строку :")
if(len(st) >1000):
    print("Строка слишком большая")
else:
    sts = st.split(' ')
    res =  []
    for w in sts:
        if(len(w)>0):
            res.append(w)

    print (" ".join(res))

