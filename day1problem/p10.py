print("to prove (a+b)**2 = a**2 + b**2 + 2*a*b")
a=input("enter first number = ")
a=int(a)
b=input("enter second number = ")
b=int(b)
LHS = (a+b)**2
RHS = a**2 + b**2 + 2*a*b
print("LHS =" , LHS,"RHS =" , RHS)
if LHS == RHS :
    print ("LHS == RHS HENCE PROVED")

print("to prove (a+b)**3 = a**3 + b**3 + 3*a**2*b +3*b**2*a")
a=input("enter first number = ")
a=int(a)
b=input("enter second number = ")
b=int(b)
LHS = (a+b)**3
RHS = a**3 + b**3 + 3*a**2*b +3*b**2*a
print("LHS =" , LHS,"RHS =" , RHS)
if LHS == RHS :
    print ("LHS == RHS HENCE PROVED")

print("to prove (a+b)**4 = a**4 + b**4 + 4*a**3*b + 4*b**3*a + 6*a**2*b**2")
a=input("enter first number = ")
a=int(a)
b=input("enter second number = ")
b=int(b)
LHS = (a+b)**4
RHS = a**4 + b**4 + 4*a**3*b + 4*b**3*a + 6*a**2*b**2
print("LHS =" , LHS,"RHS =" , RHS)
if LHS == RHS :
    print ("LHS == RHS HENCE PROVED")
