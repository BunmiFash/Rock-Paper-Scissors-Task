from ast import Pass
from logging import raiseExceptions
import random
from secrets import choice
print("Welcome to Rock, Paper, Scissors.\nRock crushes Scissors,\nScissors cuts Paper,\nPaper covers rock!")
print("R = Rock")
print("P = Paper")
print("S = Scissors")
while True:
    def user_selection(user):
        while True:
            try:
                User_Choice = input("Select R, P, or S \n") 

                if User_Choice not in option:
                    raise Exception
                break

            except:
                print("You must Select R, P, or S to play.") 
        
        if User_Choice == "R":
            User_Choice = "Rock"

        elif User_Choice == "P":
            User_Choice = "Paper"

        elif User_Choice == "S":
            User_Choice = "Scissors"

        return User_Choice 

    def computer_selection():

        Computer = random.choice(option)
        if Computer == "R":
            Computer = "Rock"

        if Computer == "P":
            Computer = "Paper"   

        if Computer == "S":
            Computer = "Scissors" 

        print("Player""(", User_Choice ,")", ":" , "CPU" "(", Computer, ")"  )  



        if User_Choice == "Rock":
            if Computer == "Scissors":
                print ("You win! Rock crushes Scissors.")
            elif Computer == "Paper":
                print("CPU Wins! Paper covers Rock.")  

        if User_Choice == "Paper":
            if Computer == "Rock":
                print ("You Win! Paper covers Rock.") 
            elif Computer == "Scissors":
                print ("CPU Wins! Scissors cuts Paper.")   

        if User_Choice == "Scissors":
            if Computer == "Paper":
                print ("You Win! Scissors cuts Paper.")  
            elif Computer == "Rock":
                print ("CPU Wins! Rock crushes Scissors.")   
        
        if User_Choice == Computer:
            print ("It's a tie, play again!")
            pass
            
            
                
            

    option = ["R", "S", "P"]
    User_Choice = user_selection(option)  
    Computer = computer_selection()  

    Option = input("Would you like to play again? Yes/No \n")  
    if Option == "Yes":
        pass
    elif Option == "yes":
        pass
    elif Option == "YES":
        pass
    elif Option == "No":
        break     
    elif Option == "no":
        break
    elif Option == "NO":
        break
    else:
        print("Invalid choice!")
        break
print("Thanks for Playing.\n Rate us below.")         
           

