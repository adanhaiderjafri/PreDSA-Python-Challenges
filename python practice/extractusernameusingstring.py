gmail = input("tell me your gmail id :")
if "@"and "." and  "com" in gmail :
    user_name=gmail.split("@")[0]
    print(f"your user_name is : {user_name}")
    domain_name=gmail.split("@")[1]
    print(f"your domain name is : {domain_name}")
    extension=gmail.split(".")[1]
    print(f"your extension is : {extension}")
else:
    print(f"your gmail id is incorrect")