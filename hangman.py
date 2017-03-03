import random, re

letters = list("abcdefghijklmnopqrstuvwxyz")

# grab the word (and corresponding hint) from our words.txt file
f = open("words.txt",'r')
lines = f.readlines()
choice = random.randrange(1,len(lines)-1,2)
sel = lines[choice][:-1]
hint = lines[choice+1][:-1]
lives = 0
wordhide = list(re.sub(".","-",sel))
f.close()

# i am so sorry for this wall of ascii
manstate = [
  """
    =====|   
    |        
    |         
    |______   
   /|     /|  
  /______/ /  
  |______|/  
  """,
  """
    =====|
    |    0
    |    
    |______
   /|     /|
  /______/ /
  |______|/
  """,
  """
    =====|
    |    0
    |    |
    |______
   /|     /|
  /______/ /
  |______|/
  """,
  """
    =====|
    |    0
    |   /|
    |______
   /|     /|
  /______/ /
  |______|/
  """,
  """
    =====|
    |    0
    |   /|\\
    |______
   /|     /|
  /______/ /
  |______|/
  """,
  """
    =====|
    |    0
    |   /|\\
    |_____\\
   /|     /|
  /______/ /
  |______|/
  """,
  """
    =====|
    |    0
    |   /|\\
    |___/_\\
   /|     /|
  /______/ /
  |______|/
  """
  ]

def draw():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t"+hint+"\t\t"+manstate[lives])
  # FIXME: better console clearing
  if sel == "supercalifragilisticexpialidocious":
    print(''.join(wordhide))
  else:
    print('\t\t\t',''.join(wordhide))
  for i in range(26):
    print(letters[i],end=' ')
  print('\n')

def game(c):
  global lives
  if c in letters:
    letters[letters.index(c)] = '\\'
  else:
    print("You either have an invalid character, or you're using a letter that has been used already.")
    game(input())
  if c in sel:
    a = [i for i, x in enumerate(sel) if x == c]
    for i in a:
      wordhide[i] = sel[i]
  else:
    lives += 1
  draw()
  return wordhide, lives

def main():
  global lives
  global wordhide
  draw()
  while ''.join(wordhide) != sel:
    if lives >= 6:
      wordhide = sel;
      print("Your man got hung! For shame.")
      return
    game(input())
  print("You did it!")
  if lives == 0:
    print("Wow, flawlessly too! Good job.")
  return 0;

main()
