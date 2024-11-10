money_rub = int(input('Введите количество рублей: '))
money_dol = int(input('Введите количество долларов: '))
curce = int(input("Введите курс доллара --> рубль: "))



def variant_2():
    if money_dol*curce == money_rub:
        print("все четко")
    elif money_dol*curce > money_rub:
        print(f"нужно перевести {((money_dol*curce - money_rub)/2)/curce} долларов в рублей" )
    elif money_dol*curce < money_rub:
        print(f"нужно перевести {((money_rub - money_dol*curce )/2)} рублей в доллраы" )
        
 
variant_2()