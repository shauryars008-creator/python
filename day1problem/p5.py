print("enter the complex numbers in form a+bj where a and b are rationals")
while True :
    x = input("1st complex number = ")
    x = x.replace(" ","")
    x = complex(x)
    y = input("2nd complex number = ")
    y = y.replace(" ","")
    y = complex(y)
    opr = input("enter the operation +,-,* or / : ")
    if opr == "+" :
        print("sum =",x+y)
    elif opr == "-" :
        print("difference =" ,x-y)
    elif opr == "*" :
        print("product =" ,x*y)
    elif opr == "/" :
        print("quotient =" ,x/y)
