import replit 
import random
from hangmanscenes import stages,logo
from hangmanwords import word_list
lives = len(stages)-1
guesses = []
def display():
  global secret
  for i in secret:
    print(i,end=" ")

def check():
  global guess
  global guesses
  global lives 
  global secret
  if guess in secret or guess in guesses :
    print('Letter already guessed / Letter already in word')
  elif guess not in word:
    print('Incorrect Guess')
    print(stages[lives])
    lives = lives - 1
    print(f"{lives+1} lives are left")
  elif guess in word : 
    print('Correct guess !')
    for i in range(0,len(secret)):
      if word[i] == guess:
        secret[i] = guess
    for i in secret:
      print(i,end="")
  else : 
    print('Invalid')
playagain = True
gameon = True 
total = 0
score = 0
while playagain:
  guesses.clear()
  print(logo)
  word = random.choice(word_list)
  secret = []
  for i in word:
    if i in 'aeiou':
      secret.append(i)
    else:
      secret.append('_')
  display()
  print(f"\nYour word has {len(word)} letters")
  total+=1
  lives = len(stages)-1
  while gameon:
    if lives != -1 or '_' not in secret:
      guess = input("\nEnter guess : ")
      check()
      guesses.append(guess)
    else :
      print(f"\nThe word was {word}")
      if '_' not in secret:
        score+=1
      break
  choice = input('Play Again ? Y or N : ').upper()
  if choice == 'Y':
    replit.clear()
  else:
    replit.clear()
    print(f'Score : {score}/{total}')
    playagain = False
