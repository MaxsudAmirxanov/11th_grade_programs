#while

number = 10
all_numbers = []

def f():
    number = 10
    all_numbers = []
    while number<100:
        if number%2==0:
            all_numbers.append(number)
        number+=1

    return sum(all_numbers)

result = f()
print(result)