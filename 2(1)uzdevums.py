import math 
 
f = float(input('Количество футболок: '))
v = input('Выбор принта(TEKSTS, ZIME, FOTO) ')

def fut():
    global f
    f = math.ceil(f)

fut()
# Цены
if v == 'TEKSTS':
    v = 5 

elif v == 'ZIME':
    v = 7

elif v == 'FOTO':
    v = 20 

else: 
    print('Неверный аргумент. Проверьте правописание и заглавные буквы. Все буквы должны быть заглавными.')
# Скидки
f1 = f * v

if f1 < 50:
    f2 = f1 + 15
    print('Заказ с доставкой стоит ' + str(f2) + 'EUR')

elif f1 >= 100:
    f3 = f1 - (f1 * 5 / 100) 
    print('Заказ со скидкой стоит' + str(f3) + 'EUR')

elif f1 >= 50:
    print('Заказ с бесплатной доставкой стоит: ' + str(f1) + ' EUR')