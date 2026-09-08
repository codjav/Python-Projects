import random

user_wins = 0;
computer_wins = 0;
tie = 0;

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type rock/paper/scissor or Q to quit: ").lower()
    if user_input=="q":
        break;
    if user_input not in ["rock", "paper", "scisson"]:
        continue;
    
    rand_number = random.randint(0,2);
    # rock=0, paper=1, scissor=2
    computer_pick = options[rand_number];
    print("Computer Picked: ", computer_pick,"!");
    
    if (user_input=="rock" and computer_pick=="scissor") or (user_input=="paper" and computer_pick=="rock") or (user_input=="scissor" and computer_pick=="paper"):
        print("You won!")
        user_wins += 1
    elif user_input==computer_pick:
        print("Tie!")
        tie += 1;
    else :
        print("You lost!")
        computer_wins += 1;
    
print("You won", user_wins, "and Computer won", computer_wins, "and it got tie", tie, "times.")
print("Good Bye!")