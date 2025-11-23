# names = ["artin", "abtin", "maria"]

# print(len(names))
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[-1])
# print(names[len(names) - 1])
# print(names[:2])
# print(names[1:])

# names[0] = "sara"
# names.append("ayda")
# names.remove("maria")
# for n in names:
#     print(n)


# i = 0 
# while i < len(names):
#     print(names[i])
#     i += 1


# names = []

# while True:
#     n = input("enter a name: ")
#     names.append(n)

#     if input("Do you want to quit(y or n)? ").lower().startswith("y"):
#         break
# print(names)

# numbers = (1,2,3,4,5)


# favorite_sports = {
#     'sara' :  'football',
#     'artin' : 'basketball'
# }

# favorite_sports['reza'] = 'baseball'
# del favorite_sports['sara']
# # print(favorite_sports)

# for key, val in favorite_sports.items():
#     print(key, val)


student = {}

name = input("enter the name: ")
age = int(input("enter the age: "))
grade = input("enter the grade: ")

student['esm'] = name
student['sen'] = age
student['nomre'] = grade

print(f"{student['esm']} is {student['sen']} years old and his/her grade is {student['nomre']}")