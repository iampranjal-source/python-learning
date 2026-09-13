a = int(input("Enter you age : "))

# if elif else ladder.
if(a>=18):
    print("You are above the age of consent")
    print("You are good")

elif(a<0): 
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering an invalid age")


else:
    print("You are below the age limit")


print("End of the programme")