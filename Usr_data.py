from loading import loading
from random import randint
from datetime import datetime
import chessdotcom

#username= input("Please enter a Username: ")

#Place Holder name#
username = "HomJob"
#username = "ziebz"


Games = []
Nogames = []

x = chessdotcom.get_player_profile(username)

d = datetime.now()

maxyr = d.year
maxmnth = d.month

year = 2007

month = 4

while year != maxyr or month < maxmnth + 1:

    if month == 13:
        month = 1
        year += 1

    usrgames = chessdotcom.get_player_games_by_month_pgn(username, year, month)
    usrgames = str(usrgames)

    for x in usrgames:
        pass
        #if usrgames[x] != 
    if usrgames != "ChessDotComResponse(pgn=Collection(pgn=''))":
        
        Games.append(year)
        Games.append(month)

    else:
        Nogames.append(year)
        Nogames.append(month)

    month += 1
    print(loading[randint(0,len(loading)-1)])

print(usrgames)

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
    
#print(usrgames)