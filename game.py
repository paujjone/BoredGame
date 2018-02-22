import random
location = 0
players = []
player = -1
nplay = int(input('Number of Players:'))
for n in range(nplay):
    rpo = {
        "Player" : n+1,
        "Location" : 0,
        "InJail" : 0,
        "JailMove" : 0,
        "Money" : 1500
    }
    players.append(rpo)
def dice():
    roll = []
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    roll = (die1, die2)
    return roll
def updateplayer(player,**modification):
    global players
    selected = players[player]
    if "Location" in modification:
        selected["Location"] = modification["Location"]
        if modification["Location"] == 30:
            selected["InJail"] = 1
            selected["Location"] = 10
        if modification["Location"] == 4:
            selected["Money"] -= 200
        if modification["Location"] == 38:
            selected["Money"] -= 120
    if "InJail" in modification:
        selected["InJail"] = modification["InJail"]
        selected["Location"] = 10
    if "JailMove" in modification:
        if modification["JailMove"] == "+1":
            selected["JailMove"] += 1
        else:
            selected["JailMove"] = modification["JailMove"]
    if "Money" in modification:
        selected["Money"] += modification["Money"]
    players[player] = selected
def movement(player,roll):
    newLocation = roll + players[player]["Location"]
    if newLocation >= 40:
        newLocation -= 40
        updateplayer(player,Money = 200)
    updateplayer(player,Location=newLocation)
def doubles(player,rolls):
    print("Player ",player+1,' - Doubles! x 1')
    roll = rolls[0] + rolls[1]
    movement(player,roll)
    rolls = dice()
    if rolls[0]==rolls[1]:
        print("Player ",player+1,' - Doubles! x 2')
        roll = rolls[0] + rolls[1]
        movement(player,roll)
        rolls = dice()
        if rolls[0]==rolls[1]:
            print("Player ",player+1,' - Doubles! x 3  Uh Oh :-(')
            updateplayer(player, InJail = 1)
        else:
            print("3rd Dice roll:",rolls)
            roll = rolls[0] + rolls[1]
            movement(player,roll)
    else:
        print("2nd Dice roll:",rolls)
        roll = rolls[0] + rolls[1]
        movement(player,roll)
def turn(player):
    print("(Player ",player+1,") - MOVE:")
    rolls = dice()
    print("Dice roll:",rolls)
    if rolls[0]==rolls[1]:
        doubles(player,rolls)
    else:
        roll = rolls[0] + rolls[1]
        movement(player,roll)
def myturn(player):
    whoisnext = (1+player) % nplay
    return whoisnext
def Jail(player):
    print("(Player ",player+1,") - JAIL BIRD MOVE:")
    rolls = dice()
    print("Dice roll:",rolls)
    if rolls[0]==rolls[1]:
        roll = rolls[0] + rolls[1]
        movement(player,roll)
        updateplayer(player, JailMove = 0)
        updateplayer(player, InJail = 0)
        print("Player ",player+1," is free!")
    else:
        updateplayer(player, JailMove = "+1")
        if players[player]["JailMove"] == 3:
            updateplayer(player, JailMove = 0)
            updateplayer(player, InJail = 0)
            updateplayer(player,Money = -50)
            print("Player ",player+1,"FINALLY is free!")
x = 1
while x = 1:
    player = myturn(player)
    if players[player]["InJail"] == 1:
        Jail(player)
    else:
        turn(player)
    for i in range(len(players)):
        print(players[i])
        if players[i]["Money"] <= 0:
            x = 2
    input('')
