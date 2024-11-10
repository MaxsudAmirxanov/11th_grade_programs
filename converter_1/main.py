

class MainNumber():
    def __init__(self):
        # self.number_main = number_main
        self.array_alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    def create_str(self, array_number):
        return_array = []
        for i in array_number:
            b = self.array_alphabet[i]
            return_array.append(b)
        return return_array
    
    def with_str_in_index(self):
        array = []
        main_number = list(self.main_number)
        for index, i in enumerate(main_number):
            print(self.array_alphabet)
            array.append[index] = self.array_alphabet.fined(i)
        return array



class NumberSystem( MainNumber):
    def __init__(self, with_NS, main_number,in_NS) -> None:
        self.main_number = main_number
        self.with_NS = with_NS #NS - Number System
        self.in_NS = in_NS
        
        if self.check() == False:
            print('Неправильно введенное число')
            exit()
    
    def check(self):
        # main_number = self.main_number
        main_number = self.with_str_in_index()
        for i in list(main_number):
            if i >= self.with_NS:
                return False
            else:
                return True




class Decimal(NumberSystem):
    "Десятиричная"

    def with_decimal_in(self):
        
        n = []
        result_2 = 0


        while True:
            result = int(self.main_number) % self.in_NS
            self.main_number = int(self.main_number) // self.in_NS
            result_2 = int(self.main_number) // self.in_NS
            n.append(result)
            if result_2 == 0:
                n.append(self.main_number)
                break
     
        return list(reversed(n))
    
class Ninefold(Decimal):
    'Девятеричная'

    def with_ninefold_in_decimal(self):
        '9 --> 10'
        
        main_number = ''.join(reversed(self.main_number))
        # print(enumerate(main_number))
        result = 0
        for index, number in enumerate(list(main_number)):
            # print(f'index - {index}')
            # print(f'number - {number}')
            result += int(number)*(self.with_NS**int(index))
        
        return result
    

main_number = input('Введите число: ')
with_NS = int(input('С какой СС: '))

in_NS = int(input('В какой СС: '))
User_1 = Decimal(with_NS, main_number,in_NS)

if with_NS == 10:
    User_1 = Decimal(with_NS, main_number,in_NS)
    result = User_1.with_decimal_in()
    print(result)

if with_NS == 9:
    # User_2 = Ninefold(with_NS, main_number,in_NS)
    result = User_1.with_ninefold_in_decimal()
    # User_1 = Decimal(with_NS, main_number=result, in_NS=in_NS)
    # User_2.
    print(User_1.with_decimal_in())


