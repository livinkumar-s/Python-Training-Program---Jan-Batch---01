print(33)
print(34)
print(35)
if True:
    print(34)

# Print("Hello")

# print("Hello"+4)

# try:
#     Print(float("the"))
# except ValueError:
#     print("Please provide valid String...!")
# except ZeroDivisionError:
#     print("Invalid Expression...!")

# print(9/0)

# print(int("Hello"))

try:
    num1=int(input("Enter 1 Number: "))
    num2=int(input("Enter 2 Number: "))
    print("The result is:", num1/num2)
except ValueError:
    print("Enter a valid Input...!")
except ZeroDivisionError:
    print(f"{num1} cannot be divided by {num2}...!")
finally:
    print("It is over")

print(1)