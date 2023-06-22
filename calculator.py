def  add(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def  multiplication(x,y):  
    return x * y

def division(x,y):
    return x / y


print("*** select option ***")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")


while True:
    choice = input("enter choice (1/2/3/4)")

    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("enter 1st number"))
            num2 = float(input("enter 2nd number"))

        except ValueError:
            print("invalid input, please enter values")
            continue

        if choice == '1':
            print(num1 , "+" ,num2, "=", add(num1 , num2))

        elif choice == '2':
            print(num1 , "-" ,num2, "=", subtraction(num1 , num2))

        elif choice == '3':
            print(num1 , "*" ,num2, "=", multiplication(num1 , num2))
        
        elif choice == '4':
            print(num1 , "/" ,num2, "=", division(num1 , num2))

            next_calculation = input("let's do next calculation? (yes/no):" )
            if next_calculation =="no":
                break
    else:
        print("invalid input")