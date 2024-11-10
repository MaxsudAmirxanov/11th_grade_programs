
n=int(input()) #24
k=int(input()) #3

s = [] #[1, 2, 3, 4, 6, 8, 12, 24]
c = []


for i in range(1,n+1):
    if n%i==0:
        s.append(i)


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

    w = number_system(i,len(s)+1)
    print(w)
    q = 1
    v=1
    if len(w)<k:
        i+=1
        continue
    for x, el in enumerate(w):
        v*=el
        q *= s[el-1]
        w[x] = s[el-1]
    if q == n:
        if w not in c:
            c.append(w)
    if v == len(s)**k:
        break
    v=1
    q=1
    i+=1

print(c)
print(len(c))
print(s)

# print(number_system(54,16))

