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


reverse = ""
num = input("Enter a number: ")
for i in range (len(num),0,-1):
    reverse += num[i-1]
print(int(reverse))


reverse = 0
number = int(input("Enter a num: "))
while(number > 0):
    remainder = number %10
    reverse = (reverse*10)+remainder
    number= number//10

print('\n reverse is:%d'%reverse)

print(input("Enter a num: ")[::-1])

