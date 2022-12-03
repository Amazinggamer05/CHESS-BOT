import chessdotcom

username= input("Please enter a Username: ")

#year = input("Please enter a year: ")

#month = input("Please enter a month: ")

x = chessdotcom.get_player_profile(username)

print(x)