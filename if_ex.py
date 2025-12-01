# if name is "XYZ" and age is below 40, 
# print "suitable" else if age is greater
# than 50, print "old", else print "OK"
# For all other names, print "not known" 

#objective - how to write nested if block 
#with correct identation 
#if name checking , inside if age checking

age=100
name="XY"
if (name=="XYZ"):
    if age<40:
        print("suitable")
    elif age>50:
        print("old")
    else:
        print("ok")
else:
    print("not known")
