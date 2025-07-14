#Задача 11.2
from collections import deque as deque

pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}

def create():
    last = deque(pets, maxlen=1)[0]
    pets[last+1] = InputPet()
    print("Данные добавлены")

def read():
    ix = petIntInput()
    if notIndex(ix):
        return
    pet = pets[ix]
    keys = []
    for key in pet.keys():
        keys.append(key)

    feat = pet[keys[0]]

    print(f"Это {feat["Вид питомца"]} по кличке {keys[0]}. Возраст питомца: {feat["Возраст питомца"]} {get_suffix(feat["Возраст питомца"])}. Имя владельца: {feat["Имя владельца"]}")


def update():
    ix = petIntInput()
    if notIndex(ix):
        return
    pets[ix] = InputPet()
    print("Данные обнавлены")

def delete():
    ix = petIntInput()
    if notIndex(ix):
        return
    pets.pop(ix)
    print("Данные удалены")

def InputPet():
    name = input("Введите имя питомца :")
    petTyp = input("Вид вашего питомца? :")
    petAge = int(input("Сколько лет вашему питомцу : "))
    owner = input("Ваше имя :")
    return { name : { "Вид питомца": petTyp , "Возраст питомца": petAge, "Имя владельца": owner}}


def get_pet(ID):
    if notIndex(ID):
        return False
    return pets[ID]

def pets_list():
    print("Список питомцев")
    for key in pets.keys():
        pet = get_pet(key)
        print(f"\t {key}", pet)

def get_suffix(age):
    year = "лет"
    if( age<5 or age >20):
        a =  age%10
        if(a== 1):
            year = "год"
        elif(a>1 and a<5):
            year = "года"
    return year

def notIndex(ix):
    if ix not in pets.keys():
        print("Индекс отсутствует")
        return True
    return False

def petIntInput():
    return int(input("Введите номер животного :"))

stopTok = True

print("Программа поддерживает следующии команды:\n", 
      "\t q quit exit stop:  Эти комманды останавливают выполнение программы \n",
      "\t create : создает нового питомца \n",
      "\t read : читает из базы данные питомца \n",
      "\t update : изменяет данные питомца \n",
      "\t delete : удаляет данные питомца \n",
      "\t get_pet : получает данные ввиде спмска \n",
      "\t pets_list : возвращает список всех питомцев ",)

while(stopTok):
    command = input("Введите комманду: ")
    if(command == "q" or command == "quit" or command == "exit" or command == "stop"):
        stopTok = False
        continue
    elif(command == "create"):
        create()
    elif(command == "read"):
        read()
    elif(command == "update"):
        update()
    elif(command == "delete"):
        delete()
    elif(command == "get_pet"):
         print(get_pet(petIntInput()))
    elif(command == "pets_list"):
       pets_list()
    else:
        print("Неверная команда")
