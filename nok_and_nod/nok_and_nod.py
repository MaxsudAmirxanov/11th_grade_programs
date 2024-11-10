def nod(number_1, number_2):
    #Нахождение общих делителей ------------------------------------------------------------
    list_1 = []
    list_2 = []

    number = 1
    while True:
        divider = number_1/number 
        if divider//1 == divider:
            list_1.append(divider)

        number+=1

        if number > number_1:
            break
    print(list_1)

    number = 1
    while True:
        divider = number_2/number 
        if divider//1 == divider:
            list_2.append(divider)

        number+=1


        if number > number_2:
            break
    print(list_2)


    #Нахождение наибольшего числа из общих делителей ---------------------------------------
    common  = []
    # print(list_1+list_2)
    for i in list_1+list_2:
        if i in list_1 and i in list_2 and i not in common:
            common.append(i)

    print(common)
    print(max(common)) #вот нащ НОД

def nok(number_1, number_2):
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
    
nod(36, 12)
nok(36, 12)
