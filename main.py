print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

turn = input('There is a crossroad. Where do you want to go? Type "left" to go left or "right" to go right. ').lower()
if turn=="left":
  lake = input('There is a lake. What do you want to do? Type "swim" to swim or "wait" to wait. ').lower()
  if lake == "wait":
    door = input('There are 3 doors: Red, Yellow and Blue. Which door do you choose? Type "red" for red door, "blue" for blue door or "yellow" for yellow door. ').lower()
    if door == "red":
      print("You were burned by fire! GAME OVER 💀")
    elif door == "blue":
      print("You were eaten by beasts! GAME OVER 💀")
    elif door == "yellow":
      print("YOU WINNNNNNNNN! 💰")
    else: 
      print("GAME OVER!💀")
    
  else: 
    print("You were attaked by trout. GAME OVER! 💀")

else:
  print("You fell into a hole. GAME OVER! 💀")
