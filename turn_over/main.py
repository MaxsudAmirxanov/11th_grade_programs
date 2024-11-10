number = int(input())
result = []

len_number = len(str(number))-1

count = -1
while count!=len_number:
    # print(list(str(number)))
    result.append(list(str(number))[int(len_number)])
    print(result)
    # if len_number!=0:

    len_number-=1

print(''.join(result))
