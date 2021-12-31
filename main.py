#step1 find a random number from game data (A)
#step 2 find another random number (B)
#step 3 ask the user to guess which among A or B is less - 
# if answer is wrong - game over else B becomes A and B is again found randomly and the whole process is repeated till the answer is correct - for each loop print whether right or wrong along with the current score
# Format - Compare A: Instagram, a Social media platform, from United States.

from game_data import data
from art import logo, vs
import random
from replit import clear

def print_compare(c1,c2):
  print("Compare A:", data[c1]['name'],",", "a ",data[c1]['description'],",", "from ", data[c1]['country'])
  score1 = data[c1]['follower_count']
  print(vs)
  print("Against B:", data[c2]['name'],",", "a ",data[c2]['description'],",", "from ", data[c2]['country'])
  score2 = data[c2]['follower_count']
  answer = input("Who has more followers? Type 'A' or 'B':").upper()
  if score1>score2:
    correct = 'A'
  else:
    correct = 'B'
  return(correct,answer)

def check(correct,answer, current_score):
  clear()
  if correct == answer:
    current_score +=1
    print(f"You're right! Current score: {current_score}. Game Continues..")
    return (1,current_score)
  else:
    print(f"Sorry, that's wrong. Final score: {current_score}. Game Ends!")
    return (0,current_score)

print(logo)
current_score = 0
contd =1
c1 = random.randint(0,49)
c2 = random.randint(0,49)
while c1 ==c2:
  c2 = random.randint(0,49)

while contd == 1:
  print(logo)
  correct, answer = print_compare(c1,c2)
  contd,crnt_scr = check(correct, answer, current_score)
  if correct == "A":
    c2 = random.randint(0,50)
    while c1 ==c2:
      c2 = random.randint(0,49)
  elif correct == 'B':
    c1 = random.randint(0,50)
    while c1 ==c2:
      c2 = random.randint(0,49)
  current_score = crnt_scr
  
