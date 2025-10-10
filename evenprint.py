w=input("Enter a word:")
if len(w)<=3:
    print("this string is not valid!!!")
elif w[-3:]=="ing":
    replace=w.replace("ing","ly")
    print("replaced word is:",replace)
    