import sys

print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ");
print(playing);

if playing.lower() !="yes": 
    sys.exit()

print("Okay! lets play: ")
score = 0;

answer = input("What does CPU stand for: ")
if answer.lower()=="central processing unit" :
    score += 1
    print("Correct!")
else:
    print("Wrong Answer!")
    
answer = input("What does GPU stand for?: ")
if answer.lower()=="graphics processing unit" :
    score += 1
    print("Correct!")
else:
    print("Wrong Answer!")

answer = input("What does RAM stand for: ")
if answer.lower()=="random access unit" :
    score += 1
    print("Correct!")
else:
    print("Wrong Answer!")
    
answer = input("What does PSU stand for: ")
if answer.lower()=="power supply unit" :
    score += 1
    print("Correct!")
else:
    print("Wrong Answer!")

print("You got "+ str(score) +" correct answers!")
print("You got "+ str((score/4)*100) +"% correct answers!")

