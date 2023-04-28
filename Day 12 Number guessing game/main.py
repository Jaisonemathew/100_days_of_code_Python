#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)

import random

# Number which I am thinking
num=random.randint(1,100)
print("I am Thinking of a number between 1 to 100")
print(f"The correct ans is {num}")
diff=input("choose a difficulty type 'easy' or 'hard':")
if diff=="easy":
  count=10
elif diff=="hard":
  count=5
else:
  print("Invalid difficulty")



def check(n,num):
  if num==n:
    return 0
  elif num<n:
    return 1
  elif num>n:
    return 2



def run(num,count): 
  while count:
    print(f"You have {count} attempts remaining to make a guess")
    guess=int(input("Make a guess:"))
    result=check(guess,num)
    if result==0:
      print(f"You got it right!{guess}")
      return 
    elif result==1:
      print("Too High")
    else:
      print("Too low")
    count=count-1
    if count==0:
      print("You run out of life you loose")
  

run(num,count)



