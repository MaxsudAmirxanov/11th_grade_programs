a = [0,1,2,3, 4, 5, 6, 7, 8, 9]
import random
import datetime

# now = datetime.datetime.now()
import random

#1 - камень
#2 - ножницы
#3 - бумага

def rps(number):
    if number > 3:
        print("Нет такого варианта ответа :(")
        return 
    r_int = random.randint(1,3)
    if number != r_int:
        if number == 1 and r_int == 3:
            return False
        elif number == 2 and r_int == 1:
            return False
        elif number == 3 and r_int == 2:
            return False
        else:
            return True
    else:
        return None
    
user = 0
bot = 0
while True:
    print("Добро пожаловать в игру камень ноницы бумага, введите ваш ответ:  ")
    number = input('''
    1 - камень
    2 - ножницы
    3 - бумага

    ''')
    if number == 's':
        print("Выход из программы")
        break

    result = rps(int(number))
    if result == True:
        print('Вы выйграли !!!')
        user+=1

    elif result == False:
        print('Вы проиграли :(')
        bot+=1
    else:
        print('Ничья')

    if user == 3 and bot<3:
        print(f'Вы выиграли со счетом {user} \ {bot} !!!')
        user = 0
        bot = 0
    elif user < 3 and bot == 3:
        print(f'Вы проиграли со счетом {user} \ {bot} :(')
        user = 0
        bot = 0

    







    
def random_1(start, stop):
    while True:
        now = datetime.datetime.now()
        # print(list(str(now)))
        # print(list(str(now))[25])
        
        # print(len(list(str(now))))

        a = []
        main_random = list(str(now))[25]
        for i in range(start, stop+1):

            if main_random:
                print(main_random)


                a.append(main_random)


    # a = sum(list(range(start, stop+1)))/ len(list(range(start, stop+1)))
    # print(a)
    # print(list(range(start, stop+1)))
    # a

# random_1(1,10)
# print(now)




import random

random_number = random.randint(1,10)
#Переменная random_number получает рандмоное значение от 1 до 10
