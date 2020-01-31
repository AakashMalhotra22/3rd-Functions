print("Instruction: You can calculate the reverse find 1 digit numbers to 3 digits number.")

def reverse_function(num):
    if len(num)==1:
        print(num)
    elif len(num) ==2:
        print(num[1]+num[0])
    elif len(num) ==3:
        print(num[2]+num[1]+num[0])
    else:
        print("Valid till three digit numbers.")

reverse_function(input("Enter a num: "))

q1 = input("Want to try again, say yes or no: ")

if q1 == "no":
    print("Okay thanks")

while q1 == "yes":
    def reverse_function(num):
        if len(num) == 1:
            print(num)
        elif len(num) == 2:
            print(num[1] + num[0])
        elif len(num) == 3:
            print(num[2] + num[1] + num[0])
        else:
            print("Valid till three digit numbers.")


    reverse_function(input("Enter a num: "))

    q1 = input("Want to try again, say yes or no: ")
    if q1 == "no":
        print("Okay thanks")
1
