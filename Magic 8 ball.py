import random
import time
response = ["Outcome is hazy", "It is unclear at the moment", "It is certain", "It will be true", "This is not to be"]

play = "Y"


while play == "Y":
    print("Ask any question!")
    q = input()
    print("Thinking...")
    time.sleep(2)
    print(random.choice(response) + "\n")

    time.sleep(1)

    #Asks if they want to play again
    print("Would you like to play again? (Y/N)")
    play = input()
    if play == "N":
        exit()
            

    #In case the person doesn't enter either Y or N
    while play != "Y":
        print("Would you like to play again? (Y/N)")
        play = input()

        
        if play == "N":
            exit()

        

        

    
    

    
        

    
