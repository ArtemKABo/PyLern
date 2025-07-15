#задача 16.2
class turtle(object):
    __x = 0
    __y = 0
    __s = 1
    __m = False #умеет ли черепаха сама управлять своей скоростью

    def __init__(self, x, y, s):
        self.__x = x
        self.__y = y
        self.__s = s

    # go_up() - увеличивает y на s
    def go_up(self):
        self.__y += self.__s

    # go_down() - уменьшает y на s
    def go_down(self):
        self.__y -= self.__s

    # go_left() - уменьшает x на s
    def go_left(self):
        self.__x -= self.__s

    # go_right() - увеличивает y на s
    def go_right(self):
        self.__x += self.__s
        
    # evolve() - увеличивает s на 1
    def evolve(self):
        self.__s += 1

    # degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
    def degrade(self):
        if((self.__s - 1) < 1):
            print("Скорость черепахи не может быть меньше 1")
            return
        self.__s -= 1

    # count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
    def count_moves( x2, y2):






