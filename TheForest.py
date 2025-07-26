#Missions for the forest stage

from Signs import validateInput as vl
from Signs import player 
import time
import random

def doPlayerTurn(battleCode,enemyHealth):
    enemyHealth-=player.weapons[battleCode][0]
    player.weapons[battleCode][1]-=1
    if player.weapons[battleCode][1]==0:
        del player.weapons[battleCode]

    return enemyHealth

def doEnemyTurn(enemyDamage):
    checkDeath=player.takeDamage(enemyDamage)
    return checkDeath

def checkWin(checkPlayerDeath,checkEnemyDeath):
    if checkEnemyDeath:
        player.currentMission+=1
        return True
    elif checkPlayerDeath:
        return True
    else:
        return False


def theFallingMysts():
    print("\n")
    print("<It is a bright day in the village of Ayutthaya…>\n")
    time.sleep(0.2)
    print("<You wake up at the crack of dawn; today is your first day at work as a researcher>\n")
    time.sleep(0.2)
    print("<You get ready, eagerly lock your house and run towards the town hall>\n")
    time.sleep(0.2)
    print("<You open the gates, and enter>\n")
    time.sleep(0.2)
    print("<The village chief, Lucien is sitting at the end of the corridor>\n")
    time.sleep(0.2)
    print("Ras:\nGood morning sir, I think I’m ready…\n")
    time.sleep(0.2)
    print("Lucien:\nGood morning indeed Ras. Well, to be honest I didn’t expect the day to come so quickly…but today is the first day you will be out in the forest…\n")
    time.sleep(0.2)
    print("Lucien:\nRemember though…please be careful out there…don’t get yourself too injured yeah? We need you back in one piece to know what the forest dwellers are actually doing.\n")
    time.sleep(0.2)
    print("<You let out a slight grin>\n")
    time.sleep(0.2)
    print("Lucien:\nAnyways, I shouldn’t really…delay you…there’s a lot on your agenda…but your first priority should definitely be finding Esperanca before dusk, their people are very accommodating.\n")
    time.sleep(0.2)
    print("Lucien:\nPlus, it helps that Esperanca is close to Wahran, a dweller settlement. This was briefed to you right?\n")
    time.sleep(0.2)
    print("Ras:\nYes yes…haha…you don’t have anything to worry about sir, the army was kind enough to provide me with weapons and an overview of many different types of situations.\n")
    time.sleep(0.2)
    print("Lucien:\nGood, good. Remember son, you don’t have to do this…it’s up to you…\n")
    time.sleep(0.2)
    print("Ras:\nI appreciate the offer, but this’ll help me learn more about my father and help us understand more about the dwellers…it’s something he would’ve wanted, especially after teaching me so much, I can’t just let it go to waste.\n")
    time.sleep(0.2)
    print("Lucien:\nIf you say so son…I’d like to think Julien would be proud of you either way…safe travels son…\n")
    time.sleep(0.2)
    print("Ras:\nGoodbye uncle, take care of yourself…\n")
    time.sleep(0.2)
    print("<He looks down in sadness, but then looks up and nods>\n")
    time.sleep(0.2)
    print("<You walk out of the town hall and look around, taking the sights of the village within; you might not come back in a while>\n")
    time.sleep(0.2)
    print("<You take a large sigh, and start walking towards the forest; you are going to be one of the first people to visit it in a long time, the others are too scared>\n")
    time.sleep(0.2)
    print("<A few hours of rustling and tustling later; you are tired, but it is not dusk yet, so you settle down on a tree stump to replenish yourself>\n")
    time.sleep(0.2)
    print("<Suddenly, something seems to be emerging from the bushes, you hold your spear, and prepare yourself for any confrontation>\n")
    time.sleep(0.2)
    print("<Suddenly, a coyote emerges, it seems to be hungry, and it barks at you; slowly approaching you>\n")
    time.sleep(0.2)
    print("<You have no choice, but to fight the coyote off because you know you cannot possibly outrun it>\n")
    time.sleep(0.2)

    coyoteHealth=50
    player.displayWeapons()
    playerDead=coyoteDead=False
    win=checkWin(playerDead,coyoteDead)
    damage=player.weapons[code][0]
    while not win:
        code=vl("Please enter the battle code of the weapon you would like to use: ", "Sorry, please enter a valid battle code: ", player.weapons.keys(),9999,str.upper)
        coyoteHealth=doPlayerTurn(code,coyoteHealth)
        print(f'You hit the coyote for {damage} damage! It now has {coyoteHealth} health left.')
        if coyoteHealth>0:
            if random.random()>0.1:
                coyoteDamage=random.randint(1,10)
                playerDead=doEnemyTurn(coyoteDamage)
            else:
                print("The coyote missed an attack on you!")
    if coyoteHealth<=0:
        print("You won...but at what cost?\n After this encounter, you have to sit down on the stump and think about what you have really done...and think about what just happened.\n")
        time.sleep(0.2)
        print("However, dusk is about to settle in soon, and you have no time left; you must continue on your journey")

def villageofEsperanca():
    print("\n")
    print("<After processing what just happened, you get up from the tree stump; determined to find the village of Esperanca>\n")
    time.sleep(0.2)
    print("<You start walking through the dense forest, cautious of any threats that might appear again>\n")
    time.sleep(0.2)
    print("<After walking for a few hours, you hear rustling from the bushes again, but this time, you’re nearing the village, so you assume it might be a villager>\n")
    time.sleep(0.2)
    print("Ras:\nHello? Is anyone there??\n")
    time.sleep(0.2)
    print("<You continue to move forward, slowly>\n")
    time.sleep(0.2)
    print("<Suddenly, a child emerges from a bush and starts running away from you>\n")
    time.sleep(0.2)
    print("Ras:\nHuh? What’s a child doing this deep in the forest?\n")
    time.sleep(0.2)
    print("<You begin to chase the child through the dense bushes and wilderness of the forest>\n")
    time.sleep(0.2)
    print("<During your pursuit…you end up on a large hill, and you start looking around to see where the child went>\n")
    time.sleep(0.2)
    print("<All of a sudden, your jaw drops; the entire village of Esperanca sits in a valley, a beautiful sight; children running around a campfire, more than a dozen straw huts and a large central trading area>\n")
    time.sleep(0.2)
    print("<You slowly inch towards the village, ensuring that you don’t startle anyone>\n")
    time.sleep(0.2)
    print("<Suddenly, warriors dressed in metal plates emerge from the bushes and cover your face with a bag and seemingly, arrest you>\n")
    time.sleep(0.2)
    print("Ras:\nNnnngh…RELEASE…ME…\n")
    time.sleep(0.2)
    print("Soldier 1:\nSILENCE…! Another word will not be tolerated.\n")
    time.sleep(0.2)
    print("<You comply, and are led by the soldiers down the hill and into the village centre. A group of villagers promptly surround you, with the Elder being amongst the audience>\n")
    time.sleep(0.2)
    print("The Elder:\nRelease him.\n")
    time.sleep(0.2)
    print("Soldier 2:\nBut…he is a spy!\n")
    time.sleep(0.2)
    print("Ras:\nMmmphh…nnnghh…\n")
    time.sleep(0.2)
    print("The Elder:\nI do not think he’s a spy, they are not usually this…obvious.\n")
    time.sleep(0.2)
    print("The Elder:\nSpeak…who are you? You bear a resemblance I have not seen in decades\n")
    time.sleep(0.2)
    print("<The guards remove the sack off your face, but you are still cuffed>\n")
    time.sleep(0.2)
    print("Ras:\nI’m Ras…uhh..I come from the village of Ayutthaya …agh…what’s happening here? I’m just an explorer…I was…told…this would be a safe place…\n")
    time.sleep(0.2)
    print("<Villagers murmur and chatter>\n")
    time.sleep(0.2)
    print("Ras:\nPlease don’t…hurt me…\n")
    time.sleep(0.2)
    print("The Elder:\nNo dear, we are not out here to hurt you…what is your purpose in our village? Speak child, does this being a ‘safe place’ mean that you are here to spy on us?\n")
    time.sleep(0.2)
    print("Ras:\nNo…no…I’m here to…learn more about the lost civilizations…and about the forest dwellers…\n")
    time.sleep(0.2)
    print("<Villager murmurs get louder>\n")
    time.sleep(0.2)
    print("The Elder:\nAh, it makes a lot of sense. Only a fool would dare attempt to find the forest dwellers, like yourself. Lucky for you, we are simple people trying to live in a shadowed world.\n")
    time.sleep(0.2)
    print("The Councilor:\n*whispering to the elder* This man claims he comes from Ayutthaya, possesses knowledge about the lost civilizations and looks familiar…could he be…the son of Reyes…perhaps even the daybringer?\n")
    time.sleep(0.2)
    print("The Elder:\n*whispering back* Impossible! Reyes was a traitor, the scrolls state that the daybringer is of pure blood.\n")
    time.sleep(0.2)
    print("The Councilor:\n*whispering back* Right, however, he can still be of use to us in our battle against the dwellers…perhaps he can gather information for us…I would prefer not sacrificing our people for this..\n")
    time.sleep(0.2)
    print("The Elder:\n*whispering back* We are in agreement on this matter.\n")
    time.sleep(0.2)
    print("The Elder:\nRight, since we believe that you have no malicious intentions, you are welcome to stay in our humble village, gather advice on the forest and of course, enjoy our lamb roast. But remember…we are watching you..\n")
    time.sleep(0.2)
    print("<The soldiers uncuff you, and walk away whilst looking at you; suspiciously>\n")
    time.sleep(0.2)
    print("The Councilor:\nRuh, please guide this gentleman to his accommodation.\n")
    time.sleep(0.2)
    print("<Ruh emerges from the crowd>\n")
    time.sleep(0.2)
    print("Ruh:\nYes sire, will do…\n")
    time.sleep(0.2)
    print("Ruh:\nUh…please follow me Mr Ras…I will take you to your quarters…\n")
    time.sleep(0.2)
    print("<You look at Ruh, visibly doubtful, yet your intuition says that they’re not out here to hurt you>\n")
    time.sleep(0.2)
    print("<Ruh starts walking towards the crowd, and they split apart to create a gap for you to walk in between>\n")
    time.sleep(0.2)
    print("<You quietly start following Ruh, where you look to your left and see the crowd staring at you like an alien creature>\n")
    time.sleep(0.2)
    print("<You then keep your head forward and keep following Ruh, who is taking you down an empty street>\n")
    time.sleep(0.2)
    print("Ruh:\nSo you’re from Ayutthaya? Must be nice not living in a shadowed world right?? If I’m being honest, our people got used to it but we are still waiting for the daybringer to come as the scroll says…I mean I don’t expect you to know anything about it…but hey, either way, it’s nice seeing a different face in this village, you do NOT know how tiring it gets to see the same faces every single day…\n")
    time.sleep(0.75)
    print("<You look at Ruh and a grin lights up your face, his chatteriness amuses you>\n")
    time.sleep(0.2)
    print("<A question pops up in your head as you’re walking down the street, and you just have to ask it>\n")
    time.sleep(0.2)
    print("Ras:\nWhat’s the deal with the daybringer?\n")
    time.sleep(0.2)
    print("Ruh:\nI KNEW you were going to ask that, the name’s pretty sweet right? Just slides off the tongue. Well, to be honest, I didn’t know much about it, but ever since I started working as an assistant to the Councilor, it’s ALL I hear everyday, apparently, one of our ancestors who escaped from the forest dwellers wrote something about a daybringer, who will be the child of a member of this village and of quote unquote pure blood will emerge some day and apparently do something to the forest dwellers, which will remove the shadow from our world and the terror the forest dwellers spread.\n")
    time.sleep(0.75)
    print("Ruh:\nSome of the villagers think YOU might be the daybringer, but hey, I doubt it…after all, you’re just an explorer of the forest, you don’t look like a warrior from any angle.\n")
    time.sleep(0.75)
    print("<Ruh suddenly stops, and so do you>\n")
    time.sleep(0.2)
    print("Ruh:\nAh, here we are, house number 57, this used to be a wizard’s house by the way, so don’t mind the occasional rat tail if you find it.\n")
    time.sleep(0.2)
    print("<You look at him, concerningly>\n")
    time.sleep(0.2)
    print("Ruh:\nAhh…haha don’t worry, it’s highly unlikely anyways. We have a really nice trading area further down the street, it’s got a bar, a place where you can buy potions, a blacksmith and of course the damn traders, so yeah feel free to check that out once you’ve settled in. We also have a lamb roast almost every night at the campfire, so join us if you ever have the chance!\n")
    time.sleep(0.45)

    player.currentMission+=1
    player.xp+=50

    print(f'50XP has been added for a successful mission completion, your current balance is {player.xp}')
