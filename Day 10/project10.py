import os 
import art 
print(art.logo)
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    should_continue=True
    n1=float(input("Please enter your first number: "))
    for symbol in operations:
        print(symbol)
    while should_continue==True:
        choice=input("Please choose your operation: ")
        n2=float(input("Please enter your next number: "))
        calculation_function=operations[choice]
        ans=calculation_function(n1,n2)
        print(f"{n1} {choice} {n2} = {ans}")
        if input(f"Type 'yes' to continue calculating with {ans}, or type 'no' to start a new calculation: ").lower()=="yes":
            n1=ans
        else:
            os.system('cls')
            should_continue=False
            calculator() #recursive 
calculator()