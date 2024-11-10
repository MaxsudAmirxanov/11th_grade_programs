list = ['1234', "12","12345", "1", "1234"]
new_list = []
count = 0
for i in range(100):
    for index, i in enumerate(list):
        len(i)
        if index == len(list):
            if len(list[index+1]) < len(i):
                list.pop(index)
                list.insert(index+1, i)
                break
            count+=1
        else:
            
            list.pop(index)
            list.insert(index+1, i)
                
            count+=1
    
print(list)




# for i in list:
#     cound_1 = len(i)
#     count = 0
#     for b in list:
        
#         cound_2 = len(b)
#         if cound_1 <= cound_2:
#             pass
#         else:
#             # print(list)
            
#             list.insert(count-1, i)
#             list.pop(count)
#             # print(list)
#             # print('-----')
            
#     count+=1
# print(list)


