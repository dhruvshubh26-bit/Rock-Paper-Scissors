import random 

computer_choice = random.choice([0,1,2]) #0 For Rock 1 For Paper 2 For Scissors

mine_choice = int(input("Enter your choice : "))

if(computer_choice==mine_choice):
    print("Draw")
else:
    if(computer_choice==0 and mine_choice==1):
        print("You Won!")
    elif(computer_choice==0 and mine_choice==2):
        print("You loose!")
    elif(computer_choice==1 and mine_choice==0):
        print("You lose!")
    elif(computer_choice==1 and mine_choice==2):
        print("You won!")
    elif(computer_choice==2 and mine_choice==0):
        print("You won!")
    elif(computer_choice==2 and mine_choice==1):
        print("You lose!")
    
