#create a basic calculator that can perform basic arithmetic operations such as addition subtraction multiplication and division using functions in python

def add(a,b):
    result=a+b
    return result

def sub(a,b):
    result=a-b
    return result

def mul(a,b):
    result=a*b
    return result

def div(a,b):
    result=a/b
    return result

def calculator():
    calculate=True
    while calculate:
        L=["1.Addition(+)","2.Subtraction(-)","3.Multiplication(*)","4.Division(/)"]
        for i in L:
            print(i,"\n")
        choice = int(input("Enter Your Choice: "))
        print("\n")
        if choice==1:
            x=float(input("enter Number: "))
            y=float(input("enter Number: "))
            s=add(x,y)
            print(f"Addition of {x} and {y} is {s} \n")
        elif choice == 2:
            x=float(input("enter Number: "))
            y=float(input("enter Number: "))
            s=sub(x,y)
            print(f"Subtraction of {x} and {y} is {s} \n")
        elif choice == 3:
            x=float(input("enter Number: "))
            y=float(input("enter Number: "))
            s=mul(x,y)
            print(f"Multiplication of {x} and {y} is {s} \n")
        elif choice == 4:
            x=float(input("enter Number: "))
            y=float(input("enter Number: "))
            s=div(x,y)
            print(f"Division of {x} and {y} is {s} \n")
        else:
            print("Please choose which operation you want to perform!(1 to 4)\n")
        
        user_choice=input("Do you want to perform more calculations? (Y/N)").lower()
        if user_choice=="y":
            calculate=True
        else:
            calculate=False      
calculator()            