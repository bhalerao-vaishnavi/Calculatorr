
from re import A
from secrets import choice

def add(a,b):
    sum = a + b
    print("\nAddition:",sum)

def multiplication(a,b):
    mul = a * b
    print("\nMultiplication:",mul)

def division(a,b):
    div = a / b
    print("\nDivision:",div)

def modulus(a,b):
    mod =a % b
    print("\nModulus:",mod)

#choice
while True:
    print("\n:::::::::::::::::::::::Calculator:::::::::::::::::::::::")
    print("\n1:Addition")
    print("\n2:Multiplication")
    print("\n3:Division")
    print("\n4:Modulus")
    choice1 = int(input("\n\nEnter a choice "))
            
    if choice1 == 1:
        a = int(input("\nEnter a number"))
        b = int(input("\nEnter a number"))
        add(a,b)

    elif choice1 == 2:
        a = int(input("\nEnter a number"))
        b = int(input("\nEnter a number"))
       
        multiplication(a,b)
        a = int(input("\nEnter a number"))
        b = int(input("\nEnter a number"))
    elif choice1 == 3:
        a = int(input("\nEnter a number"))
        b = int(input("\nEnter a number"))      
        division(a,b)

    elif choice1 == 4:
        a = int(input("\nEnter a number"))
        b = int(input("\nEnter a number"))
       
        modulus(a,b)

    elif choice1 == 5:

        break

    else:
        print("something is wrong")
 