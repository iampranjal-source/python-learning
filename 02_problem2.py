l = ["Harry", "Soham", "sachin", "Sachin", "Rahul"]


for name in l:
    if(name.startswith("S")):
        print(f"Good evening {name}")

    elif(name.startswith("s")):
        print(f"Good evening {name}")




l = ["Harry", "Soham", "sachin", "Sachin", "Rahul"]

for name in l:
    if name.startswith(("S", "s")):
        print(f"Good evening {name}")

# third line is very important kyunki isme do brackets use hue hain jahan outer bracket 
# calls out the function and the inner bracket used for tuple.

   




    
