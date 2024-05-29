import random
import replit 
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def win(round):
    global pscore,cscore
    if pscore == max:
      return 'YOU'
    elif cscore == max:
      return 'COMPUTER'
    elif cchoice == pchoice:
      print(f'Round {round} : TIE')
    elif cchoice == 3 and pchoice == 2:
      cscore+=1
      print(f'Round {round} : YOU LOSE!')
    elif cchoice == 2 and pchoice == 3:
      pscore+=1
      print(f'Round {round} : YOU win!')
    elif pchoice == 1 and cchoice == 3:
      pscore+=1
      print(f'Round {round} : YOU WIN!')
    elif cchoice == 1 and pchoice == 3:
      cscore+=1
      print(f'Round {round} : YOU LOSE!')
    elif pchoice == 2 and cchoice == 1:
      pscore+=1
      print(f'Round {round} : YOU WIN!')
    elif cchoice == 2 and pchoice == 1:
      cscore+=1
      print(f'Round {round} : YOU LOSE!')
    else :
        print('Invalid')

rps = {1:'Rock', 2:'Paper', 3:'Scissor'}
levels = {1:1, 2:3, 3:5}
options = ['x', rock, paper, scissors]
again = True 
while again:
  print('Welcome to Rock - Paper - Scissors Game !')
  max = levels[int(input("Choose difficulty level : 1.Easy 2.Medium 3.Hard - "))]
  print(f"\nFirst to {max} points , wins the game !")
  gameon = True
  pscore = 0
  cscore = 0 
  round = 0
  pchoice = 0
  cchoice = 0
  print(f"---->  Player Score : {pscore} | Computer Score : {cscore}\n")
  while gameon: 
    round = round+1
    if pscore == max or cscore == max:
      winner = win(round)
      print(f"\n{winner} win(s) ROCK PAPER SCISSORS")
      print(f"Player Score : {pscore} | Computer Score : {cscore}")
      gameon = False 
      break
    else: 
      print(f"\nRound {round}")
      pchoice = int(input('Enter Choice : 1.Rock 2.Paper 3.Scissor - '))
      cchoice = random.randint(1,3)
      print(f'\nYou chose {rps[pchoice].upper()}')
      print(options[pchoice])
      print(f'Computer chose {rps[cchoice].upper()}')
      print(options[cchoice])
      time.sleep(2.75)
      replit.clear()
      win(round)
      print(f"---->  Player Score : {pscore} | Computer Score : {cscore}")
  play = input('\nPlay again? Y or N : ').upper()
  if play == "Y":
    gameon = True
    replit.clear()
  else :
    break