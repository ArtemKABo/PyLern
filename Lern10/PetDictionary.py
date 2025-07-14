#Задача 10.1
stopTok = True

pets = dict()

print("The program supports the following commands:\n", 
      "\t q quit exit: Any comnands close program \n",
      "\t create : creates a new entry in the dictionary \n",
      "\t get : gets an animal from the dictionary by the key")

while(stopTok):
    com = input("Enter command: ")
    if(com == "q" or com == "quit" or com == "exit"):
        stopTok = False
        continue
    elif(com == "create"):
        name = input("Enter the name of the animal :")
        if name in pets.keys():
            print("This name already exists.")
            continue
        petTyp = input("What kind of pet does your pet belong to? :")
        petAge = int(input("Enter the age of the pet : "))
        owner = input("Enter your name :")
        pets[name] =  { "Вид питомца": petTyp , "Возраст питомца": petAge, "Имя владельца": owner}
    elif(com == "get"):
        name = input("Enter the name of the animal :")
        if name not in pets.keys():
            print("This name does not exist.")
            continue
        pet = pets[name]
        year = "лет"
        int(pet["Возраст питомца"])
        if( int(pet["Возраст питомца"])<5 or int(pet["Возраст питомца"]) >20):
            a =  int(pet["Возраст питомца"])%10
            if(a== 1):
                year = "год"
            elif(a>1 and a<5):
                year = "года"
        print(f"{pet["Вид питомца"]} по кличке {name}. Возраст питомца: {pet["Возраст питомца"]} {year}. Имя владельца: {pet["Имя владельца"]}")


