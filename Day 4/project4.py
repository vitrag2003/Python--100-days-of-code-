import random
game=["rock","paper","scissor"]
user=int(input("0.Rock\n1.Paper\n2.Scissor\nPlease give ur action type: "))
computer=random.randint(0,2)
print(f"Computer chose: {game[computer]}")
if user==0 and computer==0:
    print("Draw")
elif user==1 and computer==1:
    print("Draw")
elif user==2 and computer==2:
    print("Draw")

elif user==0 and computer==1:
    print("Computer wins")
elif user==0 and computer==2:
    print("User wins")

elif user==1 and computer==0:
    print("User wins")
elif user==1 and computer==2:
    print("Computer wins")

elif user==2 and computer==0:
    print("Computer wins")
elif user==2 and computer==1:
    print("User wins")
else:
    print("Please enter a valid number")