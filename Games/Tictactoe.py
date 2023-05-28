import random
import os
import sys
thisdict = {
  0:"1",
  1:"2",
  2:"3",
  3:"4",
  4:"5",
  5:"6",
  6:"7",
  7:"8",
  8:"9"
}

class gameplay():
  def test_range(n):
    if n in gameplay.available_moves():
        return n
    else :
        again_2=input("Enter valid location:")
        m=gameplay.check(again_2)
        return m

  def check(user):
    try:
      abc=int(user)
      abc=gameplay.test_range(abc)
      return abc
    except:
      again=input("Enter valid location:")
      abcd=gameplay.check(again)
      return abcd

  def print_board_nums():
          for i in range(3):
              print(f"| {thisdict[i*3]} | {thisdict[(i*3)+1]} | {thisdict[(i*3)+2]} |")

  def user(role):
    user_input=input("Input move (1-9):\n")
    user_input=gameplay.check(user_input)
    thisdict[user_input-1]=role
    gameplay.print_board_nums()
    return user_input-1

  def computer(role_2):
    computer_input=random.choice(gameplay.available_moves())
    print("\nComputer's move\n",computer_input)
    thisdict[computer_input-1]=role_2
    gameplay.print_board_nums()
    return computer_input-1

  def available_moves():
    return [i+1 for i in thisdict.keys() if thisdict[i] == " "]

  def gamecheck(winner,place,who):
    list1=[thisdict[0],thisdict[1],thisdict[2]]
    list2=[thisdict[3],thisdict[4],thisdict[5]]
    list3=[thisdict[6],thisdict[7],thisdict[8]]
    check_list=[list1,list2,list3]
    vertical=0
    horizontal=0
    diagonal1=0
    diagonal2=0
    a=int(place/3)
    b=int(place%3)
    for j in range(3):
        if(check_list[a][j]==winner):
            horizontal+=1
    for j in range(3):
        if(check_list[j][b]==winner):
            vertical+=1
    for i in range(3):
        for j in range(3):
            if((i==j) and (i+j)==2 and check_list[i][j]==winner):
                diagonal1+=1
                diagonal2+=1
            elif(i==j and check_list[i][j]==winner):
                diagonal1+=1
            elif((i+j)==2 and check_list[i][j]==winner):
                diagonal2+=1
    if(horizontal==3 or vertical==3 or diagonal1==3 or diagonal2==3):
        if(who=="USER"):
            print("\nHoooyahh!!!! YOU WIN")
        else:
            print("\nBooo!!!!!! YOU LOST")
        sys.exit()
    else:
        return False









gameplay.print_board_nums()
role=input("Choose x or o\n")
role_2=""
while role is not 'x' and role is not 'o':
  print("\nPlease enter valid input\n")
  role=input("Choose x or o\n")
print("Let's Begin")
if role is 'x':
    role_2='o'
else:
    role_2='x'
for i in thisdict.keys():
    thisdict[i]=" "
for i in range(0,5):
    if(i==4):
        user_in=gameplay.user(role)
        final_chance=gameplay.gamecheck(role,user_in,"USER")
        if(final_chance is False):
            print("MATCH WAS DRAWN!!")
    elif i>=2:
        user_in=gameplay.user(role)
        gameplay.gamecheck(role,user_in,"USER")
        comp_in=gameplay.computer(role_2)
        gameplay.gamecheck(role_2,comp_in,"COMPUTER")
    else:
        gameplay.user(role)
        gameplay.computer(role_2)