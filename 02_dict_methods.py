marks = {"Harry": 100,
         "Shubham": 56,
         "Rohan": 45, 
         0 : "Harry"}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

#marks.update({"Harry": 99}) 
#print(marks["Harry"])
#print(marks)

print(marks.get("Harry"))
print(marks["Harry"])
#here Harry exists in dictionary so btoh the output are 100

print(marks.get("Harry2"))
print(marks["Harry2"])
#but if the item does not exist in the dictioanry so .get func fuves none but [] func gives error.
#.get() give none instead of crashing out and is iseful in finding item in dict if you are sure
#the existence if the item and dont want your system to crash. both the codes look for items in the dict but one gives none and other crashes out.