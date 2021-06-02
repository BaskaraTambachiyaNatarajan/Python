import random
import os
from word import word

def hangman():
  difficulty=int(input("'1' for easy \n'2' for Medium\n'3' for Difficult\n"))
  question=get_valid_word(difficulty)
  global letters_in_question
  letters_in_question=set(question)
  print(f"Length of given word is: {len(question)}")
  global user_input
  user_input=set()
  count=6
  while len(letters_in_question)>0 and count>0:
    given_word=input("\nGuess a character: ").upper()
    os.system("cls")
    game=check(given_word,question)
    if game is False:
      count-=1
    user_input.add(given_word)
    word_list=live_letters(question)
    print("\nCurrent word is ",word_list)
    print(f"\nYou have {count} chances left and used these letters",user_input)
  if count is 0:
    print("\nOops!!! You dead, the answer is ",question)
  else:
    print("\nYou WIN!!!, the answer is ",question)

def live_letters(question):
  current_set=list()
  for i in question:
    if i in user_input:
      current_set.append(i)
    else:
      current_set.append("-")
  return current_set

def check(given_word,question):
  if given_word in user_input:
    print("You have already entered this value")
    return False
  elif given_word in letters_in_question:
    print("Correct")
    letters_in_question.remove(given_word)
    return True
  else:
    print("You have entered invalid character")
    return False
    

def get_valid_word(difficulty):
  word.sort(key = len)
  last=int((len(word)/3)*difficulty)
  first=int((difficulty-1)*(len(word)/3))
  w=word[first:last]
  question=random.choice(w).upper()
  while '-' in question or ' ' in question:
    question=random.choice(w).upper()
    print(question)
  return question


hangman()