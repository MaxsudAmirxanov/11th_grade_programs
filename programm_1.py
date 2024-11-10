figure = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


number = 0

for i in figure:
    figure[number] = int(input(f'введите значение для  {number} значения:'))
    number += 1

#Проверка на самое большое число


new_number = 0 
count = 0
for i in figure:
    count = 0

    for b in figure:

        if  figure[new_number] >= b:
            count += 1
            if count == len(figure):
                print(f'Максимальное число {figure[new_number]}')
                break
            
    new_number += 1
    
    

print(figure)