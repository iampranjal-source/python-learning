# Assuming exam was of 100 marks.
a1 = int(input("Enter marks of subject 1 : "))
a2 = int(input("Enter marks of subject 2 : "))
a3 = int(input("Enter marks of subject 3 : "))

if((a1+a2+a3)/300*100 < 40):
    print("Student has failed")

elif(a1<33 and a2>33 and a3>33):   # 1
    print("Students has failed")

elif(a1<33 and a2<33 and a3>33):
    print("Students has failed")

elif(a1<33 and a2>33 and a3<33):
    print("Students has failed")

elif(a1<33 and a2<33 and a3<33):
    print("Students has failed")

elif(a1>33 and a2<33 and a3>33):     # 2
    print("Students has failed")

elif(a1>33 and a2<33 and a3<33):
    print("Students has failed")

elif(a1<33 and a2<33 and a3>33):
    print("Students has failed")

elif(a1<33 and a2<33 and a3<33):
    print("Students has failed")

elif(a1>33 and a2<33 and a3<33):    # 3
    print("Students has failed")

elif(a1>33 and a2>33 and a3<33):
    print("Students has failed")

elif(a1<33 and a2<33 and a3<33):
    print("Students has failed")

elif(a1<33 and a2>33 and a3<33):
    print("Students has failed")

else:
    print("You have passed")


#MAJDOORI




# Assuming exam was of 100 marks.
a1 = int(input("Enter marks of subject 1 : "))
a2 = int(input("Enter marks of subject 2 : "))
a3 = int(input("Enter marks of subject 3 : "))

if((a1+a2+a3)/300*100 < 40):
    print("Student has failed")

elif(a1<33 or a2<33 or a3<33):
    print("Student has failed")

else:
    print("You have passed")

#SAMAJHDAARI