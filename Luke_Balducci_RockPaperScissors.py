import random                                                          # tells the computer to picka random element 
responses = [ 'rock', 'paper','scissors']                              # All of theweapons the computer can randomly select
score = 0                                                              # keeps the users score 
bot_score = 0                                                          # keeps te socre of the computer 

while True:                                                            # makes it so the game repeats its self the the user can play mulitple times
    if score == 3 or bot_score == 3:                                   # tells the computer that if someone has a score of 3 they win the game
        print("game over")                                             # tells the user that the game ended
        break                                                          # Stops the code so it doesnt repeat
    question  = input("choose rock, paper or scissors ")               # provides all of the weapons th euser can choose

    if question in responses:                                          # helps the computer decide who won the match
        bot=(random.choice(responses))                                 # makes the computer import a random element from the responses list
        print(f"You chose {question}, while the bot chose {bot}")      # tells the user how the match plyed out

        if question == bot:                                            # if computer and user choose the same weapon 
            print ("Tie")                                              # tells the user that they chose the same as the computer
        elif question== "rock" and bot == "scissors":                  # an example ofhow the match can play out
            print ("User Wins!")                                       #tells the user that they won the match
            score += 1                                                 # adds 1 to the users score
            bot_score -= 1                                             # subtracts 1 from the computer's score
        elif question== "paper" and bot == "rock":                     # an example ofhow the match can play out
            print ("User Wins")                                        #tells the user that they won the match
            score += 1                                                 # adds 1 to the users score
            bot_score -= 1                                             # subtracts 1 from the computer's score
        elif question=="scissors" and bot == "paper":                  # an example ofhow the match can play out
            print ("User Wins")                                        #tells the user that they won the match
            score += 1                                                 # adds 1 to the users score
            bot_score -=1                                              # subtracts 1 from the computer's score
        elif question=="rock" and bot=="paper":                        # an example ofhow the match cn play out
            print ("Computer Wins")                                    # tells the user that the computer won the match
            score -= 1                                                 # subtracts 1 from the user's score
            bot_score += 1                                             # adds 1 to the computer's score
        elif question== "paper" and bot == "scissors":                 # an example ofhow the match cn play out
            print ("Computer Wins")                                    # tells the user that the computer won the match
            score -= 1                                                 # subtracts 1 from the user's score
            bot_score += 1                                             # adds 1 to the computer's score
        elif question== "scissors" and bot == "rock":                  # an example ofhow the match cn play out
            print ("Computer Wins")                                    # tells the user that the computer won the match
            score -= 1                                                 # subtracts 1 from the user's score
            bot_score += 1                                             # adds 1 to the computer's score
        print (f"Your score is {score}")                               # Shows the user's score after every match 
        print (f"Computer score is {bot_score}")                       # shows the computer's score after every match 
    else:                                                              # if the user doesnt enter one of the elemts rps
        print("invalid answer")                                        # tells the user that they didnt choose one of the elements 

if score > bot_score:                                                  # if the user's socre is higher then the computer's score at the end of the game 
    print ('''You win!                                                 
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
''')                                                                   # tells the user that they won the game and gives them a trophy for their victory 
elif bot_score > score:                                                # if the user's socre is lower then the computer's score at the end of the game 
    print ("You lose!")                                                # tells the user that they lost the game