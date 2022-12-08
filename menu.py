num1=int(input("enter your 1st number: "))
num2=int(input("enter your 2nd number: "))

print("1.addition 2.subtraction 3.multiplication 4.division")
ch=input("enter your choice: ")
if (ch == '1'):
    add = num1+num2
    print("addition of number is:")
    print(add)
elif (ch == '2'):
    sub = num1-num2
    print("Subtraction of number is:")
    print(sub)
elif (ch == '3'):
    multi = num1*num2
    print("Multiplication of number is:")
    print(multi)
elif (ch == '4'):
    div = num1/num2
    print("division of number is")
    print(div)