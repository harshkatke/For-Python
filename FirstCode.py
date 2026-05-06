Name=input("Enter Your Name : ")
print(Name)

Login_id=input("Login_id : ")

if "@" in Login_id and ".com" in Login_id:
    print("Verified")
else:
 print("Not verified")
Pass=input("Pass")
if Pass=="12345":
    print("Done")
else:
    print("Error")
    exit()