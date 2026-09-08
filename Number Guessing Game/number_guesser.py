import random
import sys

top_of_range = input("Type a number: ");

if top_of_range.isdigit():
    top_of_range = int(top_of_range);
    if top_of_range<=0:
        print("Please type a number>0 next time.");
        sys.exit();
else:
    print("Please type a number next time.")
    sys.exit();

random_number = random.randint(0,top_of_range);
guess_count = 0;

while True:
    guess_count+=1
    user_guess=input("Make a guess");
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("Please type a number");
        continue;
    
    if user_guess==random_number :
        print("You got it correct")
        break;
    elif user_guess>random_number:
        print("Your were above number.");
    else:
        print("You were below number.")

print("You got it in ", guess_count ,(" guesses"));