import uuid
b = []
print('test')


# print(f.read())
# for i in f:
#     id_name = uuid.uuid4()
#     if i == id_name:
#         exit()
#     else:

#         f.write(str(id_name))
# while True:
#     f = open('file_name.txt', 'a+')
#     id_name = uuid.uuid4()
#     print(f.readlines())
#     if f'{str(id_name)}\n' in f.readlines():
#         print('Такой id есть')
#         break
#     else:
#         # f = open('file_name.txt', 'a')
#         f.write(f'{str(id_name)}\n')
#         # f.write('/n')
while True:
    id_name = uuid.uuid4()
    with open("file_name.txt", "r+") as file1:
        # итерация по строкам
        # print(list(file1.read()))
        if f'{str(id_name)}' in list(file1.read()):
            print('Такой id есть')
            break
        else:
            # f = open('file_name.txt', 'a')
            file1.write(f'{str(id_name)}\n')
            # f.write('/n')
