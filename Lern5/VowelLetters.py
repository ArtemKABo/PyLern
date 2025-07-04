# Задание 5_2
#Определяем Гласную
a='a'
e='e'
i='i'
o='o'
u='u'

#Получаем слово
word = input("Enter the word : ")

#Создаем счетчики
ConsonantL = 0
VowelL = 0
aC =0
eC=0
iC=0
oC =0
uC=0


#перебираем буквы
for w in word:
    if w==a:
        aC+=1
        VowelL+=1
    elif(w==e):
        eC+=1
        VowelL+=1
    elif(w==i):
        iC+=1
        VowelL+=1
    elif(w==o):
        oC+=1
        VowelL+=1
    elif(w==u):
        uC+=1
        VowelL+=1
    else:
        ConsonantL +=1

print(f"There are {ConsonantL} consonant letters in your word")
print(f"There are {VowelL} vowel letters in your word")
print("The number of occurrences of vowels in your word:")
if aC>0:
    print("a :", aC )
else:
    print("a : False")
if eC>0:
    print("e :", eC )
else:
    print("e : False")
if iC>0:
    print("i :", iC )
else:
    print("i : False")
if oC>0:
    print("o :", oC )
else:
    print("o : False")
if uC>0:
    print("u :", uC )
else:
    print("u : False")


