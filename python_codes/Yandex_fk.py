class fk:
    def __init__(self):
        pass
    # Дороги фк=1
    def fk_1(self,z):
        self.z = z
        if 1<z<5:
            color = 'начинают отображаться'
            return color
        elif z<2:
            color = "Зум не может быть меньше 2"
            return color
        elif 5 <= z < 8:
            color = "Фиолетовый"
            return color
        elif 8 <= z < 9:
            color = "Желтый"
            return color
        elif 9 <= z < 12:
            color = 'становятся зелеными'
            return color
        elif 12 <= z < 15:
            color = 'остаются зелеными, но рисуются с жирной обводкой'
            return color
        elif z>=15:
            color = 'остаются зелеными и с жирной обводкой, но становятся полупрозрачными'
            return color
    # Дороги фк=7
    def fk_7(self,z): # - начинают отображаться на z=2 розовыми; - исчезают на z=15.
        if 2<=z<15:
            color = 'Отображаются розовыми'
            return color

    # Дороги фк=9
    def fk_9(self,z): #начинают отображаться на z=12 и рисуются поверх других дорог
        if z >= 12:
            color = 'рисуются поверх других дорог'
            return color


road = fk()
z = 12
result = road.fk_1(z)
result_2 = road.fk_7(z)
result_3 = road.fk_9(z)
if result is not None:
    print(f'Дороги ФК=1 {result}')
if result_2 is not None:
    print(f'Дороги ФК=7 {result_2}')
if result_3 is not None:
    print(f'Дороги ФК=9 {result_3}')
