import random
from game_data import data
from art import logo,vs

print(logo)
score=0

#function to check score
def run(guess,score,hold): 
    if(guess==hold):
      score=score+1
      print(f"You are right current score is {score}")
      main(score)
    
    else:
      print(f"Sorry,that's wrong final score {score}")

#function to perform main task

def main(score):
  r1=random.randint(0,49)
  r2=random.randint(0,49)
  print(f"Compare A:{data[r1]['name']},a {data[r1]['description']},from {data[r1]['country']} ")
  print(vs)
  print(f"Compare A:{data[r2]['name']},a {data[r2]['description']},from {data[r2]['country']} ")
  guess=input("Who has more followers A or B:")
  def check(data):
    if(data[r1]['follower_count']>data[r2]['follower_count']):
      return 'A'
    else:
      return 'B'
  hold=check(data)
  run(guess,score,hold)
main(score)