# import math
# a = [2,12,5,3,22,5,7,12,8,3]
# b = []
# c = []
# for i in a:
    
#     if i % 2 == 0:
#         b.append(i)
#     else:
#         c.append(i)

# print(sum(b))
    
# print(math.prod(c))


s = 0
n = 2

for i in range(1,11):
    s += i
    n+=1

print(s)



a = 10

a = 5   #Теперь у нас переменная "а" равно 5
a += 2   #Теперь у нас переменная "а" котоая равняется 10 прибавляем 2. То есть 10 + 2 = 12
a -= 3   #Теперь у нас переменная "а" котоая равняется 10 отнимаем 3. То есть 10 - 3 = 7

a += 2   #Это равноправно a=a+2
a -= 3   #Это равноправно a=a-3