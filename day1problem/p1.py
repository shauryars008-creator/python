x=input("enter first number = ")
x=float(x)
y=input("enter second number = ")
y=float(y)
opr=input("enter the operation +,-,* or / : ")
if opr == "+" :
    print("sum =",x+y)
elif opr == "-" :
    print("difference =" ,x-y)
elif opr == "*" :
    print("product =" ,x*y)
elif opr == "/" :
    print("quotient =" ,x/y)
