#if  = Do some code only IF some condition is True
#     Else do something else
#age
#name
#response
#online


age = int(input("Enter your age: "))

if age >= 100:
    print("You are old to sign in idiot!")
elif age >=18:
    print("You are now sign in")
elif age <=0:
    print("You haven't born yet!")
else:
    print("You must be 18+ to sign in")