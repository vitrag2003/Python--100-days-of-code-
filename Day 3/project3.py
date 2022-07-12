print('''
            _ _ _
           | / \ |
           | \_/ |
            \___/ ___
            _|_|_/[_]\__==_
           [---------------]
           | O   /---\     |
           |    |     |    |
           |     \___/     |
           [---------------]
                 [___]
                  | |\\
                  | | \\
                  [ ]  \\_
                 /|_|\  
                //| |\\   
               // | | \\  
              //  |_|  \\  
             //   | |   \\
            //\   | |   /\\
           //  \  | |  /  \\
          //    \ | | /    \\
         //      \|_|/      \\
        //        [_]        \\
       //          H          \\
      //           H           \\
     //            H            \\
    //             H             \\
   //              H              \\
  //                               \\
 //                                 \\
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input("You are at a crossroad, where do u want to go? Type 'left' or 'right' ").lower()
if choice1=="right":
      print("Game over")
elif choice1=="left":
      choice2=input("You have come to a lake. There is an island in the middle of a lake. Type 'wait' to wait for the boat. Type 'swim' to swim across.").lower()
      if choice2=="wait":
            choice3=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
            if choice3=="red":
                  print("Game over")
            elif choice3=="yellow":
                  print("You win the game")
            elif choice3=="blue":
                  print("Game over")
            else:
                  print("Please enter valif input")
      elif choice2=="right":
            print("Game over")
      else:
            print("Please enter valid input")
else:
      print("Please enter valid input")