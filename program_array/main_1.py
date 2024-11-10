a = [352, 7401, 33573733, 905]

#352  --> 10

for i in a:
   #i = '352'
    print(i)
    first_letter = str(i)[0]
    count = len(str(i))
    last_letter = str(i)[count-1]
   
    # sum = (int(str(i)[0]) + int(str(i)[len(str(i))-1]))*2
    print((int(first_letter) + int(last_letter))*2)
    

