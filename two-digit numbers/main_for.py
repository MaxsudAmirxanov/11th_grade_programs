# for

number = 0

def f():
    all_numbers = []
    for i in range(10,100, 2):
        all_numbers.append(i)
        
    return sum(all_numbers)
result = f()
print(result)

