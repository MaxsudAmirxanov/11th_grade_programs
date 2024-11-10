# for i in range(0,9):
#     if i%2==0:
#         print(i, 'делиться на 2')
#     elif i%3==0:
#         print(i, 'делиться на 3')

def f_1(n):
    if n ==1:
        return 1
    return f_1(n-1)*n
s=0
n = int(input())
# for i in range(1,n+1):
#     s+=f_1(i)
# print(f_1(n))
print((1+float((1/n)))**n)