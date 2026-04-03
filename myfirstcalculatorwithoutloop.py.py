#calculator.
print("press 1 to add")#operation selection for user.
print("press 2 to subtract")
print("press 3 to multiply")
print("press 4 to divide")

choice = int(input("Enter choice: "))

A = float(input("enter the first number: "))#Taking users input
B = float(input("enter the second number: "))
if(choice == 1):
    print(A+B)
elif(choice == 2):
    print(A-B)
elif(choice == 3):
    print(A*B)
elif(choice == 4):
    print(A/B)
input("press enter to exit: ")

