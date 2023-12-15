def main():
    import math as m
    def findy():
        h = float(input('Enter a second number: '))
        return(h)
    yes = True
    x = float(input('Enter a number: '))
    z = 0
    while yes == True:
        if z >= 1:
            o = str(input('Enter an operator (type "h" for help, type "s" to stop the program): '))
        else:
            o = str(input('Enter an operator (type "h" for help): '))
        if o == 'h':
            print('Here is the key for the operations:')
            print('+ = addition\n- = subtraction\n* or x = multiplication\n/ = division')
            print('% = modulus (find the remainder between two numbers)\n^ = exponent (x to the power of y)\nq = exponent roots(the y root of x)')
            print('sin = sin(sine)\ncos = cos(cosine)\ntan = tan(tangent)\nasin = inverse sin\nacos = inverse cos\natan = inverse tan')
            print('log = logarithm\nAll trig functions are calculated in degrees\nThe key for the natural log is 0')
        elif o == '+':
            y = findy()
            a = x
            x = x + y
            print(f'The sum of {a} and {y} is {x}')
            z += 1
        elif o == '-':
            y = findy()
            a = x
            x = x - y
            print(f'The difference between {a} and {y} is {x}')
            z += 1
        elif o == '*' or o == 'x':
            y = findy()
            a = x
            x = x*y
            print(f'The product of {a} and {y} is {x}')
            z += 1
        elif o == '/':
            y = findy()
            a = x
            x = x/y
            print(f'The quotient of {a} and {y} is {x}')
            z += 1
        elif o == '%':
            y = findy()
            a = x
            x = x%y
            print(f'The remainder of {a} and {y} is {x}')
        elif o == '^':
            y = findy()
            a = x
            x = x**y
            print(f'{a}^{y} is equal to {x}')
            z += 1
        elif o == 'q':
            y = findy()
            b = y
            y = 1/y
            a = x
            x = x**y
            print(f'{b}q{a} is equal to {x}')
        elif o == 'sin':
            a = x
            x = m.radians(x)
            x = m.sin(x)
            print(f'The sine of {a} is {x}')
            z += 1
        elif o == 'cos':
            a = x
            x = m.radians(x)
            x = m.cos(x)
            print(f'The cos of {a} is {x}')
            z += 1
        elif o == 'tan':
            a = x
            x = m.radians(x)
            x = m.tan(x)
            print(f'The tan of {a} is {x}')
            z += 1
        elif o == 'asin':
            a = x
            x = m.asin(x)
            x = m.degrees(x)
            print(f'The inverse sin of {a} is {x}')
            z += 1
        elif o == 'acos':
            a = x
            x = m.acos(x)
            x = m.degrees(x)
            print(f'The inverse cos of {a} is {x}')
            z += 1
        elif o == 'atan':
            a = x
            x = m.atan(x)
            x = m.degrees(x)
            print(f'The inverse tan of {a} is {x}')
            z += 1
        elif o == 'log':
            y = findy()
            if y == 0:
                a = x
                x = m.log(x, m.e)
                print(f'The natural log of {a} is {x}')
                z += 1
            else:
                a = x
                x = m.log(x, y)
                print(f'The lof of {a} with a base {y} equals {x}')
                z += 1
        elif o == 's':
            yes = False
        else:
            print('Error, operator not recognized.')
    print(f'The final number is {x}')
    print(f'A total of {z} operations were performed.')

    return

if __name__ == '__main__':
    main()