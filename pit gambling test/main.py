from colorama import Fore, Style
from time import sleep
from random import randint

from NormalWell.sword import *
from NormalWell.bow import *
from NormalWell.pants import *

from JewelWell.sword import *
from JewelWell.bow import *
from JewelWell.pants import *

from lists import *
# print(Fore.RED + Style.BRIGHT + "----------------------------------------\nWARNING!" + Style.RESET_ALL + Style.DIM + " this is an outdated version. For the latest\nfeatures and bugfixes, go to my profile and use the\nlatest version.\n" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "----------------------------------------" + Style.RESET_ALL)
"""
Enchant sim v1.4 by SamLikesMemes

Keys:
  itemType: (1-3)
    1 = sword
    2 = bow
    3 = pants

  pantsColor: (0-4)
    0 = red
    1 = orange
    2 = yellow
    3 = green
    4 = blue

  infoCommand:
      0 = gold used
      1 = gems used
      2 = items enchanted to t3
      3 = rares gotten
      4 = artifacts gotten
      5 = overpowerds gotten
      6 = miraculouses gotten
      7 = bountifuls gotten
      8 = extraordinaries gotten
"""
"""
i = 3
while i < len(pantsList):
  j = 2
  while j < len(pantsList[i]):
    l = 0
    while l < len(pantsList[i][j]):
      print(pantsList[i][j][l] + "\n")
      l += 1
    j += 1
  i += 1"""

def messages(message):  # place to store long messages so main functions dont get too crowded
  if message == "updateMsg":
    return Fore.LIGHTYELLOW_EX + Style.BRIGHT + "PIT! " + Style.RESET_ALL + "Latest update: " + Fore.LIGHTYELLOW_EX + "v1.4.0" + Fore.GREEN + " Dark Mode " + Style.DIM + Fore.RESET + "[" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "Type \"changelog\"" + Style.DIM + Fore.RESET + "]\n" + Style.RESET_ALL
  elif message == "chooseType":
    return Style.DIM + "Choose an option by entering a number:\n1. " + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "Swords" + Style.RESET_ALL + Style.DIM + "\n2. " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Bows" + Style.RESET_ALL + Style.DIM + "\n3. " + Style.RESET_ALL + Fore.RED + "P" + Fore.YELLOW + "a" + Fore.LIGHTYELLOW_EX + "n" + Fore.GREEN + "t" + Fore.BLUE + "s" + Style.RESET_ALL + Style.DIM + "\n(press enter for random)" + Style.RESET_ALL
  elif message == "well":
    return Fore.LIGHTMAGENTA_EX + "Mystic Well\n\n" + Style.RESET_ALL + Style.DIM + "Find a" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " Mystic Bow" + Style.RESET_ALL + Style.DIM + ", " + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "Mystic Sword" + Style.RESET_ALL + Style.DIM + " or " + Style.RESET_ALL + Fore.RED + "P" + Fore.YELLOW + "a" + Fore.LIGHTYELLOW_EX + "n" + Fore.GREEN + "t" + Fore.BLUE + "s" + Style.RESET_ALL + Style.DIM + " from\nkilling players.\n\nEnchant these items in the well\nfor tons of buffs.\n\n" + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + "Choose an option by entering a number:\n" + Style.RESET_ALL
  elif message == "chooseWell":
    return Style.DIM + "1. " + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + "Normal Well" + Style.RESET_ALL + Style.DIM + "\n2. " + Style.RESET_ALL + Fore.CYAN + "Hidden Jewel Well" + Style.RESET_ALL + Style.DIM + "\n3. " + Style.RESET_ALL + Style.DIM + Fore.LIGHTRED_EX + "Rage Pants Well" + Style.RESET_ALL + Fore.RED + " (COMING SOON)" + Style.RESET_ALL


infoCommand = [0,0,0,0,0,0,0,0,0]
def startup(chooseType, chooseWell, itemsT3d):
  global infoCommand
  blankList = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
  # converting chooseType input to itemType
  if chooseType == "":
    itemType = randint(1, 3)
  else:
    itemType = int(chooseType)
  chooseWell = int(chooseWell)

  pantsColor = randint(0, 4)

  if chooseWell == 1:
    if itemType == 1:
      swordLore(0, 0, blankList)
    elif itemType == 2:
      bowLore(0, 0, blankList)
    elif itemType == 3:
      pantsLore(0, 0, pantsColor, blankList)
  elif chooseWell == 2:
    if itemType == 1:
      jewelSwordLore(0, 0, blankList)
    elif itemType == 2:
      jewelBowLore(0, 0, blankList)
    elif itemType == 3:
      jewelPantsLore(0, 0, pantsColor, blankList)


chooseWell = 0
print(messages("well"))
print(messages("chooseWell"))
while chooseWell != "1" and chooseWell != "2": #and chooseWell != "3":
  chooseWell = str(input())
print()


chooseType = 0
print(messages("updateMsg"))  # PIT! Latest update: v1.4 Update Name [Type "changelog"]
print(messages("chooseType"))  # Choose an option by entering a number:...
while chooseType != "" and chooseType != "1" and chooseType != "2" and chooseType != "3":
  chooseType = str(input())
print()

itemsT3d = 0
while True:
  startup(chooseType, chooseWell, itemsT3d)

  itemsT3d += 1


def info():
  """
    infoCommand:
      0 = gold used
      1 = gems used
      2 = items enchanted to t3
      3 = rares gotten
      4 = artifacts gotten
      5 = overpowerds gotten
      6 = miraculouses gotten
      7 = bountifuls gotten
      8 = legendaries gotten
      9 = total lives gotten
      10 = extraordinaries gotten
    """
  global infoCommand
  print(Fore.CYAN + "----------------------------\n" + Fore.YELLOW + "Resources:" + Style.RESET_ALL + "\n  Gold used: " + Fore.YELLOW + str(infoCommand[0]) + Style.RESET_ALL + "\n  Gems used: " + Fore.GREEN + str(infoCommand[1]) + Style.RESET_ALL + "\n  Items enchanted to T3: " + Fore.RED + str(infoCommand[2]) + Fore.LIGHTMAGENTA_EX + "\n\nMystic items:" + Style.RESET_ALL + "\n  Rares gotten: " + Fore.MAGENTA + str(infoCommand[3]) + Style.RESET_ALL + "\n  Artifacts gotten: " + Fore.GREEN + str(infoCommand[4]) + Style.RESET_ALL + "\n   ├─ Overpowerds gotten: " + Fore.GREEN + str(infoCommand[5]) + Style.RESET_ALL + "\n   └─ Miraculouses gotten: " + Fore.GREEN + str(infoCommand[6]) + Style.RESET_ALL + "\n  Bountifuls gotten: " + Fore.YELLOW + str(infoCommand[7]) + Style.RESET_ALL + "\n  Legendaries gotten: " + Fore.YELLOW + str(infoCommand[8]) + Style.RESET_ALL + "\n  Total lives created: " + Fore.GREEN + str(infoCommand[9]) + Style.RESET_ALL + "\n  Extraordinaries gotten: " + Fore.RED + str(infoCommand[10]) + Style.RESET_ALL + "\n\nRestarting the program will reset these stats." + Fore.CYAN + "\n----------------------------" + Style.RESET_ALL)