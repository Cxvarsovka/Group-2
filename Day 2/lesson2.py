name = str(input("Whats Your Name ? "))
age =  int(input("Whats Your Age? "))
size = len(name)
if age >= 18 :
    if ord(name[0]) >= 65 and ord(name[0]) <= 90:
        print(name , "Your Are Adult")
        print("And Your Name Contains" , size ,"Character")
    else :
        print("Human name starts with capitall letter , you should remember this ok?")
        print(name , "Your Are Adult")
        print("And Your Name Contains" , size ,"Character")
else :
    if ord(name[0]) >= 65 and ord(name[0]) <= 90:
        print("You Are Kid")
        print("And Your Name Contains" , size ,"Character") 
    else:
        print("Human name starts with capitall letter , you should remember this ok?")
        print(name , "Your Are Kid")
        print("And Your Name Contains" , size ,"Character")
