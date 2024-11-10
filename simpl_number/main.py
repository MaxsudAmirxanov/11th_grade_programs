
def ciunt_simpl_number(numbers):
    a = []

    count = 0
    for number in numbers:
        for i in range(1,int(number)+1):
            if int(number) % i == 0:
                count += 1
        if count == 2:
            a.append(int(number))
        count=0
    return a





numbers = []

while True:
    number = input('Введите число: ')
    print('Для стопа нажмите "s"')
    if number == 's':
        break
    numbers.append(number)


print(numbers)
result = ciunt_simpl_number(numbers=numbers)
print(result)



# list=[4,7,17,18,21,47,51,99,107]
# count=0
# abc=0
# for i in list:
#     number=range(1, i+1)
#     for k in number:
#         if i%k==0:
#             abc+=1
#     if abc==2:
#         count+=1
#     abc=0


# print(count)