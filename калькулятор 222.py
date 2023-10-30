import math
print("0 в качестве знака операции"
      "\nзавершит работу программы\n")
 
while True:
    s = input("Знак: ")
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        a = float(input("a = "))
        b = float(input("b = "))
        if s == '+':
            print("%.2f" % (a + b))
        elif s == 'sin':
            print(math.sin(5))
        elif s == '-':
            print("%.2f" % (a - b))
        elif s == '*':
            print("%.2f" % (a * b))
        elif s =='/':
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("Деление на ноль!")
    elif s in ('cos'):
        a = float(input("a = "))
        print(math.cos(a))
    elif s in ('!'):
        a = float(input("a = "))
        print(math.factorial(a))
    elif s in ('sin'):
        a = float(input("a = "))
        print(math.sin(5))
    elif s in ('tan'):
        a = float(input("a = "))
        print(math.tan(a))
    else:
        print("Неверный знак операции!")
