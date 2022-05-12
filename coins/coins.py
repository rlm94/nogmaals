# name of student: Rudson
# number of student: 99066434
# purpose of program: counting coins
# function of program: giving back change
# structure of program: if/elif/else, operators, input, var,


toPay = int(float(input('Amount to pay: '))* 100) #bedrag te betalen invoeren
paid = int(float(input('Paid amount: ')) * 100)  #betaald bedrag invoeren
change = paid - toPay #nieuwe var met de waarde van betaald - te betalen

if change > 0: #als de change hoger dan 0 gaat het de begint de loop
  coinValue = 500 #startmunt van 5 euro
  
  while change > 0 and coinValue > 0:  #zijn beide statements true maak de var nrCoins
    nrCoins = change // coinValue #nieuwe var met de waarde van change delen door coinValue
    if coinValue >= 100:#hele euro munten
      if nrCoins > 0:
        print('return maximal ', int(nrCoins/10), ' coins of ', int(coinValue/100), ' euro!' ) #
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue/100) +  ' euro\'s did you return? ')) #
        change -= nrCoinsReturned * coinValue #
    else:#euro cents
      if nrCoins > 0:
        print('return maximal ', int(nrCoins/10), ' coins of ', int(coinValue), ' cents!' ) #
        nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
        change -= nrCoinsReturned * coinValue #




# comment on code below: new var added on all coin values
    if coinValue == 500:
      coinValue = 300
      change500 = nrCoinsReturned
    elif coinValue == 300:
      coinValue = 200
      change300 = nrCoinsReturned
    elif coinValue == 200:
      coinValue = 50
      change200 = nrCoinsReturned
    elif coinValue == 50:
      coinValue = 20
      change50 = nrCoinsReturned
    elif coinValue == 20:
      coinValue = 10
      change20 = nrCoinsReturned
    elif coinValue == 10:
      coinValue = 5
      change10 = nrCoinsReturned
    elif coinValue == 5:
      coinValue = 2
      change5 = nrCoinsReturned
    elif coinValue == 2:
      coinValue = 1
      change2 = nrCoinsReturned
    elif coinValue == 1:
      coinValue = 0
      change1 = nrCoinsReturned
 
#Printing result of the returned coins
if change > 0:     
  if change500 > 0:
    print("You returned ",(change500),"5.00 Euro's")
  if change300 > 0:
    print("You returned ",(change300),"3.00 Euro's")
  if change200 > 0:
    print("You returned ",(change200),"2.00 Euro's")
  if change50 > 0:
    print("You returned ",(change50),"0,50 Euro's cents")
  if change20 > 0:
    print("You returned ",(change20),"0,20 Euro's cents")
  if change10 > 0:
    print("You returned ",(change10),"0,10 Euro's cents")
  if change5 > 0:
    print("You returned ",(change5),"0,05 Euro's cents")
  if change2 > 0:
    print("You returned ",(change2),"0,02 Euro's cents")
  if change1 > 0:
    print("You returned ",(change1),"0,01 Euro's cents")
  print('Change not returned:', str(change) + ' cents')