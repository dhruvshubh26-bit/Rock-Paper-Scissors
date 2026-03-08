import random 

computer_choice_int = random.choice([0,1,2]) #0 For Rock, 1 For Paper, 2 For Scissors

mine_choice_str = input("Enter your choice : ") #'r' for Rock ,'p' for Paper, 's' for Scissors

mine_choice_dict={'r':0,'p':1,'s':2}

rev_choice_dict={0:'Rock',1:'Paper',2:"Scissors"}

mine_choice_int=mine_choice_dict[mine_choice_str]

mine_choice=rev_choice_dict[mine_choice_int]
computer_choice = rev_choice_dict[computer_choice_int]
print(f"You choose {mine_choice} and computer choose {computer_choice}")

if(computer_choice_int==mine_choice_int):
    print("\nDraw")
else:
    if(computer_choice_int==0 and mine_choice_int==1):
        print("\nYou Won!")
    elif(computer_choice_int==0 and mine_choice_int==2):
        print("\nYou loose!")
    elif(computer_choice_int==1 and mine_choice_int==0):
        print("\nYou lose!")
    elif(computer_choice_int==1 and mine_choice_int==2):
        print("\nYou won!")
    elif(computer_choice_int==2 and mine_choice_int==0):
        print("\nYou won!")
    elif(computer_choice_int==2 and mine_choice_int==1):
        print("\nYou lose!")
    
