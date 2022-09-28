def registration():
    my_name = str(input("Whats Your Name ? ")) 
    my_lastname = str(input("Whats Your Lastname ? "))
    my_age = int(input("Whats Your Age ?"))
    my_password = str(input("Please Enter The New Password : "))
    my_mail = str(input("Please Enter Your Mail : "))
    info = open("info1.txt" , "a")
    info.write("Name : {} ; Lastname : {} ; Age : {} ; Mail : {} ; Password : {} \n".format(my_name , my_lastname , my_age , my_mail , my_password))

    
registration()
