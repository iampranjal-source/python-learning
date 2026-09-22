a = "Harry"

post = input("Enter your comment : ")

if((a in post)):
    print("Harry is a part of the given post")

else:
    print("Harry is not a part of the given post")



post = input("Enter the post : ")

if("Harry".lower() in post.lower()):            # if i write harry the also it will detect.
    print("This post is talking about Harry")

else: 
    print("This post is not talking about Harry")