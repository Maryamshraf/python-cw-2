my_name = input("what is your name?")
my_age =int(input("how old are you?"))
print(f"my name is{my_name} and iam {my_age} years old")
first_number= int(input("enter first number:"))
secound_number= int(input("enter secound number:"))

operation = input("enter the operation")
if operation == "+" :
    print(first_number+secound_number)
    
elif operation== "-":
    print(first_number-secound_number)
elif operation== "*":
    print(first_number*secound_number)
elif operation== "/":
    print(first_number/secound_number) 
else: 
    print("the operation is not valid")


    bus_capacity = 30
    inbus = int(input("how many people are in the bus? "))
    outbus = int(input("how many people are out of the bus?"))
    empty_seats = bus_capacity - inbus
    print(empty_seats)
    if empty_seats>outbus:
        print("you can get in")
    elif empty_seats<=outbus:
        print("the bus is full")
 

