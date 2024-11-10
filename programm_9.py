# import time
# import datetime

# for i in range(100000):

#     start_time = datetime.datetime.now()
#     start = time.time()
#     b = [267,568,2489,6926]
#     i = 0
#     while len(b) < i:
#         token = []
#         result = 0
#         a = 0

#         for i in b:

#             if a == len(token)-1:
#                 print('й')
#                 result = result + int(str(i)[0])**2
#             elif a == 0:
#                 print('ц')
#                 result = result + int(str(i)[0])**2
#             print(result)
#             print(token)
#     end = time.time() 
#     end_time = datetime.datetime.now()

# print(end - start)
# print(end_time-start_time)

# n=int(input())

# k=int(input())
# s=0
# def f(n,k):
    
#     global s
#     if k == 0:
#         return 1
#     for i in range(n+1):
#         # print(i)
#         v = f(n, k-1)
        
#         if i*v == n:
#             # print(2345)
#             print(i)
#             print(v)
#             s+=1
#     return 1
# f(n,k) 
# print(s)     

n=int(input())
k=int(input())

s = []
b = 0
for i in range(1,n):
    if n%i==0:
        s.append(i)

print(s)

# def c(k):
#     global n,b
#     if k == 0:
#         return 1
#     for i in s:
#         if i * c(k-1) == n:
#             b+=1
#             # return i * c(k-1)
#     return 1
    
# print(b)
a = 1
v=k
c = []
def c_2():
    global s,c,a,k
    if k == 0:
        k==v
        return 1
    for i, u in enumerate(s):
        print(i,u)
        a*=u
        k-=1
        if a == n:
            a == 1
            print(123)
        c_2()
# c_2()