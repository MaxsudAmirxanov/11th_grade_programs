
n=int(input()) #24
k=int(input()) #3

s = [] #[1, 2, 3, 4, 6, 8, 12]
b = [] #[0, 0, 0]
c = []
d=[]

for i in range(1,n+1):
    if n%i==0:
        s.append(i)
for i in range(k):
    b.append(0)

def multiplication(n):
    s=1
    for i in range(len(n)):
        s*=int(n[i])
    return s

def number_system(n, k):
    'Переход из десятичного в любое'
    s = []
    if n<k:
        return [n]
    while n>k:
        s.append(n%k)
        n=n//k
        if n<k:
            s.append(n)
    s.reverse()
    return s


i=1
while True:

    d.append(number_system(i,len(s)+1))
    if multiplication(number_system(i,len(s)+1))==len(s)**k:
        break
    i+=1
# print('Всу возможные комбинации ------------------')
# print(d)
for i in d:
    multi = 1
    for x,v in enumerate(i):
        if len(i)<k:
            continue
        i[x] = s[v-1]
        multi = multi*s[v-1]
    if multi == n:
        if i not in c:
            c.append(i)
    multi=1
# print('То что нам нужно --------------')
print(c)
print(len(c))

# print(number_system(54,16))

