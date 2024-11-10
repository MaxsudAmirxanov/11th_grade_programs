import random

class CrossZero():
    def __init__(self) -> None:
        # self.answer = answer

        self.fealds = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    
    def cheak_answer(self, whom, answer):

        if self.fealds[answer] != ' ' :
            return False
        else:
            return True
        # count=1
        # for i in self.fealds:
        #     if i[count] == whom:
        #         return False
        # else:
        #     return True

    def replacement(self, whom, answer):
        # print(1234)
        # print(self.fealds)
        if whom == 'U':
            self.fealds[answer] = 'X'
        elif whom == 'B':
            self.fealds[answer] = 'O'
        print(self.fealds)

    def check_win(self):
        if self.fealds[1] == self.fealds[2] == self.fealds[3] != ' ':
            return self.fealds[1], True
        elif self.fealds[4] == self.fealds[5] == self.fealds[6] != ' ':
            return self.fealds[4], True
        elif self.fealds[7] == self.fealds[8] == self.fealds[9] != ' ':
            return self.fealds[7], True
        
        elif self.fealds[1] == self.fealds[5] == self.fealds[9] != ' ':
            return self.fealds[1], True  
        elif self.fealds[3] == self.fealds[5] == self.fealds[7] != ' ':
            return self.fealds[1], True  

        elif self.fealds[1] == self.fealds[4] == self.fealds[7] != ' ':
            return self.fealds[4], True
        elif self.fealds[2] == self.fealds[5] == self.fealds[8] != ' ':
            return self.fealds[2], True
        elif self.fealds[3] == self.fealds[6] == self.fealds[9] != ' ':
            return self.fealds[3], True
        else:
            return 1, False
        
class Bot(CrossZero):
    def bot_answer(self):
        r = random.randint(1,9)
        return r

    def input_information(self, choice, whom):
        if self.cheak_answer(whom, answer=choice) == True and whom=='U':
            user.replacement('U', answer=choice)
        elif self.cheak_answer(whom, answer=choice) == True and whom=='B':
            user.replacement('B', answer=choice)
        else:
            print('Такое поле занято')
            return False



class Interface(CrossZero):
    def field_output(self):
        dict = self.fealds

        print(f'''
         {dict[1]} | {dict[2]} | {dict[3]}
        ---|---|---
         {dict[4]} | {dict[5]} | {dict[6]}
        ---|---|---
         {dict[7]} | {dict[8]} | {dict[9]}
        ''')
    def input_information(self, choice, whom):
        if self.cheak_answer(whom, answer=choice) == True and whom=='U':
            user.replacement('U', answer=choice)
        elif self.cheak_answer(whom, answer=choice) == True and whom=='B':
            user.replacement('U', answer=choice)
        else:
            print('Такое поле занято')
            return 1, False



user = Interface()
while True:
    
    print(user.field_output())
    answer = int(input())
    user.input_information(answer, 'U')

    result = user.check_win() 
    # print(result)
    # print(12345)
    if result[1] == True:
        print(user.field_output())
        print(f"Выиграла {result[0]} !!!")

        break
        
    bot = Bot()
    r = bot.bot_answer()
    while True:
        if  bot.input_information(r, 'B') != False:
            break



    
        