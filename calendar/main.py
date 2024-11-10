list = [[1], [2], [3], [4], [5], [6], [7]]

def add(money, day):

    count = 0
    for i in list:
        if i[0] == day:
            i.append(money)
            break
        count+=1

def return_day():
    result= ''
    all_money = 0
    for i in list:
        result+=f'День {i[0]} -- Сумарные траты на {sum(i) - i[0]}\n'
        all_money+=sum(i) - i[0]
    result+=f'Траты за всю неделю -- {all_money}'
    return result

day = 1
while day<8:
    print(f'Введите сумму для {day}-ого дня: ')
    print('Введите "n" для переходя на следующий день')
    
    while True:
        # day = int(input("Введите день: "))
        money = input('Траты: ')
        if money == 'n':
            day+=1
            break

        add(int(money), day)
        # print(list)
print(return_day())


