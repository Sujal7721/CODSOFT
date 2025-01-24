import random

# def add_userscore(int a):
#     v = 0
#     v = a + v
#     return v
    


flag = True
user_score = 0
com_score = 0
while(flag):
   user_input = input("Choose Rock, Paper or Scissor \n")
   com = random.randint(1,3)
#    user_score = 0
#    com_score = 0
   choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
   com_choice = choices[com]

   print("Computer chose: ", com_choice)

   if(user_input == com_choice):
      print("It's a tie!")
   elif(user_input == "Rock" and com_choice == "Scissor"):
      print("Rock smashes scissor! You win!")
      user_score = 1 + user_score
   elif(user_input == "Paper" and com_choice == "Rock"):
      print("Paper covers rock! You win!")
      user_score = 1 + user_score
   elif(user_input == "Scissor" and com_choice == "Paper"):
      print("Scissors cuts paper! You win!")
      user_score = 1 + user_score
   else:
      print("You lose!")
      com_score = 1 + com_score
      
    

   again = input("Do you want to play again? Choose [y/n]: ")
    
   if("y" == again):
    flag = True
   elif("n" == again):
    flag = False
    print("User Score is ",user_score)
    print("Computer Score is ",com_score)
#    else:
#     print("Invalid Input! chose [y/n]")
#     print("User Score is ",user_score)
#     print("Computer Score is ",com_score)
#     break
    
  

