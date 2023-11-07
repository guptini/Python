import random
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path+"/valid-wordle-words.txt") as file:
    lines = [line.rstrip() for line in file]
randword=random.choice(lines)
atts =[]
aws=[]
def help():
  print('you have 6 attempts to guess a random 5 letter word. after you answer, you will see a code under the word. each digit represents the corresponding position in your guess. this is what they mean:\n0 - letter does not exist in word\n1 - letter exists in word, but its not in the correct spot\n2 - letter exists in word and is in the correct location')
for i in range(6):
  for i in atts:
    print(i+'\n'+aws[atts.index(i)]+'\n')
  ana=''
  uh=[]
  while True:
    guess=input('enter guess, or type "help" for information: ')
    if guess=='help':
      help()
    elif len(guess) != 5:
      print('please enter 5 letter word')
    elif guess not in lines:
      print('please enter a real valid word')
    else:
      break
  print(guess)
  if guess==randword:
    print('you got it!')
    break
  else:
    for i in range(len(list(guess))):
      if list(guess)[i] in list(randword) and uh.count(list(guess)[i]) != list(randword).count(list(guess)[i]):    
        if list(guess)[i]==list(randword)[i]:
          print(2,end='')
          ana += '2'
          uh.append(list(guess)[i])
        else:
          print(1, end='')
          ana+='1'
          uh.append(list(guess)[i])
      else:
        if i in list(randword):
          print(1, end='')
        else:
          print(0, end='')
        ana+='0'
  print('\n----------------')
  try:os.system('cls')
  except:pass
  atts.append(guess)
  aws.append(ana)
print('game over! ' + randword)