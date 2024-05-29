import replit 
from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(choice,word,samt):
  global newtext 
  newtext =""
  samt = samt%26
  if choice == "decode":
    samt*=-1
  for i in word :
    if i == " ":
      newtext+=i
    else :
      position = alphabet.index(i)
      newtext+=alphabet[position+samt]
  print(f"\n{choice[0].upper() + choice[1:]}d word is ----> {repr(newtext)}") 
  
gameon = True 
while gameon:
  replit.clear()
  print(logo)
  print('Welcome to the CAESAR CIPHER !\n')
  choice = input("\n Write encode or decode : ")
  word = input(f" Enter word you want to {choice} : ")
  samt = int(input(" Enter the shift amount : "))
  cipher(choice,word,samt)
  again = input('Want to encode/decode another word? Y or N : ').upper()
  if again == "Y":
    continue
  else :
    break
  