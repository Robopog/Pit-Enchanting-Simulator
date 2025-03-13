from colorama import Fore, Style
from time import sleep
from random import randint
from lists import *

"""
infoList structure:
  0 = enchant 1 index (list[][][HERE])
  1 = enchant 2 index (list[][][HERE])
  2 = enchant 3 index (list[][][HERE])

  3 = enchant 1 tokens (list[][HERE][])
  4 = enchant 2 tokens (list[][HERE][])
  5 = enchant 3 tokens (list[][HERE][])

  6 = enchant 1 type (list[HERE][][])
  7 = enchant 2 type (list[HERE][][])
  8 = enchant 3 type (list[HERE][][])

list structure: 
  list[enchant type][enchant tier][enchant]
"""

tiers = [
  "Mystic ",
  "Tier I ",
  "Tier II ",
  "Tier III "
]

def bowLore(tier, lives, infoList):
  global infoCommand
  # updates list
  if tier == 1:
    infoList = tier0_1(infoList)
    roll()
  elif tier == 2:
    infoList = tier1_2(infoList)
    roll()
  elif tier == 3:
    infoList = tier2_3(infoList)
    roll()

  # contatonate lore
  itemLore = ""
  if infoList[3] != -1:
    enchant1 = bowList[infoList[6]][infoList[3]][infoList[0]]
    itemLore += enchant1
  if infoList[4] != -1:
    enchant2 = bowList[infoList[7]][infoList[4]][infoList[1]]
    itemLore += "\n" + enchant2
  if infoList[5] != -1:
    enchant3 = bowList[infoList[8]][infoList[5]][infoList[2]]
    itemLore += "\n" + enchant3

  # prefix
  itemPrefix = prefix(infoList)

  # lives and artifact
  if tier == 1:
    lives += randint(3,6)
  elif tier == 2:
    lives += randint(4,7)
  elif tier == 3:
    lives += randint(7,15)
    artifact = randint(0,75)
    if artifact == 0:
      lives = 100
      itemPrefix = artifactPrefix(infoList)

  # prints everything
  if tier == 0:
    print(Fore.YELLOW + "Held item:" + Style.RESET_ALL + "\n----------------------------\n" + changeTierColor(tier) + itemPrefix + tiers[tier] + "Bow" + Style.DIM + Fore.RESET + "\nKept on death\n\nUsed in the mystic well" + Style.RESET_ALL + "\n----------------------------")
  else:
    print(Fore.YELLOW + "Held item:" + Style.RESET_ALL + "\n----------------------------\n" + changeTierColor(tier) + itemPrefix + tiers[tier] + "Bow" + Style.DIM + Fore.RESET + "\n" + "Lives: " + Style.RESET_ALL + Fore.GREEN + str(lives) + Style.DIM + Fore.RESET + "/" + str(lives) + Style.RESET_ALL + "\n" + itemLore + Style.RESET_ALL + "\n----------------------------")
  input1 = input(Fore.GREEN + "Press enter to continue\n" + Style.RESET_ALL)

  # gemming
  while tier != 3 and (input1 == "gem" or input1 == "g"):
    print(Fore.RED + "\nYou cannot gem this item!\n" + Style.RESET_ALL)
    input1 = input(Fore.GREEN + "Press enter to continue\n" + Style.RESET_ALL)
  if tier == 3 and (input1 == "gem" or input1 == "g"):
    gemmedEnchant = input(Style.DIM + "\nChoose an enchant to gem by entering a number:\n1. " + Style.RESET_ALL + get1stEnchant(infoList) + Style.DIM + "\n2. " + Style.RESET_ALL + get2ndEnchant(infoList) + Style.DIM + "\n3. " + Style.RESET_ALL + get3rdEnchant(infoList) + Style.DIM + "\n(enter \"cancel\" or \"c\" to cancel)\n" + Style.RESET_ALL)
    while fixGemmedEnchant(infoList, gemmedEnchant) == False:
      gemmedEnchant = input()
    if gemmedEnchant != "c" and gemmedEnchant != "cancel":
      print(gem(infoList, gemmedEnchant, tier, lives))
    input(Fore.GREEN + "Press enter to continue\n" + Style.RESET_ALL)

  # commands
  if input1 != "":
    commands(input1)


  # 
  if tier < 3:
    tier += 1
    bowLore(tier, lives, infoList)

def changeTierColor(tier):
  if tier == 0:
    return Fore.CYAN
  elif tier == 1:
    return Fore.GREEN
  elif tier == 2:
    return Fore.LIGHTYELLOW_EX
  elif tier == 3:
    return Fore.RED
  else:
    return Fore.MAGENTA

def roll():
  print("It's rollin'!")
  sleep(0.2)
  print("It's rollin'!\n")
  sleep(0.2)

def randomColor():
  return styleList[randint(0, len(styleList) - 1)] + colorList[randint(0, len(colorList) - 1)]

def tokens(infoList):
  return infoList[3] + infoList[4] + infoList[5] + 3
def numberEnchantType(infoList, eType):
  numberType = 0
  i = 6
  while i <= 8:
    if infoList[i] == eType:
      numberType += 1
    i += 1
  return numberType

def prefix(infoList):
  if tokens(infoList) >= 8: # legendary
    return "Legendary "

  if numberEnchantType(infoList, 1) == 3: # bountiful
    return "Bountiful "

  if numberEnchantType(infoList, 3) == 3: # unthinkable
    return "Unthinkable "

  if numberEnchantType(infoList, 3) == 2: # extraordinary
    return "Extraordinary "
  return ""
def artifactPrefix(infoList):
  if tokens(infoList) >= 7: # overpowered
    return "Overpowered "

  if numberEnchantType(infoList, 3) == 3: # one in a million
    return "One in a Million "

  if numberEnchantType(infoList, 3) == 2: # miraculous
    return "Miraculous "
  return "Artifact "

def get1stEnchant(infoList):
  if infoList[6] == 3:
    color = Fore.MAGENTA
  else:
    color = Fore.BLUE
  if infoList[3] != -1:
    return color + bowList[infoList[6]][infoList[3]][infoList[0]].split("\n")[1] + Style.RESET_ALL
  return Fore.RED + "✖" + Style.RESET_ALL
def get2ndEnchant(infoList):
  if infoList[7] == 3:
    color = Fore.MAGENTA
  else:
    color = Fore.BLUE
  if infoList[4] != -1:
    return color + bowList[infoList[7]][infoList[4]][infoList[1]].split("\n")[1] + Style.RESET_ALL
  return Fore.RED + "✖" + Style.RESET_ALL
def get3rdEnchant(infoList):
  if infoList[8] == 3:
    color = Fore.MAGENTA
  else:
    color = Fore.BLUE
  if infoList[5] != -1:
    return color + bowList[infoList[8]][infoList[5]][infoList[2]].split("\n")[1] + Style.RESET_ALL
  return Fore.RED + "✖" + Style.RESET_ALL

def gem(infoList, gemmedItem, tier, lives):
  gemmedItem = int(gemmedItem)
  infoList[gemmedItem + 2] += 1
  if infoList[5] == -1:
    target = 2
  elif infoList[5] != -1:
    target = 3
  infoList = reorderEnchants(infoList, gemmedItem, target)

  # contatonate lore
  itemLore = ""
  if infoList[3] != -1:
    enchant1 = bowList[infoList[6]][infoList[3]][infoList[0]]
    itemLore += enchant1
  if infoList[4] != -1:
    enchant2 = bowList[infoList[7]][infoList[4]][infoList[1]]
    itemLore += "\n" + enchant2
  if infoList[5] != -1:
    enchant3 = bowList[infoList[8]][infoList[5]][infoList[2]]
    itemLore += "\n" + enchant3

  # prefix
  itemPrefix = ""
  if lives == 100:
    itemPrefix = artifactPrefix(infoList)
  else:
    itemPrefix = prefix(infoList)

  # return everything
  return Fore.YELLOW + "\nHeld item:" + Style.RESET_ALL + "\n----------------------------\n" + changeTierColor(tier) + itemPrefix + tiers[tier] + "Bow" + Style.DIM + Fore.RESET + "\n" + "Lives: " + Style.RESET_ALL + Fore.GREEN + str(lives) + Style.DIM + Fore.RESET + "/" + str(lives) + Style.RESET_ALL + Fore.GREEN + " ♦️" + Style.RESET_ALL + "\n" + itemLore + Style.RESET_ALL + "\n----------------------------"

def fixGemmedEnchant(infoList, gemmedItem):
  if gemmedItem != "1" and gemmedItem != "2" and gemmedItem != "3" and gemmedItem != "c" and gemmedItem != "cancel":
    return False
  if gemmedItem != "c" and gemmedItem != "cancel":
    gemmedItem = int(gemmedItem)
  if gemmedItem == "c" or gemmedItem == "cancel":
    return True
  if infoList[gemmedItem + 5] == 3:
    return False
  if infoList[gemmedItem + 2] == -1 or infoList[gemmedItem + 2] == 2:
    return False
  if tokens(infoList) == 8:
    return False
  return True

def reorderEnchants(infoList, enchantMoved, target):
  infoList[enchantMoved - 1], infoList[target - 1] = infoList[target - 1], infoList[enchantMoved - 1]
  infoList[enchantMoved + 2], infoList[target + 2] = infoList[target + 2], infoList[enchantMoved + 2]
  infoList[enchantMoved + 5], infoList[target + 5] = infoList[target + 5], infoList[enchantMoved + 5]
  return infoList
  

def tier0_1(infoList):
  tokensAdded = randint(1,2) # randomize tokens added
  for i in range(tokensAdded): # loops for amount if tokens added
    if infoList[3] == -1: # if enchant 1 has 0 tokens
      enchantAddedTo = 1
    else:
      enchantAddedTo = randint(1,2) # randomize what enchant current token gets added token
    if infoList[enchantAddedTo + 5] == -1: # if enchant type hasn't been defined yet
      if infoList[6] == 1: # if 1st enchant is resource
        infoList[enchantAddedTo + 5] = 0 # define enchant as lame
      else:
        infoList[enchantAddedTo + 5] = randint(0,1) # define enchant type to lame or resource
    infoList[enchantAddedTo + 2] += 1 # add token to enchant

    if infoList[enchantAddedTo - 1] == -1: # if enchant hasnt been defined yet
      infoList[enchantAddedTo - 1] = randint(0, len(bowList[infoList[enchantAddedTo + 5]][infoList[enchantAddedTo + 2]]) - 1) # define enchant
      infoList = fixDupeEnchants(infoList, enchantAddedTo) # fix dupe enchants
  return infoList

def tier1_2(infoList):
  addRare = randint(0,10)
  tokensAdded = randint(1,2)
  if addRare != 0: # -===-dont add rare-===-
    for i in range(tokensAdded):
      if infoList[4] == -1: # find what enchant to add to
        enchantAddedTo = 2
      else:
        enchantAddedTo = randint(1,3)
      while infoList[enchantAddedTo + 2] == 2: # prevent 4 token enchants
        enchantAddedTo = randint(1,3)
      if infoList[enchantAddedTo + 5] == -1: # define enchant type (if appliccable)
        infoList[enchantAddedTo + 5] = randint(0,2)
      infoList[enchantAddedTo + 2] += 1 # add token

      if infoList[enchantAddedTo - 1] == -1: # if enchant hasnt been defined yet
        infoList[enchantAddedTo - 1] = randint(0, len(bowList[infoList[enchantAddedTo + 5]][infoList[enchantAddedTo + 2]]) - 1) # define enchant
        infoList = fixDupeEnchants(infoList, enchantAddedTo) # fix dupe enchants
  else: # -===-add rare-===-
    if infoList[4] == -1: # find what enchant to add to
      enchantAddedTo = 2
    else:
      enchantAddedTo = 3
    infoList[enchantAddedTo + 5] = 3 # define enchant type
    infoList[enchantAddedTo + 2] += 1 # add token

    if infoList[enchantAddedTo - 1] == -1: # if enchant hasnt been defined yet
        infoList[enchantAddedTo - 1] = randint(0, len(bowList[infoList[enchantAddedTo + 5]][infoList[enchantAddedTo + 2]]) - 1) # define enchant
        infoList = fixDupeEnchants(infoList, enchantAddedTo) # fix dupe enchants
  return infoList

def tier2_3(infoList):
  addRare = randint(0,10)
  rareTokensAdded = 0
  tokensAdded = randint(1,4)
  for i in range(tokensAdded):
    if tokens(infoList) <= 7: # prevents 9 token items
      if infoList[4] == -1: # find what enchant to add to
        enchantAddedTo = 2
      else:
        enchantAddedTo = randint(1,3)
      while infoList[enchantAddedTo + 2] == 2: # prevent 4 token enchants
        enchantAddedTo = randint(1,3)
      if infoList[enchantAddedTo + 5] == -1: # define enchant type (if appliccable)
        if addRare != 0:
          infoList[enchantAddedTo + 5] = randint(0,2)
        elif addRare == 0:
          infoList[enchantAddedTo + 5] = 3

      if infoList[enchantAddedTo + 5] == 3:
        rareTokensAdded += 1
      infoList[enchantAddedTo + 2] += 1 # add token
      if infoList[enchantAddedTo + 5] == 3 and rareTokensAdded > 3: # if enchant added to is rare and more than 3 rare tokens were added
        infoList[enchantAddedTo + 2] -= 1 # subtract token
      

      if infoList[enchantAddedTo - 1] == -1: # if enchant hasnt been defined yet
        infoList[enchantAddedTo - 1] = randint(0, len(bowList[infoList[enchantAddedTo + 5]][infoList[enchantAddedTo + 2]]) - 1) # define enchant
        infoList = fixDupeEnchants(infoList, enchantAddedTo) # fix dupe enchants
  return infoList

def fixDupeEnchants(infoList, enchantChecked):
  if enchantChecked == 1:
    while (infoList[0] == infoList[1] and infoList[6] == infoList[7]) or (infoList[0] == infoList[2] and infoList[6] == infoList[8]):
      infoList[0] = randint(0, len(bowList[infoList[6]][infoList[3]]) - 1)
  elif enchantChecked == 2:
    while (infoList[1] == infoList[0] and infoList[7] == infoList[6]) or (infoList[1] == infoList[2] and infoList[7] == infoList[8]):
      infoList[1] = randint(0, len(bowList[infoList[7]][infoList[4]]) - 1)
  elif enchantChecked == 3:
    while (infoList[2] == infoList[0] and infoList[8] == infoList[6]) or (infoList[2] == infoList[1] and infoList[8] == infoList[7]):
      infoList[2] = randint(0, len(bowList[infoList[8]][infoList[5]]) - 1)
  return infoList


def debug(infoList):
  typeList = [Fore.BLUE + "lame" + Style.RESET_ALL, Fore.YELLOW + "resource" + Style.RESET_ALL, Fore.RED + "regular" + Style.RESET_ALL, Fore.MAGENTA + "rare" + Style.RESET_ALL]
  print("[0] enchant 1 index: " + str(infoList[0]))
  print("[1] enchant 2 index: " + str(infoList[1]))
  print("[2] enchant 3 index: " + str(infoList[2]))
  print()
  print("[3] enchant 1 tokens: " + str(infoList[3]))
  print("[4] enchant 2 tokens: " + str(infoList[4]))
  print("[5] enchant 3 tokens: " + str(infoList[5]))
  print()
  print("[6] enchant 1 type: " + str(infoList[6]) + " (" + typeList[infoList[6]] + ")")
  print("[7] enchant 2 type: " + str(infoList[7]) + " (" + typeList[infoList[7]] + ")")
  print("[8] enchant 3 type: " + str(infoList[8]) + " (" + typeList[infoList[8]] + ")")

colorList = [
  Fore.BLACK,
  Fore.BLUE,
  Fore.CYAN,
  Fore.GREEN,
  Fore.LIGHTBLACK_EX,
  Fore.LIGHTBLUE_EX,
  Fore.LIGHTCYAN_EX,
  Fore.LIGHTGREEN_EX,
  Fore.LIGHTMAGENTA_EX,
  Fore.LIGHTRED_EX,
  Fore.LIGHTWHITE_EX,
  Fore.LIGHTYELLOW_EX,
  Fore.MAGENTA,
  Fore.RED,
  Fore.WHITE,
  Fore.YELLOW
]
styleList = [
  "",
  Style.DIM,
  "",
  Style.BRIGHT,
  ""
]

def commands(input1):
  global infoCommand
  while input1 == "changelog":
    print(Fore.CYAN + "----------------------------\n" + Style.RESET_ALL + "v1.4.0 changelog\n\nVisual:\n  - fresh swords and bows are now displayed\nas \"Mystic Sword\" and \"Mystic Bow\" instead\nof \"Fresh Sword\" and \"Fresh Bow\"\n  - made item lore realistic to pit\n  - made white enchant text grey\n  - new gemming GUI\n\nGameplay:\n  - merged normal sim and jewel sim into 1 program\n  - added jewel bows\n  - new algorithm for tiering up items\n  - gemming an items brings the gemmed\nenchant to the bottom\n  - the \"g\" command can be used to gem items\n  - got rid of recursion error that happens at 249\nitems enchanted\n\nBackend changed:\n  - completely re-coded program\n  - items are now tiered up randomly,\ninstead of being pre-generated\n\n----------------------------\nPlans for v1.4.1:\n  - add rage pants\n  - fix bugs discovered after release\n" + Fore.CYAN + "----------------------------" + Style.RESET_ALL)
    input1 = input(Fore.GREEN + "Press enter to continue\n" + Style.RESET_ALL)
  while input1 == "info":
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
    
    print(Fore.CYAN + "----------------------------\n" + Fore.RED + "This command is temporarily disabled." + Fore.CYAN + "\n----------------------------" + Style.RESET_ALL)
    input1 = input(Fore.GREEN + "Press enter to continue\n" + Style.RESET_ALL)
  while input1 == "help":
    print(Fore.CYAN + "----------------------------\n" + Style.RESET_ALL + "help ------- view this list\nchangelog -- view changes in the most recent update\ninfo ------- view stats for this session" + Fore.RED + " (temporarily\ndisabled)" + Style.RESET_ALL + "\ngem -------- upgrade an enchant on a tier 3 item\ng ---------- shortcut for \"gem\" command" + Fore.CYAN + "\n----------------------------" + Style.RESET_ALL)
    input1 = input(Fore.GREEN + "Press enter to continue\n" + Style.RESET_ALL)