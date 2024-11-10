a = [3,2,2,4,4,7,6,1]
print(1)
print(a)
    #1) Найти индекс
    #2) Сравнить если чило ране той хуйне 
    # Индекс == числу

for i in a:
    index = a.index(i)

    if index == i:
        print('Ахуеть')
        print(i)


q = enumerate(a)
for i,s in enumerate(a):

    if s == i:
        print('Ахуеть')
        print(i)

z=0
for i in a:
    
    if z == i:
        print('Ахуеть')
        print(i)
    z=z+1