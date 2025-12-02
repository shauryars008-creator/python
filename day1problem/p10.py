pow = input("enter the power 2,3 or 4 : ")
pow = int(pow)
if pow == 2 :
    print("to prove (a+b)**2 = a**2 + b**2 + 2*a*b")
    a=input("enter first number = ")
    a=float(a)
    b=input("enter second number = ")
    b=float(b)
    lhs = (a+b)**2
    rhs = a**2 + b**2 + 2*a*b
    print("lhs =" , lhs,"rhs =" , rhs)
    if lhs == rhs :
        print ("lhs == rhs HENCE PROVED")
if pow ==3 :
    print("to prove (a+b)**3 = a**3 + b**3 + 3*a**2*b +3*b**2*a")
    a=input("enter first number = ")
    a=float(a)
    b=input("enter second number = ")
    b=float(b)
    lhs = (a+b)**3
    rhs = a**3 + b**3 + 3*a**2*b +3*b**2*a
    print("lhs =" , lhs,"rhs =" , rhs)
    if lhs == rhs :
        print ("lhs == rhs HENCE PROVED")
if pow == 4:
    print("to prove (a+b)**4 = a**4 + b**4 + 4*a**3*b + 4*b**3*a + 6*a**2*b**2")
    a=input("enter first number = ")
    a=float(a)
    b=input("enter second number = ")
    b=float(b)
    lhs = (a+b)**4
    rhs = a**4 + b**4 + 4*a**3*b + 4*b**3*a + 6*a**2*b**2
    print("lhs =" , lhs,"rhs =" , rhs)
    if lhs == rhs :
        print ("lhs == rhs HENCE PROVED")
