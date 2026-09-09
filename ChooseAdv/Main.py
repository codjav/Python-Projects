name = input("Type your name: ");

while True:
    print("Welcome", name, "on this adventure game! ");

    answer = input("You are on a dirt road, it has come to an end you can go left or right, Which way would you like to go?: ").lower();

    if answer=="left":
        answer = input("You come to a river, and you can walk around it or swim, Type walk to walk or swim to swim.").lower();
        if answer=="swim":
            print("You swam across, and got eaten by alligator!");
        elif answer =="walk":
            print("You walked many miles, and you got out of water, and end of game!")
        else:
            print("Not a valid answer, End of game!")
    elif answer=="right":
        answer = input("You come to a bridge it looks wobly, If you want to cross, type cross, or to walk back type back!").lower();
        if answer=="cross":
            answer = input("You reached a home, type food to ask for food, or type move to go further!").lower();
            if answer=="food":
                print("It is your home your mother identified you, So you won the game!");
            elif answer=="move":
                print("You ran out of food, So you lost the game!")
            else:
                print("Not a valid answer, End of game!");
        elif answer=="walk":
            print("You walked back to same spot where you started and got out of food so you lost the game");
        else:
            print("Not a valid answer, End of game!");
    else:
        print("Not a valid answer, End of game!")
    again = input("Type q to quit or p to play again!").lower();
    if again=="q":
        break;
    
print("Thank you for playing game!");