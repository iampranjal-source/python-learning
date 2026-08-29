friends = ["Apple", "Orange", 5, 646.03, False, "Aakash", "Rohan"]
print(friends)

friends.append("Harry")
# append means to add(jod dena) 
print(friends)

L1 = [1, 34, 78, 67, 54]
L1.sort()  # sort is a function which will write the nu,bers in ascending oreder
print(L1)


L1 = [1, 34, 78, 67, 54]
# L1.sort()
L1.reverse()  
print(L1)

L1 = [1, 34, 78, 67, 54]
# L1.sort()
# L1.reverse()  
L1.insert(3, 3333)  # Index comes before than the object
print(L1)
print(L1.pop(4))
print(L1)

L1 = [1, 34, 78, 67, 54]
# L1.sort()
# L1.reverse()  
#L1.insert(3, 3333)  # Index comes before than the object
#print(L1)
print(L1.pop(4))
print(L1)
# Here the outputs were different because we used the insert 
#function before the pop fucntion and when only the opo function was used the output was different.
 
L1 = [1, 34, 78, 67, 54]
L1.remove(34)
print(L1)
# with remove function inside the bracket do not type the index type the
# object that needs to be removed 