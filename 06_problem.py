marks = int(input("Enter your marks : "))

if(90<marks<=100 or marks == 90 ):
    print("Excellent")

elif(80<marks<90 or marks == 80):
    print("A")

elif(70<marks<=80 or  marks == 70):
    print("B")

elif(60<marks<=70 or marks == 60):
    print("C")

elif(50<marks<=60 or marks == 50):
    print("D")

elif(marks<50):
    print("F")