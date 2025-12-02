import cmath
while True :
    x=input("1st complex number = ")
    x= x.replace(" ","")
    x=complex(x)
    y=input("2nd complex number = ")
    y= y.replace(" ","")
    y=complex(y)
    opr=input("enter the operation +,-,*,/,sqrt,sin,cos,tan,log or exp :")
    if opr == "+" :
        print("sum =",x+y)
    elif opr == "-" :
        print("difference =" ,x-y)
    elif opr == "*" :
        print("product =" ,x*y)
    elif opr == "/" :
        print("quotient =" ,x/y)
    elif opr == "sqrt" :
        print("root1st =" ,cmath.sqrt(x) ,"root2nd =" ,cmath.sqrt(y))
    elif opr == "sin" :
        print("sin1st =" ,cmath.sin(x) ,"sin2nd =" ,cmath.sin(y))
    elif opr == "cos" :
        print("cos1st =" ,cmath.cos(x) ,"cos2nd =" ,cmath.cos(y))
    elif opr == "tan" :
        print("tan1st =" ,cmath.tan(x) ,"tan2nd =" ,cmath.tan(y))
    elif opr == "log" :
        print("log1st =" ,cmath.log(x) ,"log2nd =" ,cmath.log(y))
    elif opr == "exp" :
        print("exp^1st =" ,cmath.exp(x) ,"exp^2nd =" ,cmath.exp(y))