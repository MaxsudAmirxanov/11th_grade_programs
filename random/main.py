import math
import datetime
import time
def with_decimal_in(main_number, in_NS ):
    
    n = []
    result_2 = 0


    while True:
        result = int(main_number) % in_NS
        main_number = int(main_number) // in_NS
        result_2 = int(main_number) // in_NS
        n.append(result)
        if result_2 == 0:
            n.append(main_number)
            break
    
    return list(reversed(n))

def with_2_for_10(number):
    result = 0
    index = 0
    for i in reversed(str(number)):
        result+=int(i)*(2**index)
        index+=1

    return result

def with_10_for_2_2(number):
    result = []

    while int(number)>=1:
        a_2 = number %2
        number = number /2
        print(number)
        result.append(int(a_2))

    print(result)

def with_10_for_2(number):
    result = []
    count = 0
    
    end = int(math.log2(number))
    while end>=0:
        print(result)
        if int(math.log2(number)) == end-count:
            result.append(1)
            number= number-2**end
            print(number)
        else:
            result.append(0)
        count+=1
        end-=1
    print(result)
        # if 2**number_2 > number:
        #     result.append(number_2-1)
        #     number=number-(2**number_2)
        #     number_2=0
        # else:
        #     number_2+=1
        
        

def random_1(start, stop):
    min_n = len(with_decimal_in(start,2))
    max_n = len(with_decimal_in(stop,2))
    a = []
    b = []
    
    while True:
        now = datetime.datetime.now()
        # print(now)
        
        main_random = list(str(now))[25]

        if int(main_random) == 0 or int(main_random) == 1:
            #print('rts')
            #print(main_random)
            time.sleep(0.000047345)

            a.append(main_random)
            # print(a)
            if len(a) >= max_n:
                #print(123)
                result = ''.join(a)
                #print(result)
                a.clear()
                result_10 = with_2_for_10(result)
                #print(result_10)
                #print(12345)
                # print(a)
                if start <= result_10 <= stop:
                    return result_10
                    # b.append(result_10)
                    # if len(b) == 1000:
                    #     return b
        
def chek(number):
    pass    
# with_10_for_2_2(168)
while True:
    start = int(input('Старт: '))
    stop = int(input('Стоп: '))
    # b = []
    # for i in range(100):

    result = random_1(start,stop)
    print(result)
# result.sort()
# print(result)
# n = 0
# for i in range(0, 21):
#     count = result.count(n)
#     print(f'{n} -- {count}')
#     n+=1
# b.append(result)
# b.sort
# print(b)
# print(now)


# print(with_2_for_10(start))

import random

random_number = random.randint(1,10)
#Переменная random_number получает рандмоное значение от 1 до 10