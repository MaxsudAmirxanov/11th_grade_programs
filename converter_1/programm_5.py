#Калькулятор СС

import requests
import math

class Number_10:
    def __init__(self, main_number, turn_number) -> None:
        self.main_number = main_number
        self.turn_number = turn_number


    def hexadecimal(self):
        'Шеснатиричная'
        n = []
        result_2 = 0

        while True:
            result = self.main_number % self.turn_number
            self.main_number = self.main_number // self.turn_number
            result_2 = self.main_number // self.turn_number
            n.append(result)
            if result_2 == 0:
                n.append(self.main_number)
                break
     
        return list(reversed(n))
     
    

    def octal(self):
        "Восмиричная"

    def binary(self):
        "Двоичная"
        binary_number = self.main_number
        # print(list(str(binary_number)))
        number = self.hexadecimal()

        
        log = math.log(self.turn_number,2)
        print(f"Степень числа {log}")
        # print(number)
        # print(''.split(binary_number, maxsplit=int(log)))
        count = 0
        new_array = []

        a = list(str(binary_number))
        a.reverse()

        for i in a:
            new_array.append(i)
            count+=1
            if count == int(log):
                new_array.append(',')
                count=0


        print(new_array)
        return_str = []
        b = []
        for i in new_array:
            
            if i != ',':
                b.append(i)
            else:
                return_str.append(''.join(b))
                b.clear()
        print(return_str)

class Interfece:
    def __init__(self, number_main):
        self.number_main = number_main
        self.array_alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def create_str(self, array_number):
        return_array = []
        for i in array_number:
            b = self.array_alphabet[i]
            return_array.append(b)
        return return_array
    
        
        
        
main_number = int(input('Введите число которое хотите конвертирвать из 10 системы счесления: \n'))
turn_number = int(input("В какую СС хотите конвертировать ? \n"))


User = Number_10(main_number, turn_number)
console = Interfece(User)
User.binary()
i = User.hexadecimal()
b = console.create_str(i)

# print(i)
# print(b)


