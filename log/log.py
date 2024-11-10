from sympy.solvers import solve
from sympy import Symbol


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
    # print(list(result))
    return array

def log(number_1, number_2):
    # y = 0
    # x = 0
    # number_2**(1/x) - number_1

    x = Symbol('x')

    r = solve(number_2**(1/x) - number_1, x)
    print(r)
    # return number_2**(1/number_1)


    return r[0]

log(2,9)
# print(log(2,16) )



# print(len(number))

# if str(6.0*2) == str(12.0):
#     print(123)

#-------------------------------------------------------------------------------------------------------------------
# import decimal
# decimal.getcontext().prec = 100
# number_1 = 2
# number_2 = 8
# number = 1
# # print(number_2)
# loop = True
# while loop:
#     print(f'Поток с делителем {number}')
#     for x in range_float(1, number_2, number, len(str(number))):
#         if decimal.Decimal(number_1)**decimal.Decimal(x) == float(number_2):
#             # print(x)
#             break
#     else:
#         number/=10