# a = int(input())
# b = int(input())
# c = int(input())

import requests
import pprint

def programm_1(a, b, c):
    if a+b>c:
        if c+b>a:
            if a+c>b:
                print('Возвозможно !!!')

            else:
                print('Невозможно')
        else:
            print('Невозможно')
    else:
        print('Невозможно')

def program_2(a,b,c):
    if a+b>c and c+b>a and a+c>b:
        print('Возвозможно !!!')

    else:
        print('Невозможно')

def programm_3(a,c):
    if a > c:
        print('a > c')
    elif a == c:
        print('a == c')
    else:
        print('a < c')


url = 'http://svgimnazia1.grodno.by/sinica/Book_ABC/Book_ABC_pascal/sistem_2_10_16/dec2bin2oct2hex.htm'
t = requests.get(url=url)
# # f = open('text.txt', 'w')
# # f.write(str(t.text))
print(t.text)


# from bs4 import BeautifulSoup

# soup = BeautifulSoup(t.text, 'html.parser')
# # print(soup)
# # allNews = soup.findAll('a')
# print(soup )