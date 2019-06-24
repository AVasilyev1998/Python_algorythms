def arithmetic(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return ArithmeticError
    else:
        return  "Неизвестная операция"


# TEST1
if arithmetic(1, 2, '+') == 3:
    print("TEST1 OK")
else:
    print("TEST1 ERROR")

# TEST2
if arithmetic(2, 4, '-') == -2:
    print("TEST2 OK")
else:
    print("TEST2 ERROR")

# TEST3
if arithmetic(2, 4, '*') == 8:
    print("TEST3 OK")
else:
    print("TEST3 ERROR")

# TEST4
if arithmetic(4, 2, '/') == 2:
    print("TEST4 OK")
else:
    print("TEST4 ERROR")

# TEST5
if arithmetic(4, 0, '/') == ArithmeticError:
    print("TEST5 OK")
else:
    print("TEST5 ERROR")

# TEST6
if arithmetic(4, 2, '^') == "Неизвестная операция":
    print("TEST6 OK")
else:
    print("TEST6 ERROR")

