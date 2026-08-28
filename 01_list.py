# a[3] = 'y'  (rpl)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
# you cannot make chnage in string but you can in lists

friends = ["Apple", "Orange", 5, 646.03, False, "Aakash", "Rohan"]

print(friends[0])
print(friends[5])

friends[1] = "Hat" # Unlike strings lists are mutable 
print(friends[1]) 

print( friends[1:5])