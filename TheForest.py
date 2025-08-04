#Missions for the forest stage

from Signs import validateInput as vl
from Signs import player
from Signs import kaiser,alara,dementia,riz
import time
import random

fixedOptions={"Riz the Bartender":riz.uporbuy,"Dementia the Witch":dementia.playorbuy,"Kaiser the Bartender":kaiser.drinkServe,"Alara the Trader":alara.sellbuyortrade,"Start Mission":None}

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
        return True
    elif checkPlayerDeath:
        return True
    else:
        return False

def doBattle(enemyHealth,enemyName,randomFailDia,winEnemyHealth=0, Endamagerange=(1,10),randomFailChance=0.0):
    player.displayWeapons()
    playerDead=enemyDead=False
    win=checkWin(playerDead,enemyDead)
    while not win:
        code=vl("Please enter the battle code of the weapon you would like to use: ", "Sorry, please enter a valid battle code: ", player.weapons.keys(),9999,str.upper)
        damage=player.weapons[code][0]
        enemyHealth=doPlayerTurn(code,enemyHealth)
        print(f'You hit the {enemyName} for {damage} damage! It now has {enemyHealth} health left.')
        if enemyHealth>winEnemyHealth:
            if random.random()>randomFailChance:
                playerDead=doEnemyTurn(random.randint(*Endamagerange))
            else:
                print(randomFailDia)
        win=(playerDead,enemyHealth<=winEnemyHealth)
    else:
        return enemyHealth

def printDialogues(diaList,sleepTime=4,letterswithExtension=30,extensionTime=10):
    for dia in diaList:
        if len(dia.split())>=letterswithExtension:
            print(dia)
            time.sleep(extensionTime)
        else:
            print(dia)
            time.sleep(sleepTime)

def userOptions(*onetimeevents,**options):
    funcNames=list(options.values())
    displayNames=list(options.keys())
    ex=False

    while not ex:
        print("~~~~~~Your Options~~~~~~")
        for i in range(len(displayNames)):
            print(f'{i+1}- {displayNames[i]}')
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        inp=vl("Please enter the number of the option you would like to choose","Sorry, please enter a valid number",[str(i) for i in range(1,len(displayNames)+1)],999)
        inp=int(inp)-1
        if displayNames[inp]=="Start Mission":
            ex=True
        else:
            funcNames[inp]()
            if displayNames[inp] in onetimeevents:
                displayNames.pop(inp)
                funcNames.pop(inp)



def theFallingMysts():
    print("\nStage 1. The Falling Mysts\n")
    time.sleep(4)
    dialogues=["<It is a bright day in the village of Ayutthaya...>\n", "<You wake up at the crack of dawn; today is your first day at work as a researcher>\n", "<You get ready, eagerly lock your house and run towards the town hall>\n", "<You open the gates, and enter>\n", "<The village chief, Lucien is sitting at the end of the corridor>\n", "Ras:\nGood morning sir, I think I'm ready...\n", "Lucien:\nGood morning indeed Ras. Well, to be honest I didn't expect the day to come so quickly...but today is the first day you will be out in the forest...\n", "Lucien:\nRemember though...please be careful out there...don't get yourself too injured yeah? We need you back in one piece to know what the forest dwellers are actually doing.\n", "<You let out a slight grin>\n", "Lucien:\nAnyways, I shouldn't really...delay you...there's a lot on your agenda...but your first priority should definitely be finding Esperanca before dusk, their people are very accommodating.\n", "Lucien:\nPlus, it helps that Esperanca is close to Wahran, a dweller settlement. This was briefed to you right?\n", "Ras:\nYes yes...haha...you don't have anything to worry about sir, the army was kind enough to provide me with weapons and an overview of many different types of situations.\n", "Lucien:\nGood, good. Remember son, you don't have to do this...it's up to you...\n", "Ras:\nI appreciate the offer, but this'll help me learn more about my father and help us understand more about the dwellers...it's something he would've wanted, especially after teaching me so much, I can't just let it go to waste.\n", "Lucien:\nIf you say so son...I'd like to think Julien would be proud of you either way...safe travels son...\n", "Ras:\nGoodbye uncle, take care of yourself...\n", "<He looks down in sadness, but then looks up and nods>\n", "<You walk out of the town hall and look around, taking the sights of the village within; you might not come back in a while>\n", "<You take a large sigh, and start walking towards the forest; you are going to be one of the first people to visit it in a long time, the others are too scared>\n", "<A few hours of rustling and tustling later; you are tired, but it is not dusk yet, so you settle down on a tree stump to replenish yourself>\n", "<Suddenly, something seems to be emerging from the bushes, you hold your spear, and prepare yourself for any confrontation>\n", "<Suddenly, a coyote emerges, it seems to be hungry, and it barks at you; slowly approaching you>\n", "<You have no choice, but to fight the coyote off because you know you cannot possibly outrun it>\n"]
    printDialogues(dialogues)

    fight=doBattle(50,"Coyote","The Coyote missed an attack on you!",0,(1,10),0.1)
    if fight<=0:
        print("You won...but at what cost?\n After this encounter, you have to sit down on the stump and think about what you have really done...and think about what just happened.\n")
        time.sleep(3)
        print("However, dusk is about to settle in soon, and you have no time left; you must continue on your journey")
        print(f'50XP has been added for successful mission completion, your new balance is {player.xp}XP')
        player.xp+=50
        player.currentMission+=1


def villageofEsperanca():
    print("\nStage 2. The Village of Esperanca\n")
    time.sleep(4)
    userOptions(**{"Start Mission":None})
    time.sleep(4)
    dialogues=["<You start walking through the dense forest, cautious of any threats that might appear again>\n", "<After walking for a few hours, you hear rustling from the bushes again, but this time, you're nearing the village, so you assume it might be a villager>\n", "Ras:\nHello? Is anyone there??\n", "<You continue to move forward, slowly>\n", "<Suddenly, a child emerges from a bush and starts running away from you>\n", "Ras:\nHuh? What's a child doing this deep in the forest?\n", "<You begin to chase the child through the dense bushes and wilderness of the forest>\n", "<During your pursuit...you end up on a large hill, and you start looking around to see where the child went>\n", "<All of a sudden, your jaw drops; the entire village of Esperanca sits in a valley, a beautiful sight; children running around a campfire, more than a dozen straw huts and a large central trading area>\n", "<You slowly inch towards the village, ensuring that you don't startle anyone>\n", "<Suddenly, warriors dressed in metal plates emerge from the bushes and cover your face with a bag and seemingly, arrest you>\n", "Ras:\nNnnngh...RELEASE...ME...\n", "Soldier 1:\nSILENCE...! Another word will not be tolerated.\n", "<You comply, and are led by the soldiers down the hill and into the village centre. A group of villagers promptly surround you, with the Elder being amongst the audience>\n", "The Elder:\nRelease him.\n", "Soldier 2:\nBut...he is a spy!\n", "Ras:\nMmmphh...nnnghh...\n", "The Elder:\nI do not think he's a spy, they are not usually this...obvious.\n", "The Elder:\nSpeak...who are you? You bear a resemblance I have not seen in decades\n", "<The guards remove the sack off your face, but you are still cuffed>\n", "Ras:\nI'm Ras...uhh..I come from the village of Ayutthaya ...agh...what's happening here? I'm just an explorer...I was...told...this would be a safe place...\n", "<Villagers murmur and chatter>\n", "Ras:\nPlease don't...hurt me...\n", "The Elder:\nNo dear, we are not out here to hurt you...what is your purpose in our village? Speak child, does this being a 'safe place' mean that you are here to spy on us?\n", "Ras:\nNo...no...I'm here to...learn more about the lost civilizations...and about the forest dwellers...\n", "<Villager murmurs get louder>\n", "The Elder:\nAh, it makes a lot of sense. Only a fool would dare attempt to find the forest dwellers, like yourself. Lucky for you, we are simple people trying to live in a shadowed world.\n", "The Councilor:\n*whispering to the elder* This man claims he comes from Ayutthaya, possesses knowledge about the lost civilizations and looks familiar...could he be...the son of Reyes...perhaps even the daybringer?\n", "The Elder:\n*whispering back* Impossible! Reyes was a traitor, the scrolls state that the daybringer is of pure blood.\n", "The Councilor:\n*whispering back* Right, however, he can still be of use to us in our battle against the dwellers...perhaps he can gather information for us...I would prefer not sacrificing our people for this..\n", "The Elder:\n*whispering back* We are in agreement on this matter.\n", "The Elder:\nRight, since we believe that you have no malicious intentions, you are welcome to stay in our humble village, gather advice on the forest and of course, enjoy our lamb roast. But remember...we are watching you..\n", "<The soldiers uncuff you, and walk away whilst looking at you; suspiciously>\n", "The Councilor:\nRuh, please guide this gentleman to his accommodation.\n", "<Ruh emerges from the crowd>\n", "Ruh:\nYes sire, will do...\n", "Ruh:\nUh...please follow me Mr Ras...I will take you to your quarters...\n", "<You look at Ruh, visibly doubtful, yet your intuition says that they're not out here to hurt you>\n", "<Ruh starts walking towards the crowd, and they split apart to create a gap for you to walk in between>\n", "<You quietly start following Ruh, where you look to your left and see the crowd staring at you like an alien creature>\n", "<You then keep your head forward and keep following Ruh, who is taking you down an empty street>\n", "Ruh:\nSo you're from Ayutthaya? Must be nice not living in a shadowed world right?? If I'm being honest, our people got used to it but we are still waiting for the daybringer to come as the scroll says...I mean I don't expect you to know anything about it...but hey, either way, it's nice seeing a different face in this village, you do NOT know how tiring it gets to see the same faces every single day...\n", "<You look at Ruh and a grin lights up your face, his chatteriness amuses you>\n", "<A question pops up in your head as you're walking down the street, and you just have to ask it>\n", "Ras:\nWhat's the deal with the daybringer?\n", "Ruh:\nI KNEW you were going to ask that, the name's pretty sweet right? Just slides off the tongue. Well, to be honest, I didn't know much about it, but ever since I started working as an assistant to the Councilor, it's ALL I hear everyday, apparently, one of our ancestors who escaped from the forest dwellers wrote something about a daybringer, who will be the child of a member of this village and of quote unquote pure blood will emerge some day and apparently do something to the forest dwellers, which will remove the shadow from our world and the terror the forest dwellers spread.\n", "Ruh:\nSome of the villagers think YOU might be the daybringer, but hey, I doubt it...after all, you're just an explorer of the forest, you don't look like a warrior from any angle.\n", "<Ruh suddenly stops, and so do you>\n", "Ruh:\nAh, here we are, house number 57, this used to be a wizard's house by the way, so don't mind the occasional rat tail if you find it.\n", "<You look at him, concerningly>\n", "Ruh:\nAhh...haha don't worry, it's highly unlikely anyways. We have a really nice trading area further down the street, it's got a bar, a place where you can buy potions, a blacksmith and of course the damn traders, so yeah feel free to check that out once you've settled in. We also have a lamb roast almost every night at the campfire, so join us if you ever have the chance!\n"]

    printDialogues(dialogues)
    print("<After processing what just happened, you get up from the tree stump; determined to find the village of Esperanca>\n")

    player.currentMission+=1
    player.xp+=50

    print(f'50XP has been added for a successful mission completion, your current balance is {player.xp}')

def betrayalofFate():
    print("\nStage 3. Betrayal of Fate\n")
    print("<You wake up and are ready to enter the forest once again, using the knowledge of the forest that you obtained from the research back in Ayutthaya in an attempt to guide your way>\n")
    time.sleep(4)
    dialogues=["<You push through some thick bushes, brushing aside branches and vines as you make your way in deeper>\n","<The ground is uneven, roots sticking out in every direction, and you nearly trip more than once>\n","<Birds scatter overhead as you pass by, and you hear the distant sound of running water somewhere to your left>\n","<You stop for a moment, listening; something feels off>\n","<Suddenly, emerged from a bush, a giant creature>\n","<You know this creature, your father told you about it in fragments of folklore; a type of animal the forest dwellers have domesticated for battle purposes>\n","<You think about this situation very carefully; either you attempt to run away or you fight the creature. The decision is up to your intuition>\n"]
    printDialogues(dialogues)

    inp=vl("What will it be: fight or run? (F/R): ","Sorry, please enter a valid option from F or R: ",["f","r"],999)
    if inp=="r":
        chanceofEscape=player.currentStamina/100.0
        if chanceofEscape>random.random():
            print(f'<The Esperanca council is disturbed, and unimpressed by your cowardice. Your acts have posed danger to the village itself and for this misdemeanour, they have charged you a fine of {player.xp*0.2} and Dementia has been asked to penalize your max stamina by {player.maxStamina*0.1}, just in case.>\n')
            player.maxStamina*=0.9
            player.xp*=0.75
            theBeast=None
        else:
            theBeast=doBattle(75,"The Beast","The Beast missed an attack on you, lucky you!",0,(1,10),0.0)
    else:
        theBeast=doBattle(75,"The Beast","The Beast missed an attack on you, lucky you!",0,(1,10),0.15)
    
    if theBeast!=None and theBeast<=0:
        print("<Amongst the corpse of the beast, you find several pieces of armor and a blade of glory. You pick it up and keep it, hoping that it aids you in your journey>\n")
        if "blade of glory" not in player.weapons:
            player.weapons["BG"]=[30,15,15,"blade of glory"]
        player.xp+=50
        print(f"For your triumph in the battle with the beast>, the Esperanca council has given you a grant of 50XP, your new balance is {player.xp}")

    if not theBeast>0:
        player.xp+=50
        print(f'50XP has been added for a successful mission completion, your current balance is {player.xp}')
        player.currentMission+=1
    
def thekeepersoftheForest():
    print("\nStage 4. The Keepers of the Forest\n")
    time.sleep(4)
    print("<You wake up at the crack of dawn once again, sore from the events of the previous afternoon, yet you feel that today's exploration will be fruitful, yet you believe that you must be well-prepared and replenished for this quest>\n")
    time.sleep(4)
    userOptions("XY","XY",**fixedOptions)
    missionPart1Dia=["<You once again enter the forest; knowing that each entry is a life or death situation, but you feel well prepared this time>\n", "<After walking for a while, you encounter an unexpected sight; your heart drops.>\n", "<It's a campfire deep inside the forest, what could've left?>\n", "<You approach it, cautiously, you've learned from your past mistakes with the child and now you keep better tabs of your surroundings>\n", "<Once you get close to the campfire, it seems that it was recently lit up, and there are what seems to be pouches with various edibles and tools>\n", "<Suddenly, from the dense wilderness; two strange creatures emerge. They carry weapons and appear to be the 'keepers', who are part of Wahran's dweller army.>\n", "<Both the keepers approach you; spears pointed at you. But you can't move back, there's fire>\n", "Keeper 1:\nURGCM JWOCP, YJQ CTG YQWA\n", "Translation: SPEAK HUMAN, WHO ARE YOU?\n", "Ras:\nHuh?? I don't...understand you...please...I'm not here to hurt you...\n", "Keeper 2:\n*whilst looking at Keeper 1* Vjku jwocp owtowtu ikddgtkuj, Jg ku pqvjkpi dwv c nkcdknkvy vq wu\n", "Translation: This human murmurs gibberish, he is nothing but a liability to us...\n", "Keeper 1:\n*replying to Keeper 2* Vjgp, yg ctg kp citggogpv\n", "Translation: Then, we are in agreement.\n", "<The keepers both stare back at you, and you know at this point, there is no chances of running away>\n", "<As you're thinking your next course of action, a set of keys on one of the Keeper's vest intrigues you>\n"]
    missionPart2Dia=["<After defeating both of the keepers, you sit down on a tree stump to process what just happened...>\n", "<Then, you get up and search the bags that the keepers were carrying; there is a map to the forest dweller's settlement; a great discovery>\n", "<There was also a scroll inside of the bags, which was written in their language, you kept it in your bag just in case someone in the village understood it.>\n", "<Then, you grab the keys that the keepers had>\n", "<You then look at the sky and realize that it's going to be dark soon; not a safe option in this forest, especially with the first ever forest dweller encounter>\n", "<You then rush to head back to the village, still trying to process what you just did>\n", "<Once you return to the village, you sprint towards the town hall and demand entrance>\n", "<You run down a large corridor, where at the end the Elder sits on a large throne>\n", "Ras:\n*panting* Elder...elder...I...did...something...*gulps* ...really bad...\n", "The Elder:\nSon, calm down, it's alright, what has happened? Come here...take a seat...\n", "<You look towards a chair near the Elder and walk towards it and take a seat; you notice that the Councilor's office still has Ruh in it, and he's looking at you from the room, concerningly>\n", "Ras:\n*still panting heavily* So...I was in the forest, and I noticed a campfire deep within, and I decided to scout it, but then suddenly, I was ambushed by a forest dweller.\n", "The Elder:\nA...forest dweller?\n", "Ras:\nYes...they were some sort of...soldiers, I don't know, but they carried weapons and spoke a cryptic language that I couldn't understand, but they were going to kill me.\n", "Ras:\nBut I ended...up...killing them instead...\n", "<You regrettably look at the elder>\n", "The Elder:\nSon, you did nothing wrong...it was merely...self defence I would say, anybody in your situation would have done the same. Did they carry anything that would be helpful in understanding the next course of action?\n", "Ras:\nYes...yes...they had a map on them...to the forest dweller settlement...and a scroll in their language.\n", "The Elder:\nWhat!?\n", "Ras:\nYes, I can show it to you!\n", "The Elder:\nI believe you...it's just that...I'm shocked...we haven't had a direct confrontation or interaction with a forest dweller for many decades now...\n", "The Elder:\nI do need some time to process this son, but tomorrow I will call in the head scrollwriter of Esperanca, I believe he has some knowledge about their language...maybe he can help decode the message...\n", "The Elder:\nFor now, you must rest.\n", "The Elder:\nRuh, please take Ras back to his quarters.\n", "<Ruh sprints out of the Councilor's office towards you>\n", "<You get up and slowly start leaving the building with Ruh>\n", "Ruh:\nSo...I heard all that...what an interaction you had huh?\n", "Ras:\nYeah...I don't think I'll ever recover from that one...\n", "Ruh:\nHey, hey, listen to me...as the Elder said, it was self defence, don't worry much about it, if I were you, I'd actually be happy, an XP pay bump is definitely coming your way haha.\n", "Ras:\nI guess...I just got so...scared...they spoke some gibberish, I heard a lot of v's and g's.\n", "<Ruh thinks for a bit>\n", "Ruh:\nUhh...was it something like Vjgp?\n", "Ras:\nYES, YES IT WAS...do you...know their language???\n", "Ruh:\nAhh...no no, nothing like that, I heard the lead scrollwriter say it once I guess. Don't worry though, tomorrow's the big day yeah?\n", "Ras:\nYeah I guess...I don't know how I'll sleep at night...\n", "Ruh:\nHey, if you can't ever sleep, Kaiser's usually does the work.\n", "<You let out a soft laugh>\n", "Ras:\nYeah, I guess so.\n", "<You reach you quarters and enter it, looking at the dimly lit room with fear; nonetheless, you crawl into bed, staring at the timber ceiling, thinking about what just happened>\n"]

    printDialogues(missionPart1Dia)
    keeper1=doBattle(40,"Keeper 1","The Keeper missed an attack on you, lucky you!",0,(1,10),0.15)
    if keeper1<=0:
        keeper2=doBattle(40,"Keeper 2","The Keeper missed an attack on you, lucky you!",0,(1,8),0.2)
    
    if (keeper1<=0 and keeper2<=0):
        player.currentMission+=1
        printDialogues(missionPart2Dia)
        player.xp+=50
        print(f"For your triumph in the battle with the keepers, the Esperanca council has given you a grant of 50XP, your new balance is {player.xp}")

def thetalesoftheForgotten():
    print("\nStage 5. The Tales of the Forgotten\n")
    time.sleep(4)
    print("<You wake up at the crack of dawn again to the caws of the crows, weary of yesterday's events, but hopeful of your discoveries>")
    #User options go here ig
    dias=["<You leave your quarters and head towards Ruh's house, ready to meet with the Elder>\n", "<Whilst you're walking towards Ruh's house, he opens the door and leaves his house>\n", "<He looks towards you>\n", "Ruh:\nReady to go, neighbour?\n", "<You nod, and start following him; anxiously carrying the scroll and map>\n", "Ruh:\nDid you sleep well last night? I know that encounter probably left a stain on your brain.\n", "Ras:\nYeah...I definitely had trouble sleeping, but I just kept telling myself, as you said, that it was just self defense.\n", "Ruh:\nMhm, hey, don't beat yourself for it, you definitely did the right thing, those people have nothing but rage...and rabidness inside of their blood...\n", "Ras:\nI guess...\n", "<Eventually, you reach the scrollwriters' building; to you, it's an ancient dilapidated mess>\n", "Ras:\nThis...is the building...?\n", "Ruh:\nYeah...these people aren't exactly maintenance friendly.\n", "<Ruh opens the door and walks in, and you follow him>\n", "<As you walk into the building, it is nothing but a large room filled with scrolls and desks, with many scrollwriters working on analyzing and writing new scrolls>\n", "<At the end of the room, the head scrollwriter sits at a desk, observing a scroll with a magnifying glass>\n", "<You both walk towards him, and he lifts his head up to look up to you>\n", "Sapien:\nI had awaited your arrival, the Elder had informed me of what had happened.\n", "Sapien:\nYou do not hail from Esperanca, right son?\n", "Ras:\nWho? Me...?\n", "Sapien:\nYes, your eyes speak of something louder than your body allows. The people of Esperanca are too mundane to appear like this.\n", "Ras:\nUh...yes, I'm from the village of Ayutthaya, sent on a mission to study about the dwellers and report back to the chief as soon as it is done.\n", "Sapien:\nHmmh...I see...how can I help you both today?\n", "<You take out the scroll from your bag>\n", "Ras:\nWe need help uh...decoding this scroll...I picked it up from a forest dweller at one of their campsites...\n", "Sapien:\nYou crave the darkness, don't you son?\n", "Ras:\nWhat?\n", "Sapien:\nAn ordinary person would never want to interact with the forest dwellers; yet you are out here searching for them.\n", "Sapien:\nTell me...what is it that you really desire?\n", "<You stare at Sapien for a while>\n", "Ruh:\nAlright, that's enough old man, just help us decode the scroll, we haven't got all day.\n", "<Sapien stares at you for a while and then looks at Ruh>\n", "Sapien:\nVery well.\n", "<Sapien opens the scroll and looks at it, his face has a mixture of confusion and interest>\n", "<He then looks to the bottom of the scroll, and freezes>\n", "<After that, he puts the scroll down and takes a large gulp>\n", "Ruh:\nWhat...what happened?\n", "Sapien:\nThe time has come, the time we all feared, the time we all looked forward to, the time we thought was never.\n", "Ruh:\nAnd what time would that be?\n", "Sapien:\nThe dwellers of Wahran are preparing for war...the Daybringer has made himself present...\n", "<You and Ruh both look at each other with suspicion>\n", "Ras:\nWait...how sure are you of this...isn't the Daybringer just folklore??\n", "<Sapien sits down on his chair, still staring into blank space>\n", "<He then looks at both of you>\n", "Sapien:\nMy ancestors were knowledgeable, but were always doubted...the scrolls foreshadowed our fate...yet we chose to be ignorant.\n", "Ruh:\nYeah...but how can we believe that the forest dwellers know about the Daybringer? Or if the Daybringer even exists?\n", "Sapien:\nMy dear...the scrolls don't lie. The original writers themselves were there when the dwellers were cursed, yet, they were limited in only their ability to take action to it.\n", "Ruh:\nAlright...so we'll go tell this to the Elder...so uhh he can prepare defenses, I guess? That's all we can do right?\n", "<Ruh looks at you, and you nod in agreement>\n", "<As you're about to leave, Sapien puts his head down and murmurs something>\n", "Sapien:\nThe darkest of shadows...are always casted by the brightest ones...\n", "<You both stop and turn around, visibly confused>\n", "Sapien:\nYou fools...you forgot the core of the prophecy, the Daybringer is the child of Esperanca; one born in the purity of both shadow and light, one of both nobility and humility, one with both regret and reason.\n", "Ruh:\nAnd...what is that supposed to mean now? You mean the Daybringer is in the village right now?\n", "Sapien:\nYes...and if I were you, I would inform the Elder as well. Remember, the dwellers aren't monsters, their fate is just as unfortunate as their blood.\n", "Ras:\nWell...is there any...solution to this? Maybe we can prevent all out war...?\n", "Sapien:\nYes, Dementia can brew up a cure to the rabidness that their blood emanates.\n", "Ras:\nAnd how can one potion possibly be given to the whole colony?\n", "Sapien:\nAhh...good question actually, there are many hot springs that emit steam around and in Wahran, the largest one being in the centre of the city, a single drop of the potion can allow the cure to spread to the entire colony.\n", "Ruh:\nThat's fine and all, but how come no one has done this before? Anyone can penetrate their defences and cure them right?\n", "Sapien:\nSon, remember, the Daybringer hails from the darkness too, only one of sanity and insanity can truly ‘penetrate' their defences...\n", "Ruh:\nAlright...we appreciate your help, we'll inform this to the Elder now...\n", "Sapien:\nFarewell, be safe out there...\n", "<You have one last look at Sapien, who still seems to be staring at you, but you ignore it>\n", "<You turn around and start following Ruh out of the building>\n", "Ras:\nWow...that was a lot of information to take in...\n", "Ruh:\nYeah haha, that was a lot of talking. I've known this scrollwriter for a while now, all he does is yap yap yap, but hey, at least now we know what to do.\n", "Ruh:\nHopefully though, I don't get recruited for whatever defences these people come up with, my back has been SORE.\n", "Ras:\nHaha, yeah let's see.\n", "<You both make your way over to the townhall, where you enter and inch towards the Elder's throne>\n", "Ras:\nGood Morning Sir, we have received information from the head scrollwriter that the letter found from the keepers is them relaying war, and that the Daybringer has arrived.\n", "The Elder:\nWhat??!\n", "Ras:\nYes, it would be recommended to start setting up defences, as Esperanca will probably be the first target...\n", "The Elder:\nNo no, that's fine, but the Daybringer's here? I'll meet with the scrollwriter tonight to know more, how can this happen?\n", "Ruh:\nTrust me, we didn't believe it either...\n", "The Elder:\nAlright, well, I will tell Gustav to ready the defences, but we must at the same time try to observe more about Wahran, especially with the map in our possession.\n", "The Elder:\nRuh, please accompany Ras for the next exploratory mission, it is getting too dangerous out there...and we cannot risk losing vital pieces of information.\n", "Ruh:\nYes sir, will do.\n", "The Elder:\nI will convene the council later in the day to discuss possible courses of action, for now, you both are excused.\n", "Ruh:\nWell uh...I'll see you after my shift to discuss tomorrow's expedition yeah? Don't worry about the food, trust me, I make a killer soup.\n", "Ras:\nOh wow, alright, can't wait. See you later!\n"]

    printDialogues(dias)
    player.xp+=75
    print(f'You have been granted 75XP for successful mission completion, your new balance is {player.xp}')

def lunarAbyss(): #Imo, the best of them all
    print("\nStage 6. Lunar Abyss\n")
    time.sleep(4)
    print("<You wake up again at the crack of dawn, replenished after a good night's sleep, but are now aware of the danger that lurks within the forest; and the precautions you must take>")

    missionPart1Dia=["<You leave the house, carrying all the essentials you think you need in the forest>\n", "<You see that Ruh is already outside, talking to someone>\n", "<Ruh eventually sees you and dismisses the stranger>\n", "Ruh:\nHey partner, ready to go? We got a long day ahead of us really.\n", "Ras:\nYeah, I think it's best to not delay it any further.\n", "Ruh:\nMhm, I agree, let's go then.\n", "<You and Ruh enter the forest once again, this time guided by a map>\n", "Ras:\nWe'll keep a safe distance from Wahran to observe their defences, I think this part of the forest is good and dense enough for that.\n", "Ruh:\n*looking at the map* Hmm, yeah I agree, alright so we'll head that way.\n", "Ruh:\nSooo, how have you been? I'm actually quite excited for this, I haven't been in the forest for a while, but I was here when I was training to become a secretary to the councilor, I remember the nights I enjoyed deer for dinner...yeah...good days.\n", "Ras:\nYeah, I've been fine, I'm glad you're here today; I could use the extra support.\n", "Ruh:\nHey man, anytime.\n", "<Eventually, you and Ruh reach the designated spot that will help you keep a safe distance>\n", "Ruh:\nAhh, what do you say, should we grab lunch? I'm famished\n", "Ras:\nYeah...uh sure...let's settle down our things on that tree stump right there and take out the food.\n", "<You keep your bag on a tree stump and take out the food>\n", "Ruh:\nOh man, you're really not you when you're hungry, can't wait to devour this\n", "<Suddenly, leaves rustle and you hear the unknown language again>\n", "<You look behind you, and see the keepers emerging>\n", "Ras:\nRuh! Watch out!\n", "<Ruh looks back and runs towards his bag, grabbing his spear from it>\n", "<Eventually, a unit of keepers emerges, and they look at you rabidly, but then their eyes set on Ruh>\n", "Keeper 1:\nJwj? Yqw....YQW? KV YCU YQW!\nTranslation: Huh? You....YOU? IT WAS YOU!\n", "<At this point, the ‘general' of the unit steps forward, and starts speaking to Ruh>\n", "<Ruh gives you a side eye, acting confused>\n", "Keeper General:\nUrgcm vtckvqt, yjcv jcu ecwugf yqw vq cdcpfqp fguvkpy?\nTranslation: Speak traitor, what has caused you to abandon destiny?\n", "Keeper General:\nYg cyckvgf yqwt cttkxcn hqt vqq nqpi, jqy fq yqw vjkpm oqvjgt Uggng yknn hggn yjgp jgt uqp ku dgkpi gzgewvgf?\nTranslation: We awaited your arrival for too long, how do you think mother Seele will feel when her son is being executed?\n", "<At this point, you see Ruh is boiling of anger, and stabs the general>\n", "<The rest of the keepers are alerted now, and are on the pursuit to attack Ruh>\n", "<You now have to help him fight the dwellers off. You are suspicious of what happened, but you cannot risk compromising the mission>\n"]
    missionPart2Dia=["Ruh:\n*panting*\n", "Ras:\nWhat...was that?\n", "Ruh:\nI...don't know...I just knew he was going to try to kill me so I had to take action, these dwellers aren't exactly friendly\n", "Ras:\nBut we're here on a peaceful mission, to observe, not to kill.\n", "Ruh:\nRas, I don't know what to tell you, it was us dying or them, not like we can understand what they're saying anyways, and not like they'll listen to what we have to say either.\n", "<You notice Ruh is bleeding from his abdomen>\n", "Ras:\nWoah woah there, you're bleeding. Here, let me patch you up.\n", "Ruh:\nOh, oh damn, I didn't notice that, must've been the flight or fight response yeah? Haha\n", "Ras:\nYeah, here...this'll do the trick\n", "<You take a clothe from your bag and wrap it around his abdomen, tying the knot to prevent any further bleeding>\n", "Ruh looks up and sees that the sun is setting\n", "Ruh:\nI think we should make a camp, yeah? We'll continue the mission at dusk.\n", "Ras:\nAlright, yeah. I agree.\n", "<As Ruh begins to make the camp and set up the tents, you notice that it eerily looks familiar to the camp you saw the keepers settling in a few days back>\n", "<At this point, your suspicions have been partially confirmed; could Ruh be a dweller in disguise?>\n", "Ruh is sitting on a tree stump tending to the fire, and you pick up his spear and inch towards him\n", "Ruh:\nHey, can you do me a favor? We need some water for the food, so can you fetch some from the lake?\n", "<Unbeknownst to you, Ruh has untied the knot for the clothe around him>\n", "<He peeks back; seeing that you're holding a spear aimed towards him>\n", "<He isn't surprised, and goes back to tending to the fire>\n", "Ruh:\nI knew this day would come some day, even the sun has to set, doesn't it?\n", "Ras:\n*trembling* Who...who...are you? SPEAK, NOW!\n", "Ruh:\nBack in Wahran, if one of us wasn't of pure blood or had limited effects of the curse, it was mandatory to become an infiltrator. So that's what I did, I came to Esperanca as an infiltrator.\n", "Ruh:\nBut the insane part is, when I went to the townhall as a quote unquote refugee, a man named Reyes sensed something in me, and after that meeting, he came up to me and told me: “Hey, if you do anything funny, I'll slice your throat”\n", "Ras:\nGet....to...the...POINT.\n", "<He peeks once again, still unsurprised>\n", "Ruh:\nIf you want to stab me, go for it, but I don't think Reyes would approve...\n", "Ras:\nWhat are you trying to say?\n", "Ruh:\nEventually, I found my life and soul, Eva, how could I betray the land that made me human? \n", "Ruh:\nI knew Reyes was breathing down my neck every step of the way, turns out, he was half dweller too, his father had a similar story to me. I couldn't really do anything, but that just made me realize that humanity is bliss. I told the truth to Reyes, and we made a small visit to dementia, where she gave me the cure.\n", "Ruh:\nTime and time went by, I had a beautiful daughter, and Reyes had a beautiful son with Eva's friend, Esmeralda.\n", "<At this point, you freeze and drop the spear>\n", "<You creep towards Ruh, standing in front of him>\n", "Ras:\n*trembling* My...mother....?\n", "<Ruh looks up to you>\n", "Ruh:\nYes. Julien was Reyes and Reyes was Julien. He wasn't a traitor, his father was one of the original dwellers and knew who would exactly be the daybringer, and he told that to him on his deathbed. Turns out, Reyes was a bit soft hearted and panicked.\n", "<You sit on the tree stump opposite to Ruh's, still trying to process what is happening>\n", "Ruh:\nHe left me a note before he left, where he said that he was going out in search of the truth, going to wander the lands and consult different scrollwriters to double check the prophecy.\n", "Ruh:\nEventually, he settled in Ayutthaya. He used to still send me letters y'know? The head scrollwriter of the village knew about Reyes and you, and he let you guys stay, eventually becoming the village chief.\n", "Ras:\nIt...can't be...I'm not.... \n", "Ruh:\nHeh, you are though. Born of both worlds, that anger you had for me.... that's just the blood flaring son. I awaited your arrival for a very, very long time.\n", "Ras:\nDoes...anyone...else know?\n", "Ruh:\nNo, only I knew, me and Reyes became really good friends, he was a brilliant scrollwriter too, very scholarly. Kind of paved the way for me to take his position of secretary to the Councilor.\n", "Ras:\nI can't believe it, I really can't...why is this happening?\n", "<You notice Ruh removing his hand from his abdomen; it is flooded with blood>\n", "Ruh:\nT..t..tell Eva and...Mila...that I lov-\n", "Ruh then collapses; you get up quickly to support him in your arms\n", "Ruh:\nHeh...*coughs*...heh...go...daybringer.\n", "<At this point, Ruh passes out, and you are left frozen, how is it that the man who supported is gone?>\n"]

    printDialogues(missionPart1Dia)
    keeperSwordsman=doBattle(50,"Keeper Swordsman","The Keeper missed an attack on you, lucky you!",0,(1,6),0.1)
    if keeperSwordsman<=0:
        keeperArcher=doBattle(75,"Keeper Archer","The Keeper missed an attack on you, lucky you!",0,(1,12),0.3)
    
    if keeperSwordsman<=0 and keeperArcher<=0:
        printDialogues(missionPart2Dia)
        player.xp+=100
        player.currentMission+=1
        print(f'You have been granted 100XP for successful mission completion, your new balance is {player.xp}')




