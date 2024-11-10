def nod(numbers):
    numbers_divider = {}
    for index, i in enumerate(numbers):
        array = []
        i = int(i)

        number = 1
        while True:
            divider = i/number 
            if divider//1 == divider:
                array.append(divider)

            number+=1
            if number > i:
                break

        numbers_divider[i] = array

    print(numbers_divider)

    #Нахождение наибольшего числа из общих делителей ---------------------------------------
    main_array = []
    array = numbers_divider.values()
    # big_array = ''.join(array)
    for i in numbers_divider.values():
        # array.append(i)
        
        for b in i:
            index = 0
            while True:
                # print('-- ', list(array)[0])
                print(list(array)[index])
                if b in list(array)[index]:
                    index +=1 
                    if index == len(array):
                        main_array.append(b)
                        break
                else: 
                    break

        common = []
    print(array)
    # print(big_array)
    print(max(main_array))

def nok(numbers):
    list_1 = []
    list_2 = []

    for i in range(1, number_1+1):
        list_1.append(number_1*i)

    for i in range(1, number_2+1):
        list_2.append(number_2*i)
    
    array = []
    for i in list_1+list_2:
        if i in list_1 and i in list_2 and i not in array:
            array.append(i)

    print(array)
    print(min(array))
    
# nod(30, 24)
# nok(9, 12)



choice = int(input("""
    Что хотите посчитать (Введите число)
    1) НОК
    2) НОД
    """))

count = 1
numbers = []
print('Введите "s" для стопа')
while True:

    number = input(f"Ведите число {count}) ")
    count+=1
    if number.lower() == 's':
        print(f"Ваши числа {numbers}")
        break
    numbers.append(number)

if choice == 1:
    nok(numbers)

if choice == 2:
    nod(numbers)