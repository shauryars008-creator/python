import random
score = 0
for i in range(10) :
    print ( "chance" ,i+1) 
    a = input("Enter a number between 1 to 100 : ")
    a = int(a)
    b = random.randint(1,100)
    print("your number : " , a ,"code's number : " , b)
    if a > b:
        score +=1
    elif a < b:
        score -=1
    elif a == b:
        score +=3
print("score : " ,score)
if score > 0 :
    print("YOU WON")
elif score < 0 :
    print("CODE WON")
