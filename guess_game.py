#show levels
def show_levels():
    print('''Game levels:
        (1) Easy:  
            *limits:[1-10]
            *no.of trials:3
        (2) Intermediate:  
            *limits:[1-100]
            *no.of trials:7
        (3) Hard:  
            *limits:[1-1000]
            *no.of trials:15''')
            
#ask the user for the game level           
def game_level_choice():
     while True:
         game_level=int(input('Enter the game level: '))          
         if game_level in[1,2,3]:
              break
         else:
             print("Invalid choice please choose 1,2 or 3")
             continue
     return game_level       

# set the game setting       
def setgame_setting(game_level):
     if game_level==1:
         limits=range(1,11)
         no_trials=3
     elif game_level==2:
          limits=range(1,101)
          no_trials=7
     else:
          limits=range(1,1001)
          no_trials=15
    
     return limits,no_trials
    
 
#start playing
import random
def start_play(limits,no_trials):
     hidden=random.choice(limits)
     user_trial=0
     while user_trial<no_trials:
         guss=int(input("Guss the number: "))
         user_trial+=1
    
         if guss==hidden:
             print(f"You succeeded with no_trials{user_trial}")
             break
         else:
             if user_trial==no_trials:
                 print(f"no more trials!...you tried{user_trial} trials.")
                 print(f"the hidden number is {hidden}")
                 break
             elif guss<hidden:
                  print("no,increase!")
                
             else:
                 print("no,decrease!")
         continue      
             
                
#play again
def play_again():
    while True:
        play_again=int(input("play again? [0]No  [1]Yes"))
        if play_again in [0,1]:
           break
        else:
           print("invalid choice! please chooce 0 or 1  .")
    return play_again
    
#let's play
def play():
    show_levels()    
    while True:
        game_level=game_level_choice()
        limits,no_trials=setgame_setting(game_level)
        start_play(limits, no_trials)
        if not play_again():
             break
 
    
play()
    
 
    
 
    
 