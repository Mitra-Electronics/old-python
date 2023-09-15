name = input("Enter your name: ")
num = int(input("Enter the number: "))
numstr = str(num)
print("Dear "+ name + " your result is the following: ")

for i in range(1, 16, 6):
    res = str(num * i)
    istr = str(i)
    print(numstr + " X "+ istr + " = " + res)
