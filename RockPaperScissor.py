import random
while True:
    print ("Game rules : - \n Rock vs Paper => paper wins \n Rock vs Scissor => Rock wins \n Paper vs Scissor => Scissor wins")
    print ("Its your turn \n 1. Rock \n 2. Paper \n 3. scissor")
    while True: 
        user_input = int (input(" Choose one :- "))

        if user_input >0 and user_input < 4:
            if user_input == 1:
                print ("You choose:- Rock")
            elif user_input == 2:
                print ("You choose:- Paper")
            elif user_input == 3:
                print ("You choose:- Scissor")
            break
                
        else:
            print ("Invalid input \n Please choose again")

    print("Computer initiating its choice...")
    com_input = random.randint(1,3)
    if com_input == 1:
        print ("computer choose:- Rock")
    elif com_input == 2:
        print ("computer choose:- Paper")
    elif com_input == 3:
        print ("computer choose:- Scissor")

    else:
        print ("Thier is some issue")  


    if user_input == 1 and com_input == 2 or user_input == 2 and com_input == 3:
        #final_result = "Paper"
        print ("Computer Won")

    elif user_input == 2 and com_input == 1 or user_input == 3 and com_input == 2:
        #final_result = "Paper"
        print ("You Won")

    elif user_input == 3 and com_input == 1 or user_input == 2 and com_input == 3:
        #final_result = "Paper"
        print ("Computer Won")

    elif user_input == 3 and com_input == 2 or user_input == 1 and com_input == 3:
        #final_result = "Paper"
        print ("your Won")

    else:
        print ("It's a tie")


    print ("Do you want to play again ? \n press 0 for yes or 1 to Exit : ")
    user_input2 = int(input())
    if user_input2 == 1:
        print ("Thank You")
        break
        