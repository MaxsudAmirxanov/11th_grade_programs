import time 

start = time.time() 
def range_float(start, stop, step, comma_zero):
    comma_zero_new = 10**comma_zero
    array = []

    number_start = start*comma_zero_new
    number_stop = stop*comma_zero_new
    number_step = step*comma_zero_new
    while True:
        array.append(number_start)
        if number_stop <= number_start:
            break
        number_start+=number_step#**(1/comma_zero)

    result = map(lambda x: x/comma_zero_new, array)
    print(list(result))
    return array
    



range_float(1.5,6,0.34,3)

end = time.time() - start ## собственно время работы программы

# print(end) ## вывод времени

# range_float(1,5,1,3)