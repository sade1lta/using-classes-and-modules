def calculator():
    my_calc = input('my_calc: ')
    while my_calc != '':
        [a, b, c] = my_calc.split()
        a = float(a)
        c = float(c)
        if b == '+':
            print(a + c)
        elif b == '-':
            print(a - c)
        else:
            print(a * c)
        my_calc = input('my_calc: ')

calculator()