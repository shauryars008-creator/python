import random
while True :
    x = input("enter a letter A,B,C or D : ")
    y = input("enter a number from 1 to 13 : ")
    y = int(y)

    p = random.choice("ABCD") 
    q = random.randint(1,13)

    print("your choice : " ,x,y , "code's choice : " ,p,q)
    if x > p :
        print("YOU WIN")
    elif x < p :
        print("CODE WINS")
    else :
        if y > q :
            print("YOU WIN")
        if y <= q :
            print("CODE WINS")
