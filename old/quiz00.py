# for i in range(1,5):
#     print(i * "*")

# n = int(input("enter the number: "))
# for i in range(n, 0, -1):
#     print(i)

# numbers = []
# even_numbers = []
# for i in range(3):
#     n = int(input("enter the number: "))
#     numbers.append(n)
#     if n % 2 == 0:
#         even_numbers.append(n)
# print("all numbers",numbers)
# print("even numbers",even_numbers)
# print(max(numbers))
# print(sum(numbers)/len(numbers))


# names = ["ali", "sara"]
# names.reverse()
# print(names)

# new_list = []
# for i in range(len(names) - 1, -1, -1):
#     new_list.append(names[i])

# print(new_list)


# if "ali" in names:
#     print("yes")


numbers = []
for i in range(1, 11):
    numbers.append(i)

for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[i] * numbers[j], end="  ")
    print()