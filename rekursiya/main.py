import sys

sys.setrecursionlimit(100000000)
import time


def timemometr(func):
    from time import time
    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения функции {end_time-start_time} сек.')
        return value
    return wrapper

def summa():
    from time import sleep
    sleep(2)
    return 11



def main_1(n):
    list_1 = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i/j not in list_1:
                list_1.append(i/j)

    print(len(list_1))



def main_2(n, list_1=[], numbers=[1,1]):

    # print(numbers)
    # print(n)
    if numbers[0]/numbers[1] not in list_1:
        list_1.append(numbers[0]/numbers[1])
    # if numbers[0]==n and numbers[1]!=n:
    #     numbers[1]+=1
    if numbers[1]==n and numbers[0]<n:
        numbers[1]=0
        numbers[0]+=1

    # if numbers[1] == n:

        # print(numbers)
    # else:
    #     numbers[0]=1
    # if numbers[0] >=n and numbers[1]==n:
    #     return
        
    elif numbers[0]==n and numbers[1]==n:
        print(len(list_1))
        return
    numbers[1]+=1
    # print(numbers)

    main_2(n,list_1,numbers)

    
# d=[4,1]
# d[0]=9
# print(d)
@timemometr
def test():
    main_2(int(input()))

test()
