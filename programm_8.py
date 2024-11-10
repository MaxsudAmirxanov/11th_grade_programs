# s = int(input())
# b = 1
# for i in range(1,s+1):
#     b = b*i
#     print(b)
# print(b)

# for x in range(3, 6):
#     print(x)
#     y = 1/(x**2-4)
#     print(y)
    


# min = 3
# max = 5
# x = min

# while x<=max:
#     y = 1/(x**2-4)
#     print(y)
#     x+=0.5


# def treugolnik(x,y,z):
#     if not(abs(y-z)>x and x<y+z):
#         return True
#     else:
#         return False
    
def treugolnik(a,b,c):
    if abs(b-c) < a < b+c:
        return True
    else:
        return False

def function_1(number): 
    #Переобразуем нецелое число в целое, умножив его на десять (2.6 --> 26)
    number = number*10

   

    for i in range(0,15):
        if i == number:
            print('ужасно - ⭐️')

    for i in range(15, 25):
        if i == number:
            print('плохо - ⭐️⭐️')

    for i in range(25,35):
        if i == number:
            print('нормально - ⭐️⭐️⭐️')

    for i in range(35, 45):
        if i == number:
            print('хорошо - ⭐️⭐️⭐️⭐️')

    for i in range(45, 51):
        if i == number:
            print('отлично - ⭐️⭐️⭐️⭐️⭐️')


list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 





# function_1(float(input()))
# print(function_1(float(input('ваша оценка: '))))



# m = '1223425'

# print(m.find('2', 0, 3))
# print(m.count('2'))

# import math
# print(math.sqrt())

# import random
# import inspect

# print(inspect.getsource(math.sqrt)) 
# #Линейная функция
# def linear_fun(k, x, b): ...

    

# result = linear_fun(2,3,4)
# print(result)



# def say_hi(a):
#     result = f'привет {a}'
#     return result
    

# result = say_hi('Ильхам')
# # print(result)


# a = ['123','345', '567']
# b = '123'
# print(a[1][1])
# del a[1][1]


# print(a)


def f(x):
    if x>0:
        return True, x
    else:
        x = -x
        return False, x

# x = int(input())
# results = f(x) 

# if results[0] == True:
#     print('Число положително')
# else:
#     print('Введенное число отрицательно')
#     print(f'И его модуль {results[1]}')



list = ['огурец', 'помидор', 'салат', 'сыр']

tomat = list[1]
print(tomat)