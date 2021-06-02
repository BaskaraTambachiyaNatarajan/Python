import random
def play():
  count=0
  numberofmatches=int(input("Enter the number of matches:"))
  for i in range(0,numberofmatches):
    user=input("'r' for rock, 's' for scissor, 'p' for paper")
    computer = random.choice(["r", "s", "p"])
    if user is computer:
      print("Opponent:",computer)
      print("Match was draw")
    elif user_win(user,computer):
      print("Opponent:",computer)
      print("You win")
      count+=1
    else:
      print("Opponent:",computer)
      print("You lose")
      count-=1
  return count
def user_win(user,computer):
  if (user=='p' and computer=='r') or (user=='r' and computer=='s') or (user=='s' and computer=='p'):
    return True

count=play()
if count>0:
  print("Hoooooyahhh!!!, You won the series")
elif count is 0:
  print("Series was drawn")
else:
  print("Booooooo!!!, YOU LOST!")