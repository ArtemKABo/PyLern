#задачи 14
def rPrint(l, pos = 0 ):
    if(pos == len(l)):
        print("Конец списка")
        return
    print(l[pos])
    rPrint(l, pos+1)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

rPrint(my_list);