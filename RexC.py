#Rex, the card game
import random
import time
import os

#Name: [attack, defense]
normal_cards={
    "knight": [50, 30],
    "barbarian": [55, 35],
    "wizard": [65, 50],
    "civilian": [20, 5],
    "archer": [40, 40],
    "messenger": [25, 5],
    "forest dweller": [60, 50],
    "flagbearer": [25, 20],
    "wrestler": [35, 40],
    "monopolist": [10, 65],
    "spy": [15, 60],
    "chef": [25, 40],
    "executioner": [60, 35],
    "prison guard": [50, 40],
    "scientist": [45, 15],
    "shieldbearer": [20, 70],
    "assassin": [75, 30],
    "berserker": [80, 20],
    "healer": [0, 60],
    "paladin": [50, 60],
    "rogue": [60, 40],
    "samurai": [55, 55],
    "mercenary": [55, 45],
    "lancer": [70, 30],
    "warlord": [75, 25],
    "noble": [35, 65],
    "sailor": [45, 55],
    "diplomat": [30, 60],
    "beast": [70, 25],
    "strategist": [50, 50]
}

special_cards={
    "secret police": [50, 70],
    "commando": [70, 55],
    "king": [10, 85],
    "queen": [20, 75],
    "ninja": [80, 65],
    "caged warrior": [75, 35],
    "gladiator": [40, 70],
    "titan": [85, 40],
    "imperial guard": [60, 80],
    "colossus": [90, 60]
}

playerCards=[]
compCards=[]
combined_cards = normal_cards | special_cards

def cardDist():
    cards=random.randint(3,10)
    specialcardCount= (cards//2)//2

    tempspL=list(special_cards.keys())
    tempnrL=list(normal_cards.keys())
    for i in range(specialcardCount):
        randomCard=random.choice(tempspL)
        playerCards.append(randomCard)
        tempspL.remove(randomCard)

        secondrandomCard=random.choice(tempspL)
        compCards.append(secondrandomCard)
        tempspL.remove(secondrandomCard)
    for i in range(cards-specialcardCount):
        randomCard=random.choice(tempnrL)
        playerCards.append(randomCard)
        tempnrL.remove(randomCard)

        secondrandomCard=random.choice(tempnrL)
        compCards.append(secondrandomCard)
        tempnrL.remove(secondrandomCard)
    
def displayCards():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f'You currently have {len(playerCards)} cards left')
    for i in range(len(playerCards)):
        print(f'{i+1}. {playerCards[i].title()}-  Attack: {combined_cards[playerCards[i]][0]}  Defense: {combined_cards[playerCards[i]][1]}')
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def doTurn(card:str,atdef:str):
    #card validation in main program
    compChosenCard=random.choice(compCards)

    if atdef=="a":
        playerAttack=combined_cards[card][0]
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f'You have chosen the card {card} with an attack rating of {playerAttack}')
        print(f'The witch chose the card {compChosenCard} with a defense rating of {combined_cards[compChosenCard][1]}')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if playerAttack<combined_cards[compChosenCard][1]:
            print('You lost the round!')
            if card not in special_cards:
                compCards.append(card)
                playerCards.remove(card)
            if compChosenCard in special_cards: compCards.remove(compChosenCard)
            if card in special_cards: playerCards.remove(card)
        elif playerAttack>combined_cards[compChosenCard][1]:
            print('You won the round!')
            if compChosenCard not in special_cards:
                playerCards.append(compChosenCard)
                compCards.remove(compChosenCard)
            if card in special_cards: playerCards.remove(card)
            if compChosenCard in special_cards: compCards.remove(compChosenCard)
        else:
            print('Draw!')
            if compChosenCard in special_cards: compCards.remove(compChosenCard)
            if card in special_cards: playerCards.remove(card)
    else:
        playerDefense=combined_cards[card][1]
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f'You have chosen the card {card} with an defense rating of {playerDefense}')
        print(f'The witch chose the card {compChosenCard} with a attack rating of {combined_cards[compChosenCard][0]}')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if playerDefense<combined_cards[compChosenCard][0]:
            print('You lost the round!')
            if card not in special_cards:
                compCards.append(card)
                playerCards.remove(card)
            if compChosenCard in special_cards: compCards.remove(compChosenCard)
            if card in special_cards: playerCards.remove(card)
        elif playerDefense>combined_cards[compChosenCard][0]:
            print('You won the round!')
            if compChosenCard not in special_cards:
                playerCards.append(compChosenCard)
                compCards.remove(compChosenCard)
            if card in special_cards: playerCards.remove(card)
            if compChosenCard in special_cards: compCards.remove(compChosenCard)
        else:
            print('Draw!')
            if compChosenCard in special_cards: compCards.remove(compChosenCard)
            if card in special_cards: playerCards.remove(card)

def checkWin():
    if len(compCards)==0 and len(playerCards)==0:
        print("Well there, you certainly got lucky this time. Next time, fate won't be so fortunate as it was right now...")
        time.sleep(0.5)
        return -1
    elif len(playerCards)==0:
        print("HA HA HA HA HA, ANOTHER ONE FALLS FOR THE TRAP, WHAT WERE YOU THINKING? THAT YOU COULD POSSIBLY WIN AGAINST ME??")
        time.sleep(1)
        print("Hope you have fun in the dark realm...")
        time.sleep(1)
        return 0
    elif len(compCards)==0:
        print("Well, uhh..you definitely got lucky this time, I'll definitely win next time..")
        time.sleep(0.5)
        return 1
    else: return None

def takeInp():
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    displayCards()
    cr=input("Which card would you like to pick? : ")
    while cr.lower() not in playerCards:
        cr=input("Sorry that is an invalid card, please choose one from your deck: ")
    aod=input("Would you like to play attack or defense? (A/D): ")
    if aod.lower() not in ["a","d"]:
        aod=("Sorry, please enter a valid option (A or D): ")
    doTurn(cr.lower(),aod.lower())

def main():
    print("Welcome to Rex, Ras.")
    time.sleep(1.5)
    print("You weren't informed of the dangers right?")
    time.sleep(1.5)
    print("It's alright, you will find out..soon.")
    time.sleep(1.5)

    cardDist()
    while checkWin()==None:
        takeInp()
        time.sleep(1)

main()
    
    
        

