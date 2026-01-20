
# i=0

# while i<5:
#     print("Step1")
#     print("Step2")
#     print("Step3")
#     print("----------------")
#     i+=1

# print("Loop over!")

# No of Iteration:
# i=0

# For 

# a=range(3,30,3)
# print(list(a))

# print(a[5])
# print(len(a))

# for x in a:
#     print(x)
#     print("----------------")

#100
    
# for i in a:
#     print("Hello"+str(i))
#     print("----------------")


# i=0

# while i<100:
#     print(i)
#     if i>=25:
#         break
#     i+=1

# for i in range(51):
#     if i==25:
#         pass
#     print(i)

# i=int(input("Enter a number: "))

# if i==0:
#     print("Null")
# elif i==1:
#     print("One")
# elif i==2:
#     pass
# else:
#     print("Others")

# a="Dhoni"

# for i in a:
#     print(i)

# for i in range(100):
#     print("Hello")


secret_number=33

while True:
    num=int(input("Guess a number: "))
    if num==secret_number:
        print("You won!")
        break
    else:
        print("Try again!")