import math
x=input("enter first number = ")
x=float(x)
y=input("enter second number = ")
y=float(y)
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
    print("root1st =" ,math.sqrt(x) ,"root2nd =" ,math.sqrt(y))
elif opr == "sin" :
    print("sin1st =" ,math.sin(x) ,"sin2nd =" ,math.sin(y))
elif opr == "cos" :
    print("cos1st =" ,math.cos(x) ,"cos2nd =" ,math.cos(y))
elif opr == "tan" :
    print("tan1st =" ,math.tan(x) ,"tan2nd =" ,math.tan(y))
elif opr == "log" :
    print("log1st =" ,math.log(x) ,"log2nd =" ,math.log(y))
elif opr == "exp" :
    print("exp^1st =" ,math.exp(x) ,"exp^2nd =" ,math.exp(y))