#задание 16.1
import random

def giveManey():
    return int(input("Введите сколько денег хотите получить :"))

class Kassa(object):
    __amount = 0

    # top_up(X) - пополнить на X
    def top_up(self, X):
        self.__amount += X
        print(f"{X} денег кассой получено")

    # count_1000() - выводит сколько целых тысяч осталось в кассе
    def count_1000(self):
        print(f"В кассе { self.__amount//1000} тысяч денег")
        return

    # take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
    def take_away(self, X):
        if(X > self.__amount):
            print("В Кассе нат требуемой суммы")
        else:
            self.__amount -= X
            print(f"{X} денег из кассы выданно")

kassa = Kassa()

for i in range(50):
    kassa.top_up(random.randint(1,5000))

kassa.count_1000()

kassa.take_away(giveManey())

kassa.take_away(giveManey())

kassa.count_1000()