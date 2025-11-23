# username = input("enter the username: ")
# password = input("enter the password: ")

# with open("userinfo.txt", "r") as f:
#     data = f.readlines()
# data[0] = data[0][:-1]
# correct_username = data[0]
# correct_password = data[1]

# if username == correct_username and password == correct_password:
#     print("login success")
# else:
#     print("login not success")
# myList = []
# for i in range(3):
#     myList.append(input("enter the name: ") +  "\n")


# with open("sample.txt", "a") as f:
#     f.writelines(myList)

# a = int(input("enter a number : "))
# b = int(input("enter a number : "))
# try:
#     print(a/b)
# except:
#     print("blallalal")

try:
    with open("sample.txt", "r") as f:
        f.read()

except:
    print("blalalal")
finally:
    print("this is a test")