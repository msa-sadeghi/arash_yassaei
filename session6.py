# person = ('ali', 32, 'tehran')

# print(f"{person[0]} is {person[1]} and lives in  {person[2]}")
# for item in person:
#     print(item)

# person = {
#     'name' : 'ali',
#     'age' : 32,
#     'city' : "teh"
# }

# for item in person.items():
#     print(item)


# def greet(name):
#     print("hello", name)

# greet("sara")
# greet("reza")


# def add(a, b, c):
#     return a + b + c

# print(add(23, 4, 56))

# def average(numbers):
#     return sum(numbers) / len(numbers)


# print(average([1,2,3,4,5,6]))

def validate_national_code(code):
    return len(code) == 10 and code.isdigit()

print(validate_national_code("123"))
print(validate_national_code("123456789"))
print(validate_national_code("1234567890"))
print(validate_national_code("123456789s"))