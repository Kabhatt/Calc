#Simple Calculator Build
# 1.ADD
# 2.SUBSTRACT
# 3.MULTIPLY
# 4.DIVIDE

print("Please Choose an operation to preform:")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

choice = input("Enter your Choice: ")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
if choice == "1":
    print("The Sum is:" + str(int(num1) + int(num2)))
elif choice == "2":
    print("The difference is:" + str(int(num1) - int(num2)))
elif choice == "3":
    print("The product is:" + str(int(num1) * int(num2)))
elif choice == "4":
    if num2 == 0.0:
        print("Divide by 0 Error")
    else:
        print("The Quotient is:" + str(int(num1) / int(num2)))



