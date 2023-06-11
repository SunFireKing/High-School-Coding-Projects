#Written in 9th grade for APCSP Create Preformance Task

#Import Random and Time and sys
import sys
import time
import random
#Create a List with all variables

cardvalues = {"ace": 1,
              2: 2,
              3: 3,
              4: 4,
              5: 5,
              6: 6,
              7: 7,
              8: 8,
              9: 9,
              10: 10,
              "jester": 10,
              "queen": 10, 
              "king": 10}

#Create variables to store money, wallet and bank
userwallet = 100
userbank = 0
#Create deposit function
def deposit(depositinput):
  global userbank, userwallet
  userbank += depositinput
  userwallet -= depositinput
  return userbank
#Create withdraw function
def withdraw(withdrawinput):
  global userbank, userwallet
  userwallet += withdrawinput
  userbank -= withdrawinput    
  return userwallet
  
#Create slowtype function
def slowtype(x):
  for i in x:
    print(i, end = "",flush = True)
    time.sleep(0.0001)
#Create hit Function that adds a card to user or dealer values 
def hit(cardvalues, values):
  keyvalue = random.choice(list(cardvalues))
  values[keyvalue] = cardvalues[keyvalue]
#Create dealcards function with selection for requirement
uservalues = {}
dealervalues = {}
def dealcards(cardvalues, values):
  global uservalues, dealervalues
  if values == "uservalues":
    for value in range(2):
        ukeyvalue = random.choice(list(cardvalues))
        uservalues[ukeyvalue] = cardvalues[ukeyvalue]
  elif values == "dealervalues":
    for value in range(2):
        dkeyvalue = random.choice(list(cardvalues))
        dealervalues[dkeyvalue] = cardvalues[dkeyvalue]
      
  
#Create blackjack Function incorporating the hit function and printing the values won or lost by the user
def blackjack(cardvalues, hit, dealcards):
  global userwallet, gambleinput, uservalues, dealervalues   
  print("___________________________________________________")
  dealcards(cardvalues, "uservalues")
  dealcards(cardvalues, "dealervalues")
  blackjack = False
  if "ace" in uservalues.keys():
    if sum(uservalues.values()) + 10 == 21:
      slowtype("BlackJack! You win {}\n".format(gambleinput * 1.5))
      blackjack = True
      userwallet += (gambleinput * 2.5)  
    if "ace" in dealervalues:
      if sum(dealervalues.values()) + 10 == 21:
        slowtype("BlackJack! \nThe dealer won{}\n".format(gambleinput * 1.5))
        userwallet -= gambleinput * 0.5
        blackjack = True
  if blackjack == True:
    hitstand = False
  elif blackjack == False:
    key = 0
    for card in dealervalues:
      if key == 0:
        slowtype("The dealer's open card is: {0}\n".format(card))
        key += 1
    slowtype("Your cards are: {0}\n".format(" and ".join(str(card) for card in uservalues.keys())))
    slowtype("Your currently have {0} points\n".format(sum(uservalues.values())))
    hitstand = True
  while hitstand == True:
    slowtype("Would you like to hit or stand?(hit/stand): ")
    continueinput = input()
    continueinput = continueinput.lower()
    if continueinput == "hit":
      hit(cardvalues, uservalues)
      if sum(dealervalues.values()) <= 16:
        hit(cardvalues, dealervalues)
      if sum(uservalues.values()) > 21:
        slowtype("You are BUST!\n")
        hitstand = False
      elif sum(uservalues.values()) == 21:
        slowtype("BLACKJACK! you get ${}\n".format(gambleinput * 1.5))
        userwallet += (gambleinput * 2.5)
        hitstand = False
      elif sum(uservalues.values()) < 21:    
        slowtype("Your cards are: {0}\n".format(" and ".join(str(card) for card in uservalues.keys())))
      #dealer values
      if sum(dealervalues.values()) > 21:
        slowtype("The dealer is BUST!\n")
        userwallet += (gambleinput * 2)
        hitstand = False
      elif sum(dealervalues.values()) == 21:
        slowtype("BLACKJACK! The dealer gets ${}\n".format(gambleinput * 1.5))
        userwallet -= gambleinput * 0.5
        hitstand = False
      elif sum(dealervalues.values()) < 21:
        if sum(uservalues.values()) >= 21:
          hitstand = False
        else:
          hitstand = True

        slowtype("Your currently have {0} points\n".format(sum(uservalues.values()))) 
    elif continueinput == "stand":
      dealerdraw = True
      while dealerdraw == True:
        if sum(dealervalues.values()) <= 16:
          hit(cardvalues, dealervalues)
          dealerdraw = True
        elif sum(dealervalues.values()) >= 17:
          dealerdraw = False
          if sum(dealervalues.values()) > 21:
            slowtype("The dealer is BUST! You get ${}\n".format(gambleinput * 1))  
            userwallet += (gambleinput * 2)
            hitstand = False
          elif sum(dealervalues.values()) == 21:
            slowtype("BLACKJACK! The dealer gets ${}\n".format(gambleinput * 1.5))
            userwallet -= gambleinput * 0.5
            hitstand = False
          elif sum(dealervalues.values()) < 21:
            if sum(dealervalues.values()) > sum(uservalues.values()):
              slowtype("The Dealer won ${0} becuase they had {1} point more than you\n".format(gambleinput, sum(dealervalues.values()) - sum(uservalues.values())))
              hitstand = False
            elif sum(dealervalues.values()) < sum(uservalues.values()):
              slowtype("You WON ${0} becuase the dealer had {1} points less than you\n".format(gambleinput, sum(uservalues.values()) - sum(dealervalues.values())))
              userwallet += (gambleinput * 2)
              hitstand = False
  uservalues = {}
  dealervalues = {}
              
              #Print: the user starts with 100 coins
repeat = True
while repeat == True:
  print("__________________________________________________")
  slowtype("You currently have ${0} in your wallet and ${1} in your bank\n".format(userwallet, userbank))
  if userwallet == 0 and userbank == 0:
    sys.exit("You have no money left")
  promptinput = slowtype("To play Blackjack press 1 \nTo deposit money into your bank press 2 \nTo withdraw money from the bank press 3 \nTo exit the program press 4: ")
  userinput = input()
  if userinput == "1":
    gambleamount = slowtype("How much would you like to gamble: ")
    gambleinput = int(input())
    if gambleinput <= userwallet and gambleinput > 0:    
      userwallet -= gambleinput
      blackjack(cardvalues, hit, dealcards)
    else:
      slowtype("Unable to gamble that amount\n")
      repeat = True
  elif userinput == "2":
    if userwallet > 0:
      depositamount = slowtype("how much would you like to deposit: ")
      depositinput = int(input())
      if depositinput <= userwallet and depositinput >= 0:
        deposit(depositinput)
      else:
        slowtype("Unable to withdraw this amount\n")
        repeat = True
    else:
      slowtype("You cannot deposit anymore money into the bank\n")
    repeat = True
  elif userinput == "3":
    if userbank > 0:
      withdrawamount = slowtype("how much would you like to withdraw: ")
      withdrawinput = int(input())
      if withdrawinput <= userbank and withdrawinput >= 0:
        withdraw(withdrawinput)
      else:
        slowtype("Unable to withdraw this amount\n")
        repeat = True
    else:
      slowtype("You cannot withdraw anymore money from the bank because your balance is $0 or have a negative value\n")
    repeat = True
  elif userinput == "4":
    sys.exit()
  else:
    repeat = True


  
  

    





