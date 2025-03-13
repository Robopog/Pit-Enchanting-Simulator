from colorama import Fore, Style

"""
list structure: 
  list[enchant type][enchant tier][enchant]

enchant types:
  0 = lame
  1 = resource
  2 = regular
  3 = rare

enchant tier:
  0 = tier 1
  1 = tier 2
  2 = tier 3

Sword list: line 21-318
Bow list: line 322-541
Pants list: line 543-
"""

swordList = [
  [
    [ # sword, lame, t1
      Fore.BLUE + "\nSharp\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +4% " + Style.RESET_ALL + Style.DIM + "meelee damage" + Style.RESET_ALL,

      Fore.BLUE + "\nBounty Reaper\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +7% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwith a bounty" + Style.RESET_ALL,

      Fore.BLUE + "\nDiamond Stomp\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +6% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwearing diamond armor" + Style.RESET_ALL,

      Fore.BLUE + "\nBeat the Spammers\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +10% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nholding a bow" + Style.RESET_ALL,

      Fore.BLUE + "\nPunisher\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +6% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nbelow 50% HP" + Style.RESET_ALL,

      Fore.BLUE + "\nKing Buster\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +7% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nabove 50% HP" + Style.RESET_ALL,

      Fore.BLUE + "\nPain Focus\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +1% " + Style.RESET_ALL + Style.DIM + "damage per" + Style.RESET_ALL + Fore.RED + " ❤\n" + Style.RESET_ALL + Style.DIM + "you're missing" + Style.RESET_ALL,

      Fore.BLUE + "\nGold and Boosted\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +5% " + Style.RESET_ALL + Style.DIM + "damage when you have\nabsorbtion hearts" + Style.RESET_ALL,

      Fore.BLUE + "\nGrasshopper\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +5% " + Style.RESET_ALL + Style.DIM + "damage when you or\nyour victim are standing on grass" + Style.RESET_ALL,

      Fore.BLUE + "\nShark\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +2% " + Style.RESET_ALL + Style.DIM + "damage per other\nplayers below" + Style.RESET_ALL + Fore.RED + " 6❤  " + Style.RESET_ALL + Style.DIM + "within 12\nblocks" + Style.RESET_ALL,

      Fore.BLUE + "\nFancy Raider\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +5% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwearing leather armor" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Damage\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "strike deals\n" + Style.RESET_ALL + Fore.RED + "+20% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL
      ], 
    [ # sword, lame, t2
      Fore.BLUE + "\nSharp II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +7% " + Style.RESET_ALL + Style.DIM + "meelee damage" + Style.RESET_ALL,

      Fore.BLUE + "\nBounty Reaper II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +15% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwith a bounty" + Style.RESET_ALL,

      Fore.BLUE + "\nDiamond Stomp II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +12% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwearing diamond armor" + Style.RESET_ALL,

      Fore.BLUE + "\nBeat the Spammers II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +25% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nholding a bow" + Style.RESET_ALL,

      Fore.BLUE + "\nPunisher II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +12% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nbelow 50% HP" + Style.RESET_ALL,

      Fore.BLUE + "\nKing Buster II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +13% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nabove 50% HP" + Style.RESET_ALL,

      Fore.BLUE + "\nPain Focus II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +2% " + Style.RESET_ALL + Style.DIM + "damage per" + Style.RESET_ALL + Fore.RED + " ❤\n" + Style.RESET_ALL + Style.DIM + "you're missing" + Style.RESET_ALL,

      Fore.BLUE + "\nGold and Boosted II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +9% " + Style.RESET_ALL + Style.DIM + "damage when you have\nabsorbtion hearts" + Style.RESET_ALL,

      Fore.BLUE + "\nGrasshopper II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +9% " + Style.RESET_ALL + Style.DIM + "damage when you or\nyour victim are standing on grass" + Style.RESET_ALL,

      Fore.BLUE + "\nShark II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +4% " + Style.RESET_ALL + Style.DIM + "damage per other\nplayers below" + Style.RESET_ALL + Fore.RED + " 6❤  " + Style.RESET_ALL + Style.DIM + "within 12\nblocks" + Style.RESET_ALL,

      Fore.BLUE + "\nFancy Raider II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +9% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwearing leather armor" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Damage II\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " third " + Style.RESET_ALL + Style.DIM + "strike deals\n" + Style.RESET_ALL + Fore.RED + "+30% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL
      ], 
    [ # sword, lame, t3
      Fore.BLUE + "\nSharp III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +12% " + Style.RESET_ALL + Style.DIM + "meelee damage" + Style.RESET_ALL,

      Fore.BLUE + "\nBounty Reaper III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +25% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwith a bounty" + Style.RESET_ALL,

      Fore.BLUE + "\nDiamond Stomp III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +25% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwearing diamond armor" + Style.RESET_ALL,

      Fore.BLUE + "\nBeat the Spammers III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +40% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nholding a bow" + Style.RESET_ALL,

      Fore.BLUE + "\nPunisher III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +18% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nbelow 50% HP" + Style.RESET_ALL,

      Fore.BLUE + "\nKing Buster III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +20% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nabove 50% HP" + Style.RESET_ALL,

      Fore.BLUE + "\nPain Focus III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +5% " + Style.RESET_ALL + Style.DIM + "damage per" + Style.RESET_ALL + Fore.RED + " ❤\n" + Style.RESET_ALL + Style.DIM + "you're missing" + Style.RESET_ALL,

      Fore.BLUE + "\nGold and Boosted III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +15% " + Style.RESET_ALL + Style.DIM + "damage when you have\nabsorbtion hearts" + Style.RESET_ALL,

      Fore.BLUE + "\nGrasshopper III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +15% " + Style.RESET_ALL + Style.DIM + "damage when you or\nyour victim are standing on grass" + Style.RESET_ALL,

      Fore.BLUE + "\nShark III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +7% " + Style.RESET_ALL + Style.DIM + "damage per other\nplayers below" + Style.RESET_ALL + Fore.RED + " 6❤  " + Style.RESET_ALL + Style.DIM + "within 12\nblocks" + Style.RESET_ALL,

      Fore.BLUE + "\nFancy Raider III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +16% " + Style.RESET_ALL + Style.DIM + "damage vs. players\nwearing leather armor" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Damage III\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " third " + Style.RESET_ALL + Style.DIM + "strike deals\n" + Style.RESET_ALL + Fore.RED + "+45% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL
      ]
    ],
  [
    [ # sword, resource, t1
      Fore.BLUE + "\nGold Bump\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +4g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +15% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +7g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +2 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +10% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +1g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +2g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: XP\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fifth " + Style.RESET_ALL + Style.DIM + "strike rewards\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+20 XP" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty\n" + Fore.LIGHTCYAN_EX + "+20% " + Style.RESET_ALL + Style.DIM + "XP from streak XP bonus" + Style.RESET_ALL,

      Fore.BLUE + "\nPitpocket\n" + Style.RESET_ALL + Style.DIM + "Steal" + Style.RESET_ALL + Fore.YELLOW + " 15g " + Style.RESET_ALL + Style.DIM + "on meelee hit (25s\ncooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +30% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL,

      Fore.BLUE + "\nSierra\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +30g " + Style.RESET_ALL + Style.DIM + "per" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " diamond\n" + Style.RESET_ALL + Style.DIM + "pieces your victims wear" + Style.RESET_ALL
      ], 
    [ # sword, resource, t2
      Fore.BLUE + "\nGold Bump II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +8g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +30% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +12g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +4 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +20% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +2g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +4g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: XP II\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fifth " + Style.RESET_ALL + Style.DIM + "strike rewards\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+28 XP" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty II\n" + Style.RESET_ALL + Style.DIM + "Earn " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+40% XP " + Style.RESET_ALL + Style.DIM + "from streak XP\nbonus and" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +50 max XP " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPitpocket II\n" + Style.RESET_ALL + Style.DIM + "Steal" + Style.RESET_ALL + Fore.YELLOW + " 20g " + Style.RESET_ALL + Style.DIM + "on meelee hit (20s\ncooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar II\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +60% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL,

      Fore.BLUE + "\nSierra II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +60g " + Style.RESET_ALL + Style.DIM + "per" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " diamond\n" + Style.RESET_ALL + Style.DIM + "pieces your victims wear" + Style.RESET_ALL
      ], 
    [ # sword, resource, t3
      Fore.BLUE + "\nGold Bump III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +12g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +45% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +18g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +6 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +30% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +3g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +6g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: XP III\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fifth " + Style.RESET_ALL + Style.DIM + "strike rewards\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+36 XP" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty III\n" + Style.RESET_ALL + Style.DIM + "Earn " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+60% XP " + Style.RESET_ALL + Style.DIM + "from streak XP\nbonus and" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +100 max XP " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPitpocket III\n" + Style.RESET_ALL + Style.DIM + "Steal" + Style.RESET_ALL + Fore.YELLOW + " 25g " + Style.RESET_ALL + Style.DIM + "on meelee hit (13s\ncooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar III\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +90% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL,

      Fore.BLUE + "\nSierra III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +90g " + Style.RESET_ALL + Style.DIM + "per" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " diamond\n" + Style.RESET_ALL + Style.DIM + "pieces your victims wear" + Style.RESET_ALL
      ]
    ],
  [
    [ # sword, regular, t1
      Fore.BLUE + "\nBruiser\n" + Style.RESET_ALL + Style.DIM + "Blocking with your sword reduces\nreceived damage by" + Style.RESET_ALL + Fore.RED + " 0.5❤ " + Style.RESET_ALL,

      Fore.BLUE + "\nBerserker\n" + Style.RESET_ALL + Style.DIM + "You can now critical hit on the\nground." + Style.RESET_ALL + Fore.GREEN + " 12% chance " + Style.RESET_ALL + Style.DIM + "to crit for\n" + Style.RESET_ALL + Fore.RED + "50% extra " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSpeedy Kill\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed I " + Style.RESET_ALL + Style.DIM + "(4s) on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCounter-Janitor\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Resistance I " + Style.RESET_ALL + Style.DIM + "(2s) on\nkill" + Style.RESET_ALL,

      Fore.BLUE + "\nGuts\n" + Style.RESET_ALL + Style.DIM + "Heal" + Style.RESET_ALL + Fore.RED + " 0.25❤  " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Heal\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "strike heals\n" + Style.RESET_ALL + Fore.RED + "0.4❤  " + Style.RESET_ALL + Style.DIM + "and grants " + Style.RESET_ALL + Fore.YELLOW + "0.4❤\n" + Style.RESET_ALL + Style.DIM + "absorbtion" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Swift\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "strike gain\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "Speed I" + Style.RESET_ALL + Style.DIM + " (3s)" + Style.RESET_ALL,

      Fore.BLUE + "\nCrush\n" + Style.RESET_ALL + Style.DIM + "Strikes apply" + Style.RESET_ALL + Fore.RED + " Weakness V\n" + Style.RESET_ALL + Style.DIM + "(lasts 0.2s, 2s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nLifesteal\n" + Style.RESET_ALL + Style.DIM + "Heal for" + Style.RESET_ALL + Fore.RED + " 4% " + Style.RESET_ALL + Style.DIM + "of damage dealt up\nto" + Style.RESET_ALL + Fore.RED + " 1.5❤" + Style.RESET_ALL,

      Fore.BLUE + "\nBullet Time\n" + Style.RESET_ALL + Style.DIM + "Blocking destroys arrows that hit\nyou" + Style.RESET_ALL,

      Fore.BLUE + "\nRevengeance\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +8% " + Style.RESET_ALL + Style.DIM + "damage vs. the last\nplayer who killed you" + Style.RESET_ALL,

      Fore.BLUE + "\nDuelist\n" + Style.RESET_ALL + Style.DIM + "Blocking two hits from the same\nplayer empowers your next strike\nagainst them for" + Style.RESET_ALL + Fore.RED + " +20% " + Style.RESET_ALL + Style.DIM + "damage\nand heals " + Style.RESET_ALL + Fore.RED + "0.5❤" + Style.RESET_ALL
      ], 
    [ # sword, regular, t2
      Fore.BLUE + "\nBruiser II\n" + Style.RESET_ALL + Style.DIM + "Blocking with your sword reduces\nreceived damage by" + Style.RESET_ALL + Fore.RED + " 1❤ " + Style.RESET_ALL,

      Fore.BLUE + "\nBerserker II\n" + Style.RESET_ALL + Style.DIM + "You can now critical hit on the\nground." + Style.RESET_ALL + Fore.GREEN + " 20% chance " + Style.RESET_ALL + Style.DIM + "to crit for\n" + Style.RESET_ALL + Fore.RED + "50% extra " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSpeedy Kill II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed I " + Style.RESET_ALL + Style.DIM + "(7s) on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCounter-Janitor II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Resistance I " + Style.RESET_ALL + Style.DIM + "(3s) on\nkill" + Style.RESET_ALL,

      Fore.BLUE + "\nGuts II\n" + Style.RESET_ALL + Style.DIM + "Heal" + Style.RESET_ALL + Fore.RED + " 0.5❤  " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Heal II\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "strike heals\n" + Style.RESET_ALL + Fore.RED + "0.8❤  " + Style.RESET_ALL + Style.DIM + "and grants " + Style.RESET_ALL + Fore.YELLOW + "0.8❤\n" + Style.RESET_ALL + Style.DIM + "absorbtion" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Swift II\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " third " + Style.RESET_ALL + Style.DIM + "strike gain\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "Speed II" + Style.RESET_ALL + Style.DIM + " (4s)" + Style.RESET_ALL,

      Fore.BLUE + "\nCrush II\n" + Style.RESET_ALL + Style.DIM + "Strikes apply" + Style.RESET_ALL + Fore.RED + " Weakness VI\n" + Style.RESET_ALL + Style.DIM + "(lasts 0.4s, 2s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nLifesteal II\n" + Style.RESET_ALL + Style.DIM + "Heal for" + Style.RESET_ALL + Fore.RED + " 8% " + Style.RESET_ALL + Style.DIM + "of damage dealt up\nto" + Style.RESET_ALL + Fore.RED + " 1.5❤" + Style.RESET_ALL,

      Fore.BLUE + "\nBullet Time II\n" + Style.RESET_ALL + Style.DIM + "Blocking destroys arrows hitting\nyou. Destroying arrows this way\nheals " + Style.RESET_ALL + Fore.RED + "1❤" + Style.RESET_ALL,

      Fore.BLUE + "\nRevengeance II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +15% " + Style.RESET_ALL + Style.DIM + "damage vs. the last\nplayer who killed you" + Style.RESET_ALL,

      Fore.BLUE + "\nDuelist II\n" + Style.RESET_ALL + Style.DIM + "Blocking two hits from the same\nplayer empowers your next strike\nagainst them for" + Style.RESET_ALL + Fore.RED + " +40% " + Style.RESET_ALL + Style.DIM + "damage\nand heals " + Style.RESET_ALL + Fore.RED + "1❤" + Style.RESET_ALL
      ], 
    [ # sword, regular, t3
      Fore.BLUE + "\nBruiser III\n" + Style.RESET_ALL + Style.DIM + "Blocking with your sword reduces\nreceived damage by" + Style.RESET_ALL + Fore.RED + " 2❤ " + Style.RESET_ALL,

      Fore.BLUE + "\nBerserker III\n" + Style.RESET_ALL + Style.DIM + "You can now critical hit on the\nground." + Style.RESET_ALL + Fore.GREEN + " 30% chance " + Style.RESET_ALL + Style.DIM + "to crit for\n" + Style.RESET_ALL + Fore.RED + "50% extra " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSpeedy Kill III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed I " + Style.RESET_ALL + Style.DIM + "(12s) on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCounter-Janitor III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Resistance I " + Style.RESET_ALL + Style.DIM + "(5s) on\nkill" + Style.RESET_ALL,

      Fore.BLUE + "\nGuts III\n" + Style.RESET_ALL + Style.DIM + "Heal" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Heal III\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "strike heals\n" + Style.RESET_ALL + Fore.RED + "1.2❤  " + Style.RESET_ALL + Style.DIM + "and grants " + Style.RESET_ALL + Fore.YELLOW + "1.2❤\n" + Style.RESET_ALL + Style.DIM + "absorbtion" + Style.RESET_ALL,

      Fore.BLUE + "\nCombo: Swift III\n" + Style.RESET_ALL + Style.DIM + "Every" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " third " + Style.RESET_ALL + Style.DIM + "strike gain\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "Speed II" + Style.RESET_ALL + Style.DIM + " (5s)" + Style.RESET_ALL,

      Fore.BLUE + "\nCrush III\n" + Style.RESET_ALL + Style.DIM + "Strikes apply" + Style.RESET_ALL + Fore.RED + " Weakness VII\n" + Style.RESET_ALL + Style.DIM + "(lasts 0.5s, 2s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nLifesteal III\n" + Style.RESET_ALL + Style.DIM + "Heal for" + Style.RESET_ALL + Fore.RED + " 13% " + Style.RESET_ALL + Style.DIM + "of damage dealt up\nto" + Style.RESET_ALL + Fore.RED + " 1.5❤" + Style.RESET_ALL,

      Fore.BLUE + "\nBullet Time III\n" + Style.RESET_ALL + Style.DIM + "Blocking destroys arrows hitting\nyou. Destroying arrows this way\nheals " + Style.RESET_ALL + Fore.RED + "1.5❤" + Style.RESET_ALL,

      Fore.BLUE + "\nRevengeance III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +25% " + Style.RESET_ALL + Style.DIM + "damage vs. the last\nplayer who killed you" + Style.RESET_ALL,

      Fore.BLUE + "\nDuelist III\n" + Style.RESET_ALL + Style.DIM + "Blocking two hits from the same\nplayer empowers your next strike\nagainst them for" + Style.RESET_ALL + Fore.RED + " +75% " + Style.RESET_ALL + Style.DIM + "damage\nand heals " + Style.RESET_ALL + Fore.RED + "1.5❤" + Style.RESET_ALL
      ]
    ],
  [
    [ # sword, rare, t1
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Knockback\n" + Style.RESET_ALL + Style.DIM + "Increases knockback taken by\nenemies by" + Style.RESET_ALL + " 3 blocks",

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Hemorrhage\n" + Style.RESET_ALL + Style.DIM + "Strikes bleed enemies for" + Style.RESET_ALL + Fore.RED + " 4s" + Style.RESET_ALL + Style.DIM + ",\nstopping them from gaining\n" + Style.RESET_ALL + Fore.YELLOW + "Absorbtion ❤  " + Style.RESET_ALL + Style.DIM + "and slowing them.\n(6s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Combo: Perun's Wrath\n" + Style.RESET_ALL + Style.DIM + "Each" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fifth " + Style.RESET_ALL + Style.DIM + "hit strikes\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "lightning " + Style.RESET_ALL + Style.DIM + "for " + Style.RESET_ALL + Fore.RED + "1.5❤" + Style.RESET_ALL + Style.DIM + ".\n(Lightning deals true damage)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Executioner\n" + Style.RESET_ALL + Style.DIM + "Hitting an enemy to below " + Style.RESET_ALL + Fore.RED + "1❤\n" + Style.RESET_ALL + Style.DIM + "instantly kills them" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Speedy Hit\n" + Style.RESET_ALL + Style.DIM + "Gain Speed I for" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 5s " + Style.RESET_ALL + Style.DIM + "on hit (3s\ncooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "The Punch\n" + Style.RESET_ALL + Style.DIM + "Hitting a player launches them up\nin the air (30s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Gamble\n" + Fore.MAGENTA + "50% chance " + Style.RESET_ALL + Style.DIM + "to deal" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "true\ndamage to whoever you hit, or to\nyourself" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Combo: Stun\n" + Style.RESET_ALL + Style.DIM + "The " + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "fifth " + Style.RESET_ALL + Style.DIM + "strike on an enemy\nstuns them for 0.5 seconds\n(Can only be stunned every 8s)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Billionaire\n" + Style.RESET_ALL + Style.DIM + "Hits with this swords deal " + Style.RESET_ALL + Fore.RED + "1.33x\ndamage " + Style.RESET_ALL + Style.DIM + "but cost " + Style.RESET_ALL + Fore.YELLOW + "100g" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Healer\n" + Style.RESET_ALL + Style.DIM + "Your hits " + Style.RESET_ALL + Fore.GREEN + "heal " + Style.RESET_ALL + Style.DIM + "you for" + Style.RESET_ALL + Fore.RED + " 0.5❤\n" + Style.RESET_ALL + Style.DIM + "and them for" + Style.RESET_ALL + Fore.RED + " 2❤ " + Style.RESET_ALL + Style.DIM + "(1s cd)" + Style.RESET_ALL
      ], 
    [ # sword, rare, t2
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Knockback II\n" + Style.RESET_ALL + Style.DIM + "Increases knockback taken by\nenemies by" + Style.RESET_ALL + " 6 blocks",

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Hemorrhage II\n" + Style.RESET_ALL + Style.DIM + "Strikes bleed enemies for" + Style.RESET_ALL + Fore.RED + " 4s" + Style.RESET_ALL + Style.DIM + ",\nstopping them from gaining\n" + Style.RESET_ALL + Fore.YELLOW + "Absorbtion ❤  " + Style.RESET_ALL + Style.DIM + "and slowing them.\n(4s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Combo: Perun's Wrath II\n" + Style.RESET_ALL + Style.DIM + "Each" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "hit strikes\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "lightning " + Style.RESET_ALL + Style.DIM + "for " + Style.RESET_ALL + Fore.RED + "2❤" + Style.RESET_ALL + Style.DIM + ".\n(Lightning deals true damage)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Executioner II\n" + Style.RESET_ALL + Style.DIM + "Hitting an enemy to below " + Style.RESET_ALL + Fore.RED + "1.5❤\n" + Style.RESET_ALL + Style.DIM + "instantly kills them" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Speedy Hit II\n" + Style.RESET_ALL + Style.DIM + "Gain Speed I for" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 7s " + Style.RESET_ALL + Style.DIM + "on hit (2s\ncooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "The Punch II\n" + Style.RESET_ALL + Style.DIM + "Hitting a player launches them up\nin the air (25s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Gamble II\n" + Fore.MAGENTA + "50% chance " + Style.RESET_ALL + Style.DIM + "to deal" + Style.RESET_ALL + Fore.RED + " 2❤  " + Style.RESET_ALL + Style.DIM + "true\ndamage to whoever you hit, or to\nyourself" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Combo: Stun II\n" + Style.RESET_ALL + Style.DIM + "The " + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "fifth " + Style.RESET_ALL + Style.DIM + "strike on an enemy\nstuns them for 0.8 seconds\n(Can only be stunned every 8s)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Billionaire II\n" + Style.RESET_ALL + Style.DIM + "Hits with this swords deal " + Style.RESET_ALL + Fore.RED + "1.67x\ndamage " + Style.RESET_ALL + Style.DIM + "but cost " + Style.RESET_ALL + Fore.YELLOW + "200g" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Healer II\n" + Style.RESET_ALL + Style.DIM + "Your hits " + Style.RESET_ALL + Fore.GREEN + "heal " + Style.RESET_ALL + Style.DIM + "you for" + Style.RESET_ALL + Fore.RED + " 0.75❤\n" + Style.RESET_ALL + Style.DIM + "and them for" + Style.RESET_ALL + Fore.RED + " 4❤ " + Style.RESET_ALL + Style.DIM + "(1s cd)" + Style.RESET_ALL
      ], 
    [ # sword, rare, t3
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Knockback III\n" + Style.RESET_ALL + Style.DIM + "Increases knockback taken by\nenemies by" + Style.RESET_ALL + " 9 blocks",

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Hemorrhage III\n" + Style.RESET_ALL + Style.DIM + "Strikes bleed enemies for" + Style.RESET_ALL + Fore.RED + " 5s" + Style.RESET_ALL + Style.DIM + ",\nstopping them from gaining\n" + Style.RESET_ALL + Fore.YELLOW + "Absorbtion ❤  " + Style.RESET_ALL + Style.DIM + "and slowing them.\n(2s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Combo: Perun's Wrath III\n" + Style.RESET_ALL + Style.DIM + "Each" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " fourth " + Style.RESET_ALL + Style.DIM + "hit strikes\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "lightning " + Style.RESET_ALL + Style.DIM + "for " + Style.RESET_ALL + Fore.RED + "1❤" + Style.RESET_ALL + Style.DIM + " + " + Style.RESET_ALL + Fore.RED + "1❤\n" + Style.RESET_ALL + Style.DIM + "per" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " diamond piece " + Style.RESET_ALL + Style.DIM + "on your\nvictim.\n(Lightning deals true damage)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Executioner III\n" + Style.RESET_ALL + Style.DIM + "Hitting an enemy to below " + Style.RESET_ALL + Fore.RED + "2❤\n" + Style.RESET_ALL + Style.DIM + "instantly kills them" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Speedy Hit III\n" + Style.RESET_ALL + Style.DIM + "Gain Speed I for" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 9s " + Style.RESET_ALL + Style.DIM + "on hit (1s\ncooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "The Punch III\n" + Style.RESET_ALL + Style.DIM + "Hitting a player launches them up\nin the air (20s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Gamble III\n" + Fore.MAGENTA + "50% chance " + Style.RESET_ALL + Style.DIM + "to deal" + Style.RESET_ALL + Fore.RED + " 3❤  " + Style.RESET_ALL + Style.DIM + "true\ndamage to whoever you hit, or to\nyourself" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Combo: Stun III\n" + Style.RESET_ALL + Style.DIM + "The " + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "fifth " + Style.RESET_ALL + Style.DIM + "strike on an enemy\nstuns them for 1.5 seconds" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Billionaire III\n" + Style.RESET_ALL + Style.DIM + "Hits with this swords deal " + Style.RESET_ALL + Fore.RED + "2x\ndamage " + Style.RESET_ALL + Style.DIM + "but cost " + Style.RESET_ALL + Fore.YELLOW + "350g" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Healer III\n" + Style.RESET_ALL + Style.DIM + "Your hits " + Style.RESET_ALL + Fore.GREEN + "heal " + Style.RESET_ALL + Style.DIM + "you for" + Style.RESET_ALL + Fore.RED + " 1❤\n" + Style.RESET_ALL + Style.DIM + "and them for" + Style.RESET_ALL + Fore.RED + " 5❤ " + Style.RESET_ALL + Style.DIM + "(1s cd)" + Style.RESET_ALL
      ]
    ]
]

bowList = [
  [
    [ # bow, lame, t1
      Fore.BLUE + "\nBottomless Quiver\n" + Style.RESET_ALL + Style.DIM + "Get" + Style.RESET_ALL + " 1 arrow " + Style.RESET_ALL + Style.DIM + "on arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nJumpspammer\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +10% " + Style.RESET_ALL + Style.DIM + "damage while midair\non arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nFletching\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +7% " + Style.RESET_ALL + Style.DIM + "bow damage" + Style.RESET_ALL,

      Fore.BLUE + "\nFirst Shot\n" + Style.RESET_ALL + Style.DIM + "First arrow hiy on a player deals\n" + Style.RESET_ALL + Fore.RED + "+10% damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSniper\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +9% " + Style.RESET_ALL + Style.DIM + "damage when shooting\nfrom over" + Style.RESET_ALL + " 24 " + Style.RESET_ALL + Style.DIM + "blocks" + Style.RESET_ALL,

      Fore.BLUE + "\nSpammer and Proud\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +9% " + Style.RESET_ALL + Style.DIM + "damage when shooting\nwithin" + Style.RESET_ALL + " 8 " + Style.RESET_ALL + Style.DIM + "blocks" + Style.RESET_ALL
      ], 
    [ # bow, lame, t2
      Fore.BLUE + "\nBottomless Quiver II\n" + Style.RESET_ALL + Style.DIM + "Get" + Style.RESET_ALL + " 3 arrows " + Style.RESET_ALL + Style.DIM + "on arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nJumpspammer II\n" + Style.RESET_ALL + Style.DIM + "While midair, your arrows deal\n" + Style.RESET_ALL + Fore.RED + "+16% " + Style.RESET_ALL + Style.DIM + "damage. While midair,\nrecieve" + Style.RESET_ALL + Fore.BLUE + " -10% " + Style.RESET_ALL + Style.DIM + "damage from melee\nand ranged attacks" + Style.RESET_ALL,

      Fore.BLUE + "\nFletching II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +12% " + Style.RESET_ALL + Style.DIM + "bow damage" + Style.RESET_ALL,

      Fore.BLUE + "\nFirst Shot II\n" + Style.RESET_ALL + Style.DIM + "First arrow hiy on a player deals\n" + Style.RESET_ALL + Fore.RED + "+16% damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSniper II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +18% " + Style.RESET_ALL + Style.DIM + "damage when shooting\nfrom over" + Style.RESET_ALL + " 24 " + Style.RESET_ALL + Style.DIM + "blocks" + Style.RESET_ALL,

      Fore.BLUE + "\nSpammer and Proud II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +15% " + Style.RESET_ALL + Style.DIM + "damage when shooting\nwithin" + Style.RESET_ALL + " 8 " + Style.RESET_ALL + Style.DIM + "blocks" + Style.RESET_ALL
      ], 
    [ # bow, lame, t3
      Fore.BLUE + "\nBottomless Quiver III\n" + Style.RESET_ALL + Style.DIM + "Get" + Style.RESET_ALL + " 8 arrows " + Style.RESET_ALL + Style.DIM + "on arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nJumpspammer III\n" + Style.RESET_ALL + Style.DIM + "While midair, your arrows deal\n" + Style.RESET_ALL + Fore.RED + "+24% " + Style.RESET_ALL + Style.DIM + "damage. While midair,\nrecieve" + Style.RESET_ALL + Fore.BLUE + " -20% " + Style.RESET_ALL + Style.DIM + "damage from melee\nand ranged attacks" + Style.RESET_ALL,

      Fore.BLUE + "\nFletching III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +20% " + Style.RESET_ALL + Style.DIM + "bow damage" + Style.RESET_ALL,

      Fore.BLUE + "\nFirst Shot III\n" + Style.RESET_ALL + Style.DIM + "First arrow hiy on a player deals\n" + Style.RESET_ALL + Fore.RED + "+25% damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSniper III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +30% " + Style.RESET_ALL + Style.DIM + "damage when shooting\nfrom over" + Style.RESET_ALL + " 24 " + Style.RESET_ALL + Style.DIM + "blocks" + Style.RESET_ALL,

      Fore.BLUE + "\nSpammer and Proud III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " +21% " + Style.RESET_ALL + Style.DIM + "damage when shooting\nwithin" + Style.RESET_ALL + " 8 " + Style.RESET_ALL + Style.DIM + "blocks" + Style.RESET_ALL
      ]
    ],
  [
    [ # bow, resource, t1
      Fore.BLUE + "\nGold Bump\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +4g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +15% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +7g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +2 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +10% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +1g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +2g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty\n" + Fore.LIGHTCYAN_EX + "+20% " + Style.RESET_ALL + Style.DIM + "XP from streak XP bonus" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +30% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL
      ], 
    [ # bow, resource, t2
      Fore.BLUE + "\nGold Bump II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +8g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +30% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +12g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +4 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +20% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +2g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +4g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty II\n" + Style.RESET_ALL + Style.DIM + "Earn " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+40% XP " + Style.RESET_ALL + Style.DIM + "from streak XP\nbonus and" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +50 max XP " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar II\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +60% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL
      ], 
    [ # bow, resource, t3
      Fore.BLUE + "\nGold Bump III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +12g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +45% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +18g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +6 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +30% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +3g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +6g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty III\n" + Style.RESET_ALL + Style.DIM + "Earn " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+60% XP " + Style.RESET_ALL + Style.DIM + "from streak XP\nbonus and" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +100 max XP " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar III\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +90% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL
      ]
    ],
  [
    [ # bow, regular, t1
      Fore.BLUE + "\nArrow Armory\n" + Style.RESET_ALL + Style.DIM + "Deals" + Style.RESET_ALL + Fore.RED + " +12% " + Style.RESET_ALL + Style.DIM + "damage but uses" + Style.RESET_ALL + " 3\narrows " + Style.RESET_ALL + Style.DIM + "per shot, if available" + Style.RESET_ALL,

      Fore.BLUE + "\nPush comes to shove\n" + Style.RESET_ALL + Style.DIM + "Every 3rd shot on a player has\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Punch" + Style.RESET_ALL,

      Fore.BLUE + "\nParasite\n" + Style.RESET_ALL + Style.DIM + "Heal" + Style.RESET_ALL + Fore.RED + " 0.25❤  " + Style.RESET_ALL + Style.DIM + "on arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nFaster than their shadow\n" + Style.RESET_ALL + Style.DIM + "Hitting" + Style.RESET_ALL + " 3 " + Style.RESET_ALL + Style.DIM + "shots without\nmissing grants" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II " + Style.RESET_ALL + Style.DIM + "(4s)" + Style.RESET_ALL,

      Fore.BLUE + "\nWhat doesn't kill you\n" + Style.RESET_ALL + Style.DIM + "Shooting yourself heals you" + Style.RESET_ALL + Fore.RED + " 1.5❤  " + Style.RESET_ALL + Style.DIM + "\n(3s cd)" + Style.RESET_ALL,

      Fore.BLUE + "\nWasp\n" + Style.RESET_ALL + Style.DIM + "Apply" + Style.RESET_ALL + Fore.RED + " Weakness II " + Style.RESET_ALL + Style.DIM + "(6s) on hit" + Style.RESET_ALL,

      Fore.BLUE + "\nMixed Combat\n" + Style.RESET_ALL + Style.DIM + "Shooting an enemy empowers your\nnext melee strike against them for\n" + Style.RESET_ALL + Fore.RED + "+10% " + Style.RESET_ALL + Style.DIM + "extra damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSprint Drain\n" + Style.RESET_ALL + Style.DIM + "Arrow shots grant you" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed I\n" + Style.RESET_ALL + Style.DIM + "(3s)" + Style.RESET_ALL,

      Fore.BLUE + "\nChipping\n" + Style.RESET_ALL + Style.DIM + "Deals" + Style.RESET_ALL + Fore.RED + " 0.5❤  " + Style.RESET_ALL + Style.DIM + "extra true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nPin down\n" + Style.RESET_ALL + Style.DIM + "Fully charged shots pin the victim\ndown, preventing them from gaining\nSpeed and Jump Boost (3s)" + Style.RESET_ALL
      ], 
    [ # bow, regular, t2
      Fore.BLUE + "\nArrow Armory II\n" + Style.RESET_ALL + Style.DIM + "Deals" + Style.RESET_ALL + Fore.RED + " +25% " + Style.RESET_ALL + Style.DIM + "damage but uses" + Style.RESET_ALL + " 5\narrows " + Style.RESET_ALL + Style.DIM + "per shot, if available" + Style.RESET_ALL,

      Fore.BLUE + "\nPush comes to shove II\n" + Style.RESET_ALL + Style.DIM + "Every 3rd shot on a player has\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Punch V" + Style.RESET_ALL + Style.DIM + " and deals" + Style.RESET_ALL + Fore.RED + " +0.5❤\n" + Style.RESET_ALL + Style.DIM + "extra damage" + Style.RESET_ALL,

      Fore.BLUE + "\nParasite II\n" + Style.RESET_ALL + Style.DIM + "Heal" + Style.RESET_ALL + Fore.RED + " 0.5❤  " + Style.RESET_ALL + Style.DIM + "on arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nFaster than their shadow II\n" + Style.RESET_ALL + Style.DIM + "Hitting" + Style.RESET_ALL + " 2 " + Style.RESET_ALL + Style.DIM + "shots without\nmissing grants" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed III " + Style.RESET_ALL + Style.DIM + "(4s)" + Style.RESET_ALL,

      Fore.BLUE + "\nWhat doesn't kill you II\n" + Style.RESET_ALL + Style.DIM + "Shooting yourself heals you" + Style.RESET_ALL + Fore.RED + " 2.5❤  " + Style.RESET_ALL + Style.DIM + "\n(3s cd)" + Style.RESET_ALL,

      Fore.BLUE + "\nWasp II\n" + Style.RESET_ALL + Style.DIM + "Apply" + Style.RESET_ALL + Fore.RED + " Weakness III " + Style.RESET_ALL + Style.DIM + "(11s) on\nhit" + Style.RESET_ALL,

      Fore.BLUE + "\nMixed Combat II\n" + Style.RESET_ALL + Style.DIM + "Shooting an enemy empowers your\nnext melee strike against them for\n" + Style.RESET_ALL + Fore.RED + "+20% " + Style.RESET_ALL + Style.DIM + "extra damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSprint Drain II\n" + Style.RESET_ALL + Style.DIM + "Arrow shots grant you" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed I\n" + Style.RESET_ALL + Style.DIM + "(5s) and apply " + Style.RESET_ALL + Fore.BLUE + "Slowness I\n" + Style.RESET_ALL + Style.DIM + "(3s)" + Style.RESET_ALL,

      Fore.BLUE + "\nChipping II\n" + Style.RESET_ALL + Style.DIM + "Deals" + Style.RESET_ALL + Fore.RED + " 1.0❤  " + Style.RESET_ALL + Style.DIM + "extra true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nPin down II\n" + Style.RESET_ALL + Style.DIM + "Fully charged shots pin the victim\ndown, preventing them from gaining\nSpeed and Jump Boost (5s)" + Style.RESET_ALL
      ], 
    [ # bow, regular, t3
      Fore.BLUE + "\nArrow Armory III\n" + Style.RESET_ALL + Style.DIM + "Deals" + Style.RESET_ALL + Fore.RED + " +60% " + Style.RESET_ALL + Style.DIM + "damage but uses" + Style.RESET_ALL + " 8\narrows " + Style.RESET_ALL + Style.DIM + "per shot, if available" + Style.RESET_ALL,

      Fore.BLUE + "\nPush comes to shove III\n" + Style.RESET_ALL + Style.DIM + "Every 3rd shot on a player has\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Punch VII" + Style.RESET_ALL + Style.DIM + " and deals" + Style.RESET_ALL + Fore.RED + " +1❤\n" + Style.RESET_ALL + Style.DIM + "extra damage" + Style.RESET_ALL,

      Fore.BLUE + "\nParasite III\n" + Style.RESET_ALL + Style.DIM + "Heal" + Style.RESET_ALL + Fore.RED + " 1.0❤  " + Style.RESET_ALL + Style.DIM + "on arrow hit" + Style.RESET_ALL,

      Fore.BLUE + "\nFaster than their shadow III\n" + Style.RESET_ALL + Style.DIM + "Hitting" + Style.RESET_ALL + " 2 " + Style.RESET_ALL + Style.DIM + "shots without\nmissing grants" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed IV " + Style.RESET_ALL + Style.DIM + "(4s)" + Style.RESET_ALL,

      Fore.BLUE + "\nWhat doesn't kill you III\n" + Style.RESET_ALL + Style.DIM + "Shooting yourself heals you" + Style.RESET_ALL + Fore.RED + " 3.5❤  " + Style.RESET_ALL,

      Fore.BLUE + "\nWasp III\n" + Style.RESET_ALL + Style.DIM + "Apply" + Style.RESET_ALL + Fore.RED + " Weakness IV " + Style.RESET_ALL + Style.DIM + "(16s) on hit" + Style.RESET_ALL,

      Fore.BLUE + "\nMixed Combat III\n" + Style.RESET_ALL + Style.DIM + "Shooting an enemy empowers your\nnext melee strike against them for\n" + Style.RESET_ALL + Fore.RED + "+30% " + Style.RESET_ALL + Style.DIM + "extra damage" + Style.RESET_ALL,

      Fore.BLUE + "\nSprint Drain III\n" + Style.RESET_ALL + Style.DIM + "Arrow shots grant you" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II\n" + Style.RESET_ALL + Style.DIM + "(7s) and apply " + Style.RESET_ALL + Fore.BLUE + "Slowness I\n" + Style.RESET_ALL + Style.DIM + "(3s)" + Style.RESET_ALL,

      Fore.BLUE + "\nChipping III\n" + Style.RESET_ALL + Style.DIM + "Deals" + Style.RESET_ALL + Fore.RED + " 1.5❤  " + Style.RESET_ALL + Style.DIM + "extra true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nPin down III\n" + Style.RESET_ALL + Style.DIM + "Fully charged shots pin the victim\ndown, preventing them from gaining\nSpeed and Jump Boost (10s)" + Style.RESET_ALL
      ]
    ],
  [
    [ # bow, rare, t1
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Volley\n" + Style.RESET_ALL + Style.DIM + "Shoot" + Style.RESET_ALL + " 3 arrows " + Style.RESET_ALL + Style.DIM + "at once" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Mega Longbow\n" + Style.RESET_ALL + Style.DIM + "One shot per second, this bow is\nautomatically fully drawn and\ngrants" + Style.RESET_ALL + Fore.GREEN + " Jump Boost II " + Style.RESET_ALL + Style.DIM + "(2s)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Explosive\n" + Style.RESET_ALL + Style.DIM + "Arrows go POP! (5s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Pullbow\n" + Style.RESET_ALL + Style.DIM + "Hitting a player pulls them toward\nyou (8s cooldown per player)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "True Shot\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " 25% " + Style.RESET_ALL + Style.DIM + "of arrow damage as\ntrue damage (ignores armor)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Devil Chicks\n" + Style.RESET_ALL + Style.DIM + "Arrows spawn an explosive chicken" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Telebow\n" + Style.RESET_ALL + Style.DIM + "Sneak to shoot a teleportation\narrow (90s cooldown, -3s per\nbow hit)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Lucky Shot\n" + Fore.LIGHTYELLOW_EX + "2%" + Style.RESET_ALL + Style.DIM + " chance for a shot to deal\nquadruple damage" + Style.RESET_ALL
      ], 
    [ # bow, rare, t2
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Volley II\n" + Style.RESET_ALL + Style.DIM + "Shoot" + Style.RESET_ALL + " 4 arrows " + Style.RESET_ALL + Style.DIM + "at once" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Mega Longbow II\n" + Style.RESET_ALL + Style.DIM + "One shot per second, this bow is\nautomatically fully drawn and\ngrants" + Style.RESET_ALL + Fore.GREEN + " Jump Boost III " + Style.RESET_ALL + Style.DIM + "(2s)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Explosive II\n" + Style.RESET_ALL + Style.DIM + "Arrows go BOOM! (3s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Pullbow II\n" + Style.RESET_ALL + Style.DIM + "Hitting a player pulls them and\nnearby players toward you (8s\ncooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "True Shot II\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " 35% + 0.25❤ " + Style.RESET_ALL + Style.DIM + "of arrow\ndamage as true damage (ignores\narmor)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Devil Chicks II\n" + Style.RESET_ALL + Style.DIM + "Arrows spawn many explosive\nchickens" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Telebow II\n" + Style.RESET_ALL + Style.DIM + "Sneak to shoot a teleportation\narrow (45s cooldown, -3s per bow\nhit)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Lucky Shot II\n" + Fore.LIGHTYELLOW_EX + "5%" + Style.RESET_ALL + Style.DIM + " chance for a shot to deal\nquadruple damage" + Style.RESET_ALL
      ], 
    [
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Volley III\n" + Style.RESET_ALL + Style.DIM + "Shoot" + Style.RESET_ALL + " 5 arrows " + Style.RESET_ALL + Style.DIM + "at once" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Mega Longbow III\n" + Style.RESET_ALL + Style.DIM + "One shot per second, this bow is\nautomatically fully drawn and\ngrants" + Style.RESET_ALL + Fore.GREEN + " Jump Boost IV " + Style.RESET_ALL + Style.DIM + "(2s)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Explosive III\n" + Style.RESET_ALL + Style.DIM + "Arrows go BOOM! (5s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Pullbow III\n" + Style.RESET_ALL + Style.DIM + "Hitting a player pulls them and\nnearby players toward you (8s\ncooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "True Shot III\n" + Style.RESET_ALL + Style.DIM + "Deal" + Style.RESET_ALL + Fore.RED + " 45% + 0.5❤ " + Style.RESET_ALL + Style.DIM + "of arrow\ndamage as true damage (ignores\narmor)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Devil Chicks III\n" + Style.RESET_ALL + Style.DIM + "Arrows spawn too many explosive\nchickens" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Telebow III\n" + Style.RESET_ALL + Style.DIM + "Sneak to shoot a teleportation\narrow (20s cooldown, -3s per bow\nhit)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Lucky Shot III\n" + Fore.LIGHTYELLOW_EX + "10%" + Style.RESET_ALL + Style.DIM + " chance for a shot to deal\nquadruple damage" + Style.RESET_ALL
      ]
    ]
]

pantsList = [
  [
    [ # pants, lame, t1
      Fore.BLUE + "\nProtection\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -4% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nDiamond Allergy\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -10% " + Style.RESET_ALL + Style.DIM + "damage from\ndiamond weapons" + Style.RESET_ALL,

      Fore.BLUE + "\nRing Armor\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -20% " + Style.RESET_ALL + Style.DIM + "damage from\narrows" + Style.RESET_ALL,

      Fore.BLUE + "\nBilly\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -2% " + Style.RESET_ALL + Style.DIM + "damage per\n" + Style.RESET_ALL + Fore.YELLOW + "1,000g bounty" + Style.RESET_ALL,

      Fore.BLUE + "\n\"Not\" Gladiator\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -1% " + Style.RESET_ALL + Style.DIM + "damage per nearby\nplayer (max 10 players)" + Style.RESET_ALL,

      Fore.BLUE + "\nCricket\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -5% " + Style.RESET_ALL + Style.DIM + "damage when you or\nyour victims are standing on grass\n" + Style.RESET_ALL + Fore.GREEN + "Perma" + Fore.RED + " Regen I " + Fore.GREEN + "on grass!" + Style.RESET_ALL,

      Fore.BLUE + "\nMcSwimmer\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -25% " + Style.RESET_ALL + Style.DIM + "melee damage\nwhile swimming in water or lava" + Style.RESET_ALL,

      Fore.BLUE + "\nDavid and Goliath\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -15% " + Style.RESET_ALL + Style.DIM + "damage from\nplayers with a bounty" + Style.RESET_ALL
      ], 
    [ # pants, lame, t2
      Fore.BLUE + "\nProtection II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -6% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nDiamond Allergy II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -20% " + Style.RESET_ALL + Style.DIM + "damage from\ndiamond weapons" + Style.RESET_ALL,

      Fore.BLUE + "\nRing Armor II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -40% " + Style.RESET_ALL + Style.DIM + "damage from\narrows" + Style.RESET_ALL,

      Fore.BLUE + "\nBilly II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -3% " + Style.RESET_ALL + Style.DIM + "damage per\n" + Style.RESET_ALL + Fore.YELLOW + "1,000g bounty" + Style.RESET_ALL,

      Fore.BLUE + "\n\"Not\" Gladiator II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -1.5% " + Style.RESET_ALL + Style.DIM + "damage per nearby\nplayer (max 10 players)" + Style.RESET_ALL,

      Fore.BLUE + "\nCricket II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -7% " + Style.RESET_ALL + Style.DIM + "damage when you or\nyour victims are standing on grass\n" + Style.RESET_ALL + Fore.GREEN + "Perma" + Fore.RED + " Regen I " + Fore.GREEN + "on grass!" + Style.RESET_ALL,

      Fore.BLUE + "\nMcSwimmer II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -40% " + Style.RESET_ALL + Style.DIM + "melee damage\nwhile swimming in water or lava" + Style.RESET_ALL,

      Fore.BLUE + "\nDavid and Goliath II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -25% " + Style.RESET_ALL + Style.DIM + "damage from\nplayers with a bounty" + Style.RESET_ALL
      ], 
    [ # pants, lame, t3
      Fore.BLUE + "\nProtection III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -10% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nDiamond Allergy III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -30% " + Style.RESET_ALL + Style.DIM + "damage from\ndiamond weapons" + Style.RESET_ALL,

      Fore.BLUE + "\nRing Armor III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -60% " + Style.RESET_ALL + Style.DIM + "damage from\narrows" + Style.RESET_ALL,

      Fore.BLUE + "\nBilly III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -4% " + Style.RESET_ALL + Style.DIM + "damage per\n" + Style.RESET_ALL + Fore.YELLOW + "1,000g bounty" + Style.RESET_ALL,

      Fore.BLUE + "\n\"Not\" Gladiator III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -2% " + Style.RESET_ALL + Style.DIM + "damage per nearby\nplayer (max 10 players)" + Style.RESET_ALL,

      Fore.BLUE + "\nCricket III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -15% " + Style.RESET_ALL + Style.DIM + "damage when you\nor your victims are standing on\ngrass\n" + Style.RESET_ALL + Fore.GREEN + "Perma" + Fore.RED + " Regen I " + Fore.GREEN + "on grass!" + Style.RESET_ALL,

      Fore.BLUE + "\nMcSwimmer III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -60% " + Style.RESET_ALL + Style.DIM + "melee damage\nwhile swimming in water or lava" + Style.RESET_ALL,

      Fore.BLUE + "\nDavid and Goliath III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -40% " + Style.RESET_ALL + Style.DIM + "damage from\nplayers with a bounty" + Style.RESET_ALL
      ]
    ],
  [
    [ # pants, resource, t1
      Fore.BLUE + "\nPebble\n" + Style.RESET_ALL + Style.DIM + "Picked up gold rewards" + Style.RESET_ALL + Fore.YELLOW + " +10g",

      Fore.BLUE + "\nLodbrok\n" + Style.RESET_ALL + Style.DIM + "Increases the chance for armor\npieces to drop to 40% (normally\n30%)" + Style.RESET_ALL,

      Fore.BLUE + "\nPurple Gold\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.YELLOW + " +7g " + Style.RESET_ALL + Style.DIM + "from breaking\nobsidian" + Style.RESET_ALL,

      Fore.BLUE + "\nSelf-checkout\n" + Style.RESET_ALL + Style.DIM + "Upon reaching a" + Style.RESET_ALL + Fore.YELLOW + " 5,000g\n" + Style.RESET_ALL + Style.DIM + "bounty, clear it and gain\n" + Style.RESET_ALL + Fore.YELLOW + "+2,000g" + Style.RESET_ALL + Style.DIM + ". Consumes 1 life of\nthis item" + Style.RESET_ALL,

      Fore.BLUE + "\nNegotiator\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +30% gold " + Style.RESET_ALL + Style.DIM + "from contracts" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Bump\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +4g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +15% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +7g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +2 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +10% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +1g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +2g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty\n" + Fore.LIGHTCYAN_EX + "+20% " + Style.RESET_ALL + Style.DIM + "XP from streak XP bonus" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +30% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL
      ], 
    [ # pants, resource, t2
      Fore.BLUE + "\nPebble II\n" + Style.RESET_ALL + Style.DIM + "Picked up gold rewards" + Style.RESET_ALL + Fore.YELLOW + " +20g",

      Fore.BLUE + "\nLodbrok II\n" + Style.RESET_ALL + Style.DIM + "Increases the chance for armor\npieces to drop to 55% (normally\n30%)" + Style.RESET_ALL,

      Fore.BLUE + "\nPurple Gold II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.YELLOW + " +11g " + Style.RESET_ALL + Style.DIM + "and" + Style.RESET_ALL + Fore.RED + " Regen III\n" + Style.RESET_ALL + Style.DIM + "(2s) from breaking obsidian" + Style.RESET_ALL,

      Fore.BLUE + "\nSelf-checkout II\n" + Style.RESET_ALL + Style.DIM + "Upon reaching a" + Style.RESET_ALL + Fore.YELLOW + " 5,000g\n" + Style.RESET_ALL + Style.DIM + "bounty, clear it and gain\n" + Style.RESET_ALL + Fore.YELLOW + "+3,000g" + Style.RESET_ALL + Style.DIM + ". Consumes 1 life of\nthis item" + Style.RESET_ALL,

      Fore.BLUE + "\nNegotiator II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +60% gold " + Style.RESET_ALL + Style.DIM + "from contracts" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Bump II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +8g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +30% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +12g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +4 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +20% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +2g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich II\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +4g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty II\n" + Style.RESET_ALL + Style.DIM + "Earn " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+40% XP " + Style.RESET_ALL + Style.DIM + "from streak XP\nbonus and" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +50 max XP " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar II\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +60% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL
      ], 
    [ # pants, resource, t3
      Fore.BLUE + "\nPebble III\n" + Style.RESET_ALL + Style.DIM + "Picked up gold grants" + Style.RESET_ALL + Fore.YELLOW + " 1❤" + Style.RESET_ALL + Style.DIM + " and\nrewards" + Style.RESET_ALL + Fore.YELLOW + " +30g",

      Fore.BLUE + "\nLodbrok III\n" + Style.RESET_ALL + Style.DIM + "Increases the chance for armor\npieces to drop to 75% (normally\n30%)" + Style.RESET_ALL,

      Fore.BLUE + "\nPurple Gold III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.YELLOW + " +15g " + Style.RESET_ALL + Style.DIM + "and" + Style.RESET_ALL + Fore.RED + " Regen III\n" + Style.RESET_ALL + Style.DIM + "(3s) from breaking obsidian" + Style.RESET_ALL,

      Fore.BLUE + "\nSelf-checkout III\n" + Style.RESET_ALL + Style.DIM + "Upon reaching a" + Style.RESET_ALL + Fore.YELLOW + " 5,000g\n" + Style.RESET_ALL + Style.DIM + "bounty, clear it and gain\n" + Style.RESET_ALL + Fore.YELLOW + "+5,000g" + Style.RESET_ALL + Style.DIM + ". Consumes 1 life of\nthis item" + Style.RESET_ALL,

      Fore.BLUE + "\nNegotiator III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +100% gold " + Style.RESET_ALL + Style.DIM + "from contracts" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Bump III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +12g " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nGold Boost III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +45% gold (g) " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nMoctezuma III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +18g " + Style.RESET_ALL + Style.DIM + "in kill (assists excluded)" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Bump III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +6 XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nXP Boost III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +30% XP " + Style.RESET_ALL + Style.DIM + "from kills" + Style.RESET_ALL,

      Fore.BLUE + "\nStrike Gold III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +3g " + Style.RESET_ALL + Style.DIM + "per hit (1s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Rich III\n" + Style.RESET_ALL + Style.DIM + "Earn" + Style.RESET_ALL + Fore.YELLOW + " +6g " + Style.RESET_ALL + Style.DIM + "per critical strike" + Style.RESET_ALL,

      Fore.BLUE + "\nSweaty III\n" + Style.RESET_ALL + Style.DIM + "Earn " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+60% XP " + Style.RESET_ALL + Style.DIM + "from streak XP\nbonus and" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +100 max XP " + Style.RESET_ALL + Style.DIM + "per kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPants Radar III\n" + Style.RESET_ALL + Style.DIM + "Pants, golden swords and enchanted\nbows drop" + Style.RESET_ALL + Fore.MAGENTA + " +90% " + Style.RESET_ALL + Style.DIM + "more frequently" + Style.RESET_ALL
      ]
    ],
  [
    [ # pants, regular, t1
      Fore.BLUE + "\nEggs\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.GREEN + " 8 eggs" + Style.RESET_ALL + Style.DIM + ". Gain" + Style.RESET_ALL + Fore.GREEN + " +4\neggs " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPeroxide\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.RED + " Regen I " + Style.RESET_ALL + Style.DIM + "(5s) when hit" + Style.RESET_ALL,

      Fore.BLUE + "\nLast Stand\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.BLUE + " Resistance I " + Style.RESET_ALL + Style.DIM + "(3 seconds)\nwhen reaching" + Style.RESET_ALL + Fore.RED + " 3❤" + Style.RESET_ALL,

      Fore.BLUE + "\nRevitalize\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed I " + Style.RESET_ALL + Style.DIM + "(5s) and" + Style.RESET_ALL + Fore.RED + " Regen\nII " + Style.RESET_ALL + Style.DIM + "(3s) when reaching" + Style.RESET_ALL + Fore.RED + " 3❤\n" + Style.RESET_ALL + Style.DIM + "(45s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nGotta go fast\n" + Style.RESET_ALL + Style.DIM + "Move" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 4% faster " + Style.RESET_ALL + Style.DIM + "at all times" + Style.RESET_ALL,

      Fore.BLUE + "\nTNT\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.RED + " 1 TNT" + Style.RESET_ALL + Style.DIM + "." + Style.RESET_ALL + Fore.RED + " TNT\n" + Style.RESET_ALL + Style.DIM + "explodes after 1.5 seconds and\ndeals" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "in a 3 blocks radius.\nGain" + Style.RESET_ALL + Fore.RED + " +1 TNT " + Style.RESET_ALL + Style.DIM + "om kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCounter-Offensive\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II " + Style.RESET_ALL + Style.DIM + "(3s) when hit\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "4 times " + Style.RESET_ALL + Style.DIM + "by a player" + Style.RESET_ALL,

      Fore.BLUE + "\nHearts\n" + Style.RESET_ALL + Style.DIM + "Increase your max health by\n" + Style.RESET_ALL + Fore.RED + " 0.25❤" + Style.RESET_ALL,

      Fore.BLUE + "\nBoo-boo\n" + Style.RESET_ALL + Style.DIM + "Passively regain" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "every 5\nseconds" + Style.RESET_ALL,

      Fore.BLUE + "\nMirror\n" + Style.RESET_ALL + Style.DIM + "You are immune to true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nCreative\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + " 16 planks" + Style.RESET_ALL + Style.DIM + ". Wood\nremains for 30 seconds. Gain" + Style.RESET_ALL + " +6\nblocks " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPrick\n" + Style.RESET_ALL + Style.DIM + "Enemies hitting you recieve\n" + Style.RESET_ALL + Fore.RED + "0.25❤  " + Style.RESET_ALL + Style.DIM + "true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Funky\n" + Style.RESET_ALL + Style.DIM + "Critical hits against you deal\n" + Style.RESET_ALL + Fore.BLUE + "80% " + Style.RESET_ALL + Style.DIM + "of the damage they\nnormally would" + Style.RESET_ALL,

      Fore.BLUE + "\nHunt the Hunter\n" + Style.RESET_ALL + Style.DIM + "Players using the" + Style.RESET_ALL + Fore.YELLOW + " Bounty Hunter\n" + Style.RESET_ALL + Style.DIM + "perk only deal half their bonus\ndamage against you" + Style.RESET_ALL,

      Fore.BLUE + "\nExcess\n" + Style.RESET_ALL + Style.DIM + "Can hold" + Style.RESET_ALL + Fore.GREEN + " +1 healing " + Style.RESET_ALL + Style.DIM + "item" + Style.RESET_ALL,

      Fore.BLUE + "\nRespawn: Resistance\n" + Style.RESET_ALL + Style.DIM + "Respawn with" + Style.RESET_ALL + Fore.BLUE + " Resistance I\n" + Style.RESET_ALL + Style.DIM + "(20s)" + Style.RESET_ALL,

      Fore.BLUE + "\nRespawn: Absorption\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.YELLOW + " 5❤  " + Style.RESET_ALL + Style.DIM + "absorption" + Style.RESET_ALL,

      Fore.BLUE + "\nElectrolytes\n" + Style.RESET_ALL + Style.DIM + "If you have" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed " + Style.RESET_ALL + Style.DIM + "on kill, add\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "2 " + Style.RESET_ALL + Style.DIM + "seconds to its duration.\n(Halved for Speed II+, max 18s)" + Style.RESET_ALL,

      Fore.BLUE + "\nDanger Close\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed III " + Style.RESET_ALL + Style.DIM + "(3s) when\nreaching" + Style.RESET_ALL + Fore.RED + " 3❤ " + Style.RESET_ALL + Style.DIM + "(10s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nGolden Heart\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.YELLOW + " +0.5❤  " + Style.RESET_ALL + Style.DIM + "absorption on kill\n(max" + Style.RESET_ALL + Fore.YELLOW + " 4❤ " + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL,

      Fore.BLUE + "\nSteaks\n" + Style.RESET_ALL + Style.DIM + "Gain a" + Fore.GREEN + " steak " + Fore.RESET + "instead of golden\napples on kill." + Fore.GREEN + " Steaks " + Fore.RESET + "are\ntasty and have good fibers for\nyour muscles. Can hold up to 8\nsteaks" + Style.RESET_ALL
      ], 
    [ # pants, regular, t2
      Fore.BLUE + "\nEggs II\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.GREEN + " 8 eggs" + Style.RESET_ALL + Style.DIM + ". Gain" + Style.RESET_ALL + Fore.GREEN + " +8\neggs " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPeroxide II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.RED + " Regen I " + Style.RESET_ALL + Style.DIM + "(8s) when hit" + Style.RESET_ALL,

      Fore.BLUE + "\nLast Stand II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.BLUE + " Resistance II " + Style.RESET_ALL + Style.DIM + "(4 seconds)\nwhen reaching" + Style.RESET_ALL + Fore.RED + " 3❤" + Style.RESET_ALL,

      Fore.BLUE + "\nRevitalize II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II " + Style.RESET_ALL + Style.DIM + "(5s) and" + Style.RESET_ALL + Fore.RED + " Regen\nIII " + Style.RESET_ALL + Style.DIM + "(3s) when reaching" + Style.RESET_ALL + Fore.RED + " 3❤\n" + Style.RESET_ALL + Style.DIM + "(45s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nGotta go fast II\n" + Style.RESET_ALL + Style.DIM + "Move" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 10% faster " + Style.RESET_ALL + Style.DIM + "at all times" + Style.RESET_ALL,

      Fore.BLUE + "\nTNT II\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.RED + " 2 TNT" + Style.RESET_ALL + Style.DIM + "." + Style.RESET_ALL + Fore.RED + " TNT\n" + Style.RESET_ALL + Style.DIM + "explodes after 1.5 seconds and\ndeals" + Style.RESET_ALL + Fore.RED + " 1.5❤  " + Style.RESET_ALL + Style.DIM + "in a 3 blocks\nradius.\nGain" + Style.RESET_ALL + Fore.RED + " +1 TNT " + Style.RESET_ALL + Style.DIM + "om kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCounter-Offensive II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II " + Style.RESET_ALL + Style.DIM + "(5s) when hit\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "3 times " + Style.RESET_ALL + Style.DIM + "by a player" + Style.RESET_ALL,

      Fore.BLUE + "\nHearts II\n" + Style.RESET_ALL + Style.DIM + "Increase your max health by\n" + Style.RESET_ALL + Fore.RED + " 0.5❤" + Style.RESET_ALL,

      Fore.BLUE + "\nBoo-boo II\n" + Style.RESET_ALL + Style.DIM + "Passively regain" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "every 4\nseconds" + Style.RESET_ALL,

      Fore.BLUE + "\nMirror II\n" + Style.RESET_ALL + Style.DIM + "You are immune to true damage and\ninstead reflect" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 25% " + Style.RESET_ALL + Style.DIM + "of it to\nyour attacker" + Style.RESET_ALL,

      Fore.BLUE + "\nCreative II\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + " 32 planks" + Style.RESET_ALL + Style.DIM + ". Wood\nremains for 30 seconds. Gain" + Style.RESET_ALL + " +12\nblocks " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPrick II\n" + Style.RESET_ALL + Style.DIM + "Enemies hitting you recieve\n" + Style.RESET_ALL + Fore.RED + "0.375❤  " + Style.RESET_ALL + Style.DIM + "true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Funky II\n" + Style.RESET_ALL + Style.DIM + "Critical hits against you deal\n" + Style.RESET_ALL + Fore.BLUE + "65% " + Style.RESET_ALL + Style.DIM + "of the damage they\nnormally would and empower your\nnext strike for" + Style.RESET_ALL + Fore.RED + " +14% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nHunt the Hunter II\n" + Style.RESET_ALL + Style.DIM + "Players using the" + Style.RESET_ALL + Fore.YELLOW + " Bounty Hunter\n" + Style.RESET_ALL + Style.DIM + "perk do not deal bonus damage\nagainst you" + Style.RESET_ALL,

      Fore.BLUE + "\nExcess II\n" + Style.RESET_ALL + Style.DIM + "Can hold" + Style.RESET_ALL + Fore.GREEN + " +2 healing " + Style.RESET_ALL + Style.DIM + "item" + Style.RESET_ALL,

      Fore.BLUE + "\nRespawn: Resistance II\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.BLUE + " Resistance I " + Style.RESET_ALL + Style.DIM + "(30s)" + Style.RESET_ALL,

      Fore.BLUE + "\nRespawn: Absorption II\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.YELLOW + " 10❤  " + Style.RESET_ALL + Style.DIM + "absorption" + Style.RESET_ALL,

      Fore.BLUE + "\nElectrolytes II\n" + Style.RESET_ALL + Style.DIM + "If you have" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed " + Style.RESET_ALL + Style.DIM + "on kill, add\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "4 " + Style.RESET_ALL + Style.DIM + "seconds to its duration.\n(Halved for Speed II+, max 24s)" + Style.RESET_ALL,

      Fore.BLUE + "\nDanger Close II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed III " + Style.RESET_ALL + Style.DIM + "(6s) when\nreaching" + Style.RESET_ALL + Fore.RED + " 4❤ " + Style.RESET_ALL + Style.DIM + "(10s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nGolden Heart II\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.YELLOW + " +1❤  " + Style.RESET_ALL + Style.DIM + "absorption on kill\n(max" + Style.RESET_ALL + Fore.YELLOW + " 5❤ " + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL,

      Fore.BLUE + "\nSteaks II\n" + Style.RESET_ALL + Style.DIM + "Gain a" + Fore.GREEN + " steak " + Fore.RESET + "instead of golden\napples on kill." + Fore.GREEN + " Steaks " + Fore.RESET + "are\ntasty and have good fibers for\nyour muscles. Can hold up to 10\nsteaks" + Style.RESET_ALL
      ], 
    [ # pants, regular, t3
      Fore.BLUE + "\nEggs III\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.GREEN + " 16 eggs" + Style.RESET_ALL + Style.DIM + ". Gain" + Style.RESET_ALL + Fore.GREEN + " +16\neggs " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPeroxide III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.RED + " Regen II " + Style.RESET_ALL + Style.DIM + "(8s) when hit" + Style.RESET_ALL,

      Fore.BLUE + "\nLast Stand III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.BLUE + " Resistance III " + Style.RESET_ALL + Style.DIM + "(4\nseconds) when reaching" + Style.RESET_ALL + Fore.RED + " 3❤" + Style.RESET_ALL,

      Fore.BLUE + "\nRevitalize III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II " + Style.RESET_ALL + Style.DIM + "(7s) and" + Style.RESET_ALL + Fore.RED + " Regen\nIII " + Style.RESET_ALL + Style.DIM + "(5s) when reaching" + Style.RESET_ALL + Fore.RED + " 3❤\n" + Style.RESET_ALL + Style.DIM + "(45s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nGotta go fast III\n" + Style.RESET_ALL + Style.DIM + "Move" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 20% faster " + Style.RESET_ALL + Style.DIM + "at all times" + Style.RESET_ALL,

      Fore.BLUE + "\nTNT III\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.RED + " 3 TNT" + Style.RESET_ALL + Style.DIM + "." + Style.RESET_ALL + Fore.RED + " TNT\n" + Style.RESET_ALL + Style.DIM + "explodes after 1.5 seconds and\ndeals" + Style.RESET_ALL + Fore.RED + " 2❤  " + Style.RESET_ALL + Style.DIM + "in a 3 blocks radius.\nGain" + Style.RESET_ALL + Fore.RED + " +2 TNT " + Style.RESET_ALL + Style.DIM + "om kill" + Style.RESET_ALL,

      Fore.BLUE + "\nCounter-Offensive III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed II " + Style.RESET_ALL + Style.DIM + "(7s) when hit\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "2 times " + Style.RESET_ALL + Style.DIM + "by a player" + Style.RESET_ALL,

      Fore.BLUE + "\nHearts III\n" + Style.RESET_ALL + Style.DIM + "Increase your max health by\n" + Style.RESET_ALL + Fore.RED + "1❤" + Style.RESET_ALL,

      Fore.BLUE + "\nBoo-boo III\n" + Style.RESET_ALL + Style.DIM + "Passively regain" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "every 3\nseconds" + Style.RESET_ALL,

      Fore.BLUE + "\nMirror III\n" + Style.RESET_ALL + Style.DIM + "You are immune to true damage and\ninstead reflect" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 50% " + Style.RESET_ALL + Style.DIM + "of it to\nyour attacker" + Style.RESET_ALL,

      Fore.BLUE + "\nCreative III\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + " 48 planks" + Style.RESET_ALL + Style.DIM + ". Wood\nremains for 30 seconds. Gain" + Style.RESET_ALL + " +18\nblocks " + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.BLUE + "\nPrick III\n" + Style.RESET_ALL + Style.DIM + "Enemies hitting you recieve " + Style.RESET_ALL + Fore.RED + "0.5❤\n" + Style.RESET_ALL + Style.DIM + "true damage" + Style.RESET_ALL,

      Fore.BLUE + "\nCritically Funky III\n" + Style.RESET_ALL + Style.DIM + "Critical hits against you deal\n" + Style.RESET_ALL + Fore.BLUE + "50% " + Style.RESET_ALL + Style.DIM + "of the damage they\nnormally would and empower your\nnext strike for" + Style.RESET_ALL + Fore.RED + " +30% " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.BLUE + "\nHunt the Hunter III\n" + Style.RESET_ALL + Style.DIM + "Players using the" + Style.RESET_ALL + Fore.YELLOW + " Bounty Hunter\n" + Style.RESET_ALL + Style.DIM + "perk do not deal bonus damage\nagainst you and overall deal\n" + Style.RESET_ALL + Fore.BLUE + "-20% " + Style.RESET_ALL + Style.DIM + "damage to you" + Style.RESET_ALL,

      Fore.BLUE + "\nExcess III\n" + Style.RESET_ALL + Style.DIM + "Can hold" + Style.RESET_ALL + Fore.GREEN + " +3 healing " + Style.RESET_ALL + Style.DIM + "item" + Style.RESET_ALL,

      Fore.BLUE + "\nRespawn: Resistance III\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.BLUE + " Resistance II " + Style.RESET_ALL + Style.DIM + "(40s)" + Style.RESET_ALL,

      Fore.BLUE + "\nRespawn: Absorption III\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.YELLOW + " 15❤  " + Style.RESET_ALL + Style.DIM + "absorption" + Style.RESET_ALL,

      Fore.BLUE + "\nElectrolytes III\n" + Style.RESET_ALL + Style.DIM + "If you have" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed " + Style.RESET_ALL + Style.DIM + "on kill, add\n" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + "6 " + Style.RESET_ALL + Style.DIM + "seconds to its duration.\n(Halved for Speed II+, max 30s)" + Style.RESET_ALL,

      Fore.BLUE + "\nDanger Close III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " Speed III " + Style.RESET_ALL + Style.DIM + "(9s) when\nreaching" + Style.RESET_ALL + Fore.RED + " 4❤ " + Style.RESET_ALL + Style.DIM + "(10s cooldown)" + Style.RESET_ALL,

      Fore.BLUE + "\nGolden Heart III\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.YELLOW + " +2❤  " + Style.RESET_ALL + Style.DIM + "absorption on kill\n(max" + Style.RESET_ALL + Fore.YELLOW + " 6❤ " + Style.RESET_ALL + Style.DIM + ")" + Style.RESET_ALL,

      Fore.BLUE + "\nSteaks III\n" + Style.RESET_ALL + Style.DIM + "Gain a" + Fore.GREEN + " steak " + Fore.RESET + "instead of golden\napples on kill." + Fore.GREEN + " Steaks " + Fore.RESET + "are\ntasty and have good fibers for\nyour muscles. Can hold up to 12\nsteaks" + Style.RESET_ALL
      ]
    ],
  [
    [ # pants, rare, t1
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Snowballs\n" + Style.RESET_ALL + Style.DIM + "Spawn with " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "8 snowballs" + Style.RESET_ALL + Style.DIM + ". Gain\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+8 snowballs" + Style.RESET_ALL + Style.DIM + " on kill.\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Snowballs " + Style.RESET_ALL + Style.DIM + "apply Slowness I\n(3s) and deal" + Style.RESET_ALL + Fore.RED + " 1 " + Style.RESET_ALL + Style.DIM + "true damage\nafter" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " 5 " + Style.RESET_ALL + Style.DIM + "hits in a row" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Martyrdom\n" + Style.RESET_ALL + Style.DIM + "Leave a handful of" + Style.RESET_ALL + Fore.GREEN + " creepers\n" + Style.RESET_ALL + Style.DIM + "behind on death" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Wolf Pack\n" + Style.RESET_ALL + Style.DIM + "Spawn a" + Style.RESET_ALL + Fore.RED + " Wolf " + Style.RESET_ALL + Style.DIM + "every 4 kills.\nCan have up to" + Style.RESET_ALL + Fore.RED + " 5 " + Style.RESET_ALL + Style.DIM + "wolves at\nonce" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Snowmen Army\n" + Style.RESET_ALL + Style.DIM + "Spawn with " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "3 scoops" + Style.RESET_ALL + Style.DIM + ". Gain\n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "+1 scoop" + Style.RESET_ALL + Style.DIM + " on kill. Placing the scoop\nwill consume 3 of then to spawn a\nSnowman defending you for" + Style.RESET_ALL + Fore.GREEN + " 30\n" + Style.RESET_ALL + Style.DIM + "seconds. Can hold up to" + Style.RESET_ALL + Fore.GREEN + " 6\n" + Fore.LIGHTCYAN_EX + "scoops" + Style.RESET_ALL + Style.DIM + "." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Pit Blob\n" + Style.RESET_ALL + Style.DIM + "Kills respawn" + Style.RESET_ALL + Fore.GREEN + " The Blob" + Style.RESET_ALL + Style.DIM + ". This\nslimy pet will follow you around\nand kill your enemies." + Style.RESET_ALL + Fore.GREEN + " The Blob\n" + Style.RESET_ALL + Style.DIM + "grows and gains health for every\nenemy you kill." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Instaboom\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.RED + " 1 Instaboom TNT" + Style.RESET_ALL + Style.DIM + ". It\nexplodes instantly and deals\n" + Style.RESET_ALL + Fore.RED + "0.25❤  " + Style.RESET_ALL + Style.DIM + "to enemies in a 4 blocks\nradius. Gain" + Style.RESET_ALL + Fore.RED + " +1 Instaboom TNT\n" + Style.RESET_ALL + Style.DIM + "on kill" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Escape Pod\n" + Style.RESET_ALL + Style.DIM + "When hit below" + Style.RESET_ALL + Fore.RED + " 2 ❤ " + Style.RESET_ALL + Style.DIM + ", launch\ninto the air dealing" + Style.RESET_ALL + Fore.RED + " 1❤  " + Style.RESET_ALL + Style.DIM + "damage\nto nearby enemies and gaining\n" + Style.RESET_ALL + Fore.GREEN + "Regen II " + Style.RESET_ALL + Style.DIM + "(20s). Can launch\nonce per life." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Singularity\n" + Style.RESET_ALL + Style.DIM + "Hits you recieve deal at most" + Style.RESET_ALL + Fore.RED + " 3❤\n" + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Solitude\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -40% " + Style.RESET_ALL + Style.DIM + "damage when only\none other player is within 7\nblocks" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Phoenix\n" + Style.RESET_ALL + Style.DIM + "Lethal attacks against you consume\n" + Style.RESET_ALL + Fore.RED + "1 life " + Style.RESET_ALL + Style.DIM + "of this item. Instead\nof dying, regenerate to full\nhealth." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Gomraw's Heart\n" + Style.RESET_ALL + Style.DIM + "Regain all" + Style.RESET_ALL + Fore.RED + " ❤  " + Style.RESET_ALL + Style.DIM + "when out of\ncombat" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Divine Miracle\n" + Fore.LIGHTCYAN_EX + "15% chance " + Style.RESET_ALL + Style.DIM + "retain the lives on\nyour items on death" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Assassin\n" + Style.RESET_ALL + Style.DIM + "Sneaking teleports you behind\nplayers bowing you. (10s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Retro-Gravity Microcosm\n" + Style.RESET_ALL + Style.DIM + "When a player hits you from\nabove ground" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 3 times " + Style.RESET_ALL + Style.DIM + "in a row:\nYou heal" + Style.RESET_ALL + Fore.RED + " 1.25❤" + Style.RESET_ALL
      ], 
    [ # pants, rare, t2
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Snowballs II\n" + Style.RESET_ALL + Style.DIM + "Spawn with " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "8 snowballs" + Style.RESET_ALL + Style.DIM + ". Refill\non kill. " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Snowballs " + Style.RESET_ALL + Style.DIM + "apply\nSlowness I (4s) and deal" + Style.RESET_ALL + Fore.RED + " 1\n" + Style.RESET_ALL + Style.DIM + "true damage after" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " 4 " + Style.RESET_ALL + Style.DIM + "hits in\na row" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Martyrdom II\n" + Style.RESET_ALL + Style.DIM + "Leave lots of" + Style.RESET_ALL + Fore.GREEN + " creepers " + Style.RESET_ALL + Style.DIM + "behind\non death" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Wolf Pack II\n" + Style.RESET_ALL + Style.DIM + "Spawn a" + Style.RESET_ALL + Fore.RED + " Wolf " + Style.RESET_ALL + Style.DIM + "every 3 kills.\nCan have up to" + Style.RESET_ALL + Fore.RED + " 7 " + Style.RESET_ALL + Style.DIM + "wolves at\nonce" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Snowmen Army II\n" + Style.RESET_ALL + Style.DIM + "Spawn with " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "3 scoops" + Style.RESET_ALL + Style.DIM + ". Gain" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +2\nscoops" + Style.RESET_ALL + Style.DIM + " on kill. Placing the\nscoop will consume 3 of then to\nspawn a Snowman defending you for\n" + Style.RESET_ALL + Fore.GREEN + "60 " + Style.RESET_ALL + Style.DIM + "seconds. Can hold up to" + Style.RESET_ALL + Fore.GREEN + " 9\n" + Fore.LIGHTCYAN_EX + "scoops" + Style.RESET_ALL + Style.DIM + "." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Pit Blob II\n" + Style.RESET_ALL + Style.DIM + "Kills respawn" + Style.RESET_ALL + Fore.GREEN + " The Blob" + Style.RESET_ALL + Style.DIM + ". This\nslimy pet will follow you around\nand kill your enemies." + Style.RESET_ALL + Fore.GREEN + " The Blob\n" + Style.RESET_ALL + Style.DIM + "grows and gains health for every\nenemy you kill." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Instaboom II\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.RED + " 1 Instaboom TNT" + Style.RESET_ALL + Style.DIM + ". It\nexplodes instantly and deals\n" + Style.RESET_ALL + Fore.RED + "0.5❤  " + Style.RESET_ALL + Style.DIM + "to enemies in a 4 blocks\nradius. Gain" + Style.RESET_ALL + Fore.RED + " +2 Instaboom TNT\n" + Style.RESET_ALL + Style.DIM + "on kill\nConsecutive uses" + Style.RESET_ALL + Fore.RED + " hurt " + Style.RESET_ALL + Style.DIM + "you!" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Escape Pod II\n" + Style.RESET_ALL + Style.DIM + "When hit below" + Style.RESET_ALL + Fore.RED + " 2 ❤ " + Style.RESET_ALL + Style.DIM + ", launch\ninto the air dealing" + Style.RESET_ALL + Fore.RED + " 2❤  " + Style.RESET_ALL + Style.DIM + "damage\nto nearby enemies and gaining\n" + Style.RESET_ALL + Fore.GREEN + "Regen III " + Style.RESET_ALL + Style.DIM + "(25s). Can launch\nonce per life." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Singularity II\n" + Style.RESET_ALL + Style.DIM + "Hits you recieve deal at most" + Style.RESET_ALL + Fore.RED + "\n1.25❤ " + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Solitude II\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -50% " + Style.RESET_ALL + Style.DIM + "damage when two\nor less players are within 7\nblocks" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Phoenix II\n" + Style.RESET_ALL + Style.DIM + "Lethal attacks against you consume\n" + Style.RESET_ALL + Fore.RED + "1 life " + Style.RESET_ALL + Style.DIM + "of this item. Instead\nof dying, heal to" + Style.RESET_ALL + Fore.GREEN + " full HP " + Style.RESET_ALL + Style.DIM + "and\ngain a" + Style.RESET_ALL + Fore.RED + " +10% " + Style.RESET_ALL + Style.DIM + "damage (12s)\nbuff.\n(Can revive once per life)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Gomraw's Heart II\n" + Style.RESET_ALL + Style.DIM + "Regain all" + Style.RESET_ALL + Fore.RED + " ❤  " + Style.RESET_ALL + Style.DIM + "when out of\ncombat. Gain" + Style.RESET_ALL + Fore.RED + " Regen IV " + Style.RESET_ALL + Style.DIM + "(1s)\nwhen entering combat" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Divine Miracle II\n" + Fore.LIGHTCYAN_EX + "30% chance " + Style.RESET_ALL + Style.DIM + "retain the lives on\nyour items on death" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Assassin II\n" + Style.RESET_ALL + Style.DIM + "Sneaking teleports you behind your\nattacker. (5s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Retro-Gravity Microcosm II\n" + Style.RESET_ALL + Style.DIM + "When a player hits you from\nabove ground" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 3 times " + Style.RESET_ALL + Style.DIM + "in a row:\nYou heal" + Style.RESET_ALL + Fore.RED + " 1.25❤\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.RED + " +1.5❤ " + Style.RESET_ALL + Style.DIM + "damage vs them for 30s" + Style.RESET_ALL
      ], 
    [ # pants rare, t3
      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Snowballs III\n" + Style.RESET_ALL + Style.DIM + "Spawn with " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "16 snowballs" + Style.RESET_ALL + Style.DIM + ".\nRefill on kill. " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "Snowballs " + Style.RESET_ALL + Style.DIM + "apply\nSlowness I (5s) and deal\n" + Style.RESET_ALL + Fore.RED + "1 " + Style.RESET_ALL + Style.DIM + "true damage after" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " 3 " + Style.RESET_ALL + Style.DIM + "hits\nin a row" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Martyrdom III\n" + Style.RESET_ALL + Style.DIM + "Leave a ridiculous amount of\n" + Style.RESET_ALL + Fore.GREEN + "creepers " + Style.RESET_ALL + Style.DIM + "behind on death" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Wolf Pack III\n" + Style.RESET_ALL + Style.DIM + "Spawn a" + Style.RESET_ALL + Fore.RED + " Wolf " + Style.RESET_ALL + Style.DIM + "every 3 kills.\nCan have up to" + Style.RESET_ALL + Fore.RED + " 9 " + Style.RESET_ALL + Style.DIM + "wolves at\nonce" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Snowmen Army III\n" + Style.RESET_ALL + Style.DIM + "Spawn with " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "3 scoops" + Style.RESET_ALL + Style.DIM + ". Gain" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " +3\nscoops" + Style.RESET_ALL + Style.DIM + " on kill. Placing the\nscoop will consume 3 of then to\nspawn a Snowman defending you for\n" + Style.RESET_ALL + Fore.GREEN + "90 " + Style.RESET_ALL + Style.DIM + "seconds. Can hold up to\n" + Style.RESET_ALL + Fore.GREEN + "12 " + Fore.LIGHTCYAN_EX + "scoops" + Style.RESET_ALL + Style.DIM + "." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Pit Blob III\n" + Style.RESET_ALL + Style.DIM + "Kills respawn" + Style.RESET_ALL + Fore.GREEN + " The Blob" + Style.RESET_ALL + Style.DIM + ". This\nslimy pet will follow you around\nand kill your enemies." + Style.RESET_ALL + Fore.GREEN + " The Blob\n" + Style.RESET_ALL + Style.DIM + "grows and gains health for every\nenemy you kill." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Instaboom III\n" + Style.RESET_ALL + Style.DIM + "Spawn with" + Style.RESET_ALL + Fore.RED + " 2 Instaboom TNT" + Style.RESET_ALL + Style.DIM + ". It\nexplodes instantly and deals\n" + Style.RESET_ALL + Fore.RED + "0.75❤  " + Style.RESET_ALL + Style.DIM + "to enemies in a 4 blocks\nradius. Gain" + Style.RESET_ALL + Fore.RED + " +2 Instaboom TNT\n" + Style.RESET_ALL + Style.DIM + "on kill\nConsecutive uses" + Style.RESET_ALL + Fore.RED + " hurt " + Style.RESET_ALL + Style.DIM + "you!" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Escape Pod III\n" + Style.RESET_ALL + Style.DIM + "When hit below" + Style.RESET_ALL + Fore.RED + " 2 ❤ " + Style.RESET_ALL + Style.DIM + ", launch\ninto the air dealing" + Style.RESET_ALL + Fore.RED + " 3❤  " + Style.RESET_ALL + Style.DIM + "damage\nto nearby enemies and gaining\n" + Style.RESET_ALL + Fore.GREEN + "Regen IV " + Style.RESET_ALL + Style.DIM + "(30s). Can launch\nonce per life." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Singularity III\n" + Style.RESET_ALL + Style.DIM + "Hits you recieve deal at most" + Style.RESET_ALL + Fore.RED + " 1❤\n" + Style.RESET_ALL + Style.DIM + "damage" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Solitude III\n" + Style.RESET_ALL + Style.DIM + "Recieve" + Style.RESET_ALL + Fore.BLUE + " -60% " + Style.RESET_ALL + Style.DIM + "damage when two\nor less players are within 7\nblocks" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Phoenix III\n" + Style.RESET_ALL + Style.DIM + "Lethal attacks against you consume\n" + Style.RESET_ALL + Fore.RED + "1 life " + Style.RESET_ALL + Style.DIM + "of this item. Instead\nof dying, regenerate to full\nhealth and gain a stacking" + Style.RESET_ALL + Fore.RED + " +15%\n" + Style.RESET_ALL + Style.DIM + "damage (10s)\nbuff." + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Gomraw's Heart III\n" + Style.RESET_ALL + Style.DIM + "Regain all" + Style.RESET_ALL + Fore.RED + " ❤  " + Style.RESET_ALL + Style.DIM + "when out of\ncombat. Gain" + Style.RESET_ALL + Fore.RED + " Regen IV " + Style.RESET_ALL + Style.DIM + "(2s)\nwhen entering combat" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Divine Miracle III\n" + Fore.LIGHTCYAN_EX + "45% chance " + Style.RESET_ALL + Style.DIM + "retain the lives on\nyour items on death" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Assassin III\n" + Style.RESET_ALL + Style.DIM + "Sneaking teleports you behind your\nattacker. (3s cooldown)" + Style.RESET_ALL,

      Fore.MAGENTA + "\nRARE! " + Fore.BLUE + "Retro-Gravity Microcosm III\n" + Style.RESET_ALL + Style.DIM + "When a player hits you from\nabove ground" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " 3 times " + Style.RESET_ALL + Style.DIM + "in a row:\nYou heal" + Style.RESET_ALL + Fore.RED + " 1.25❤\n" + Style.RESET_ALL + Style.DIM + "Gain" + Style.RESET_ALL + Fore.RED + " +1.5❤ " + Style.RESET_ALL + Style.DIM + "damage vs them for 30s\nThey take" + Style.RESET_ALL + Fore.RED + " 0.5❤ " + Style.RESET_ALL + Style.DIM + "true damage" + Style.RESET_ALL
      ]
    ]
]