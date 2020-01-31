reverse = ""
num = input("Enter a number: ")
for i in range (len(num),0,-1):
    reverse += num[i-1]
print(int(reverse))

q1 = input("Want to try again, say yes or no: ")

if q1 == "no":
    print("Okay thanks")

while q1 == "yes":
    reverse = ""
    num = input("Enter a number: ")
    for i in range(len(num), 0, -1):
        reverse += num[i - 1]
    print(int(reverse))

    q1 = input("Want to try again, say yes or no: ")

    if q1 == "no":
        print("Okay thanks")
