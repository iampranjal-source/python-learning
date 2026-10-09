def goodday(name, ending):
    print("Good Day, " + name)
    print(ending)

goodday("Harry", "Thank you")
goodday("Rohan", "Thank you")
goodday("Amit", "Thank you")




def goodday(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "Ending"

a = goodday("Harry", "Thank you")
print(a)