from loading import loading
from random import randint
from datetime import datetime
import chessdotcom

#username= input("Please enter a Username: ")
#Refactor loop to make run faster if not found#
#Place Holder name#
username = "HomJob"
#username = "ziebz"

chars = ["1","2","3","4","5","6","7","8","9", "a", "b", "c", "d", "e", "f", "g", "h", "x", "B", "Q", "K", "R", "+", ]

Games = []
Nogames = []

x = chessdotcom.get_player_profile(username)

d = datetime.now()

maxyr = d.year
maxmnth = d.month

year = 2007

month = 4

while year != maxyr or month < maxmnth + 1:
    #When Month goes over 12 add 1 to go next year#
    if month == 13:
        month = 1
        year += 1
    #Reassign the chess variables for each month and year#
    usrgames = chessdotcom.get_player_games_by_month_pgn(username, year, month)
    usrgames = str(usrgames)

    

    #for z,x in enumerate(usrgames):
     #   if x not in chars:
      #      if x not in chars and usrgames[z+1] in chars:
       #         usrgames = usrgames.replace(x, " ")
        #        usrgames = usrgames.replace(usrgames[z+1], " ") 
         #   usrgames = usrgames.replace(x, " ")

    #If there are games then add to the game string to show there are games#
    if usrgames != "ChessDotComResponse(pgn=Collection(pgn=''))":
        
        Games.append(year)
        Games.append(month)
    #If the string is empty then add to the no games list#
    else:
        Nogames.append(year)
        Nogames.append(month)

    month += 1
    print(loading[randint(0,len(loading)-1)])

i = 0

print("Games found on: ")
for z in range(int((len(Games))/2)): 
    print(Games[i], Games[i+1])
    i += 2

z = 0
i = 0

print("No games found on: ") 
for z in range(int((len(Nogames))/2)): 
    print(Nogames[i], Nogames[i+1])
    i += 2
    
print(usrgames)