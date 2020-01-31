print("Welcome to odd even formula originals")
print("In this, you need to enter any number, and we wil tell you the number is odd or even.")

print("                                                                               ")
x = int(input("Enter a number: "))
remainder = x % 2

if remainder == 0:
    print(str(x) + " is an even number.")
else:
    print(str(x) + " is an odd number.")

print("                                                                         ")
y = input("Do you want to use again?, yes or no: ")

while y == "yes":
    x = int(input("Enter a number: "))
    remainder = x % 2

    if remainder == 0:
        print(str(x) + " is an even number.")
    else:
        print(str(x) + " is an odd number.")
    print("                                                    ")
    y = input("Do you want to use again?, yes or no: ")

if  y == "no":
    print("Okay thanks")

