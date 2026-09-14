a = int(input("Enter you age : "))

# If statement no:1
if(a%2 == 0): 
    print("a is even")
# End of if statement no: 1

# If statement no:2
if(a>=18):
    print("You are above the age of consent")
    print("You are good")

elif(a<0): 
    print("You are entering an invalid negative age")


elif(a==0):
    print("You are entering an invalid age")


else:
    print("You are below the age limit")
# End of if statement no:2


print("End of the programme")

