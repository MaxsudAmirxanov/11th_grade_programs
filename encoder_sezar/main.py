# Напишите программу которая принимает словои шаг алгоритма, и вывод это слово в звшифрованном виде. 
# Слово должно быть зашифрованным алгоритмом цезаря

a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
a = list(a)
word = input("Введите слово: ")
step = int(input("Введите шаг алгоритма: "))
new_word = ''

for i in word:
    # print(a)
    index = a.index(i)
    new_word += a[index+step]

print(new_word)

