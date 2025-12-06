import random
score = []
a = []
b = []
for i in range(5) :
    print ( "chance" ,i+1) 
    a.append(int(input("Enter a number between 1 to 100 : ")))
    b.append(random.randint(1,100))
    print("your number : " , a[i] ,"code's number : " , b[i])
    if a[i] > b[i]:
        score.append(1)
    elif a[i] < b[i]:
        score.append(-1)
    elif a[i] == b[i]:
        score.append(3)
total = sum(score)
print("score : " ,total)
if total > 0 :
    print("YOU WON")
elif total < 0 :
    print("CODE WON")
