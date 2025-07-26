import time
import os
import random
import RexC
import ItemsList

#Rex..

def validateInput(prompt,errorPrompt,valid_options,maxTries=5,transform=str.lower):
    erCount=0
    inp=transform(input(prompt))
    while (inp not in valid_options) and (erCount<maxTries):
        inp=transform(input(errorPrompt))
        erCount+=1
    return inp if inp in valid_options else None

class Player:
    def __init__(self,name="Ras",xp=50.0,maxStamina=100.0,currentStamina=100.0,maxHealth=100.0,currentHealth=100.0,inventory={},weapons={},potions={},spawnRoom="Home",currentRoom="Home",currentMission=1):
        self.name=name
        self.xp=xp
        self.maxStamina=maxStamina
        self.currentStamina=currentStamina
        self.maxHealth=maxHealth
        self.currentHealth=currentHealth
        self.inventory=inventory
        self.weapons=weapons
        self.potions=potions
        self.spawnRoom=spawnRoom
        self.currentRoom=currentRoom
        self.currentMission=currentMission
    
    def death(self):
        self.currentRoom="Home"
        self.currentHealth=self.maxHealth
        print(f'Yikes, you took a heavy fall there, you\'re back to {self.maxHealth} health and of course, safe and sound at home')
    
    def takeDamage(self,DamageTaken:float):
        if DamageTaken>=self.currentHealth:
            self.death()
            return True
        else:
            self.currentHealth-=DamageTaken
            print(f'Ouch! You took {DamageTaken} damage, you have {self.currentHealth} health left')
            return False
    
    def heal(self,healAmount:float):
        healthDiff=self.maxHealth-self.currentHealth
        if healthDiff<healAmount:
            self.currentHealth=self.maxHealth
        else:
            self.currentHealth+=healAmount
        print(f'Ahh, that was replenishing wasn\'t it? Your new health is {self.currentHealth}')
    
    def deductXP(self,XP:float):
        if self.xp>=XP:
            self.xp-=XP
            print(f'You have spent {XP}XP, your new balance is: {self.XP}')
            return True
        else:
            return False
    
    def addtoInventory(self,item,amount):
        if item in self.inventory:
            self.inventory[item]+=amount
        else:
            self.inventory[item]=amount
        print(f'{item} has been added to your inventory, you now have {self.inventory[item]} of it.')
    
    def removefromInventory(self,item,amount):
        if (item in self.inventory) and (self.inventory[item]>=amount):
            self.inventory[item]-=amount
            return True
        else:
            print("You do not have enough of this item in your inventory!")
        if self.inventory[item]==0:
            del self.inventory[item]
        return False

    def addStamina(self,staminaAmt:float):
        staminaDiff=self.maxStamina-self.currentStamina
        if staminaAmt>=staminaDiff:
            self.currentStamina=self.maxStamina
        else:
            self.currentStamina+=staminaAmt

    def displayWeapons(self):
        print("\n")
        print("~~~~~~~Your Weapons~~~~~~~")
        for i in self.weapons:
            print(f'{self.weapons[i][3]}- Damage per Hit: {self.weapons[i][0]}, Current Durability: {self.weapons[i][1]}, Max Durability: {self.weapons[i][2]}, Battle Code: {i}')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def changeRoom(self,area:str):
        self.currentRoom=area

class Bartender:
    def __init__(self):
        self.name="Kaiser the Bartender"
        #In the bar, the variables in the list signify [XP Cost, Stamina Increase, Health Reduction]
        self.bar={"water":[1,5,0],"beer":[2,7.5,0.5],"whiskey":[5,10,1],"vodka":[7.5,25,5]}
        self.enterDia=["*Wiping table and talking to customer* Uff... warum zum Teufel haben sie mir die Dorfkuh weggenommen? Ich hab doch nix gemacht, ehrlich... schwör ich! \nEnglish Translation: Ugh...why'd they have to take the village cow away from me? I wasn't doing anything to it, I swear on it.",
                       "Man sagt ja, die hellsten Flammen brennen am schnellsten aus... Ich hab mein ganzes Leben hier vergeudet... Hätt auf meinen Onkel hören und in Bremen bleiben sollen. \nEnglish Translation: They say the brightest flames die fast... I wasted my whole life here.. I should've listened to my uncle and stayed in Bremen.",
                       "GENAU deswegen hätt ich in Bremen bleiben sollen... so ’ne Verschwendung von meinem Talent, hier in diesem Drecksnest... und dann auch noch, dass meine einzige Liebe ’ne Kuh war... \nEnglish Translation: THIS is EXACTLY why I should've stayed in Bremen....what a waste of my talent in this useless village... doesn't help that my only love is a cow...",
                       "*Drunkenly* Am Leben…?! ICH LEB NOCH?!? \nEnglish Translation: Alive.......! I'M STILL ALIVE!?!?"]
        self.greetDia=["Oh, dich hab ich gar nicht kommen sehn... Was darf's sein, Ras? \nEnglish Translation: Oh, I didn't see you there, what can I get you Ras?",
                      "Oh, sorry... Was kriegen wir heut, Chef? \nEnglish Translation: Oh sorry there, what can I get you sir?",
                      "Na dann... Womit betäuben wir heut den Schmerz? \nEnglish Translation: Alright there, what we getting to numb the pain?"]
        self.choiceDia=["Joah, der hier haut rein. \nEnglish Translation: Yeah, this one gets the job done...",
                        "Na dann, wie du meinst. \nEnglish Translation: Welp, suit yourself",
                        "Ah ja, der Liebling vom Dorf. \nEnglish Translation: Ah yes, the village favorite.",
                        "Meinst du, ich hab ’ne Chance bei der Kuh...? \nEnglish Translation: You think I can get back with the cow...?",
                        "Den hier wirst du lieben. \nEnglish Translation: You're going to love this one", "Wirklich...? \nEnglish Translation: Really...?"]
        self.negativeDia=["Wer kein Geld hat, soll den Mund halten. \nEnglish Translation: If you can't afford it, don't ask for it.", "Komm wieder, wenn du nicht mehr pleite bist. \nEnglish Translation: Come back when you can afford it.",
                          "Kaiser ist kein Freund von denen, die nicht zahlen. \nEnglish Translation: Kaiser isn't a friend of those who don't pay.", "Du kannst dir das nicht leisten? Wirklich? \nEnglish Translation: You can't afford this? Really?"]
    
    def displayBar(self):
        print("\n")
        print("~~~~~Kaizer's Bar~~~~~")
        for i in self.bar:
            print(f'Drink:{i}, XP Cost:{self.bar[i][0]}, Stamina Increase:{self.bar[i][1]}, Health Reduction:{self.bar[i][2]}')
        print("~~~~~~~~~~~~~~~~~~~~~~~")

    def drinkServe(self,player):
        print(random.choice(self.greetDia))
        self.displayBar()
        drink=validateInput("What would you like to get today?","Sorry,please enter a valid drink option: ",self.bar)
        if drink in self.bar:
            if player.deductXP(self.bar[drink][0]):
                print(random.choice(self.choiceDia))
                player.addStamina(self.bar[drink][1])
                if player.currentHealth-self.bar[drink][2]<=0:
                    player.death()
                else:
                    player.takeDamage(self.bar[drink][2])
                return 1
            else:
                print(random.choice(self.negativeDia))
                return 0
        else:
            print("Kaiser doesn't have enough time or energy for your shenanigans, try again later.")
            return 0

class Witch:
    def __init__(self):
        self.name="Dementia the Witch"
        #Shop items in the form item:[XP Cost, Stamina Increase, Max Stamina Increase, Health Increase, Max Health Increase]
        self.shop={"Potion of Healing":[3,10,0,30,0], "Potion of Epiphany":[6,15,0,50,0], "Bastardized Potion of Healing": [15,30,0,50,5], "Bastardized Potion of Epiphany":[40,40,10,100,10], "Potion of Tenacity":[15,40,0,0,0], "Cursed Potion of Tenacity":[35,100,20,30,0]}
        self.enterDia=["*Talking to herself* Dark is the night in which the moon holds its solace…","*Reading a spellbook* Ahh so…that’s how it works?!? I hope that customer doesn’t notice that I gave them a potion of grieving rather than a potion of believing… ", "*Making potions* One rabbit…another hoof of a horse….Kaiser’s cow….and a dash of salt..."]
        self.greetDia=["Ahh…welcome Ras! I didn’t see you there, what can I brew up for you today?", "So, Kaiser’s remedies didn’t work, right? I know…What can I get you?", "There’s my favorite customer, what do your needs desire today?", "Looking for a high, or a heal? What can I offer you?"]
        self.choiceDia=["Yes…this one’s my personal favorite..for no apparent reason of course.","Good choice…coming right up.","No questions asked, no take backs, alright? Here you go.","Better than anything Kaiser has to offer, right? "]
        self.negativeDia=["If I wasn’t so nice, I’d curse you with the same stuff we use on the forest dwellers. Come back when you have more XP","Dementia doesn’t forget, remember that. You don’t want to make a very powerful enemy, come back when you aren’t the portrait of despair.", "I’ll forgive you this time, but next time, you better have the XP."]
    
    def playRex(self,player):
        RexC.main()
        res=RexC.checkWin()
        if res==0:
            player.death()
            print(f'You have been penalized {player.xp*0.25} XP for losing Rex, your new balance is {player.xp*0.75}')
            time.sleep(1)
            player.xp*=0.75
        elif res==1:
            print(f'Congratulations on winning Rex...you are one of the lucky few, for your triump, you have been granted {player.xp*0.25} XP, your new balance is {player.xp*1.25}')
            time.sleep(1)
            player.xp*=1.25
            if "Potion of Epiphany" in player.inventory:
                player.inventory["Potion of Epiphany"]+=1
            else:
                player.inventory["Potion of Epiphany"]=1
        else:
            print("You escaped while you could, it's best you don't come back to this...or you can...it's all up to you.")
            time.sleep(1)
    
    def displayShop(self):
        print("\n")
        print("~~~~~~~Dementia's Domicile~~~~~~~~")
        for i in self.shop:
            print(f'{i}- XP Cost: {self.shop[i][0]}, Stamina Increase: {self.shop[i][1]}, Max Stamina Increase: {self.shop[i][2]}, Health Increase: {self.shop[i][3]}, Max Health Increase: {self.shop[i][4]}')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            

    def buyPotion(self,player):
        self.displayShop()
        potionName=validateInput("Please enter the full name of the potion you want to buy: ", "Sorry, please enter a valid potion name: ", self.shop)

        if potionName in self.shop:
            if player.deductXP(self.shop[potionName][0]):
                player.maxStamina+=self.shop[potionName][2]
                player.maxHealth+=self.shop[potionName][4]

                player.heal(self.shop[potionName][3])
                player.addStamina(self.shop[potionName][1])
                    
                print(random.choice(self.choiceDia))
                return 1
            else:
                print(random.choice(self.negativeDia))
                return 0
        else:
            print("Dementia got annoyed of the repeated attempts to anger her, try again later")
            return 0
        
    def playorbuy(self,player):
        print("Welcome...to Dementia's Domicile")
        time.sleep(0.5)
        print(f'Dementia the Witch: \n{random.choice(self.enterDia)}')
        print(f'Dementia the Witch: \n{random.choice(self.greetDia)}')
        print(f'Dementia the Witch: \nI have a rather...special offer for you my dear...why don\'t you join me in a game of Rex? No harm in it, you win you get something, you lose...I get something. Of course you don\'t have to, but it\'s up to you...')
        playornot=validateInput("So...what will it be? Rex or Buy? (R/B)", "Please enter a valid choice (R or B)", ["r,b"],3)
        if playornot.lower()=="r":
            self.playRex(player)
        elif playornot.lower()=="b":
            self.buyPotion(player)
        else:
            print("Dementia got annoyed of the repeated attempts to anger her, try again later")

class Weaponsmith:
    def __init__(self):
        self.name="Riz the Weaponsmith"
        #Shop items in the format weapon:[XP Cost, Damage Dealt, Durability, Game Short Form (for battles)]
        self.shop={"blade of honor":[15,15,30,"BH"], "blade of glory":[15,30,15,"BG"], "blade of the east":[30,30,30,"BE"], "blade of severance":[60,40,100,"BS"], "ayutthayan crossbow":[5,5,20,"AC"], "riz's bow":[10,10,20,"RB"], "axe of the millions":[15,20,5,"AM"], "the reaper's dagger":[2,5,10,"RD"], "caroline's mace":[20,30,2,"CM"], "hunting spear":[1,5,10,"HS"]}
        #Upgrade items in the format name:[XP cost, Damage Increase, Durability Increase (only if damaged)]
        self.upgrades={"dementia's curse":[5,5,0], "the liquid of uncertainty":[5,0,10], "the liquid of doubt":[10,5,15], "the dweller's intuition":[20,10,20], "secrets of the void":[30,15,40], "voices of catharsis":[15,0,40], "messer's kuss":[15,15,0]}
        self.enterDia = ["*Talking to customer* Hey, handle that with care aight? Don’t want you slicing off another finger this time yeah?", "*Sharpening a sword* A warrior looks best when his reflection is stained in blood…", "*Practicing with a dagger* Still got it.", "*Talking to the customer* Pacifism is overrated, isn’t it?", "*Talking to himself* Them Ayutthayans just don’t know how to do it, damn it."]
        self.greetDia = ["Oh, what’s up Ras? What’ll it be today, sticks or stones?", "There’s my favorite customer, how you doing man? What can I do for you today?", "You’ve come to the right place today Ras, what can I get for you?", "So, Kaiser and Dementia let you down again? I would never heh, what can I do for you today?"]
        self.choiceDiaU = ["Good choice, one upgrade coming right up!", "So, stones, it is, good choice.", "You did the right thing, I wouldn’t abandon a preciousness like this either", "See that new shine? It’ll help you glimmer in the battlefield once you raise it, call it the warrior’s triumph"]
        self.choiceDiaP = ["Smart choice, this one definitely gets the job done.", "Remember, the blade chose you, you didn’t choose it.", "I don’t think you’ll be back for a while, after all, nobody does it like the Esperancans. Make it worthwhile.", "Don’t worry, I won’t let the Elder know you bought this heh…", "You, my friend, are a smart individual, coming right up."]
        self.negativeDia = ["It’s alright friend, I’ll keep it reserved, come back when you have more XP yeah?", "Yeah…so the thing is…I got mouths to feed so I need XP to do this stuff…don’t worry yeah? Come back when you have more.", "I wish I could give you a discounted rate, but the Councilor’s messing with my business model, if he wasn’t so high up, I’d do something, you get me? But yeah, sorry man, come back when you got more XP.", "Good selection, but unfortunately you’re a bit short on XP, so come back when you have the required amount yeah?"]

    def displayShop(self,choice:str):
        print("\n")
        print("~~~~~~~Riz's Dungeon~~~~~~~")
        if choice=="p":
            for i in self.shop:
                print(f'{i}- XP Cost: {self.shop[i][0]}, Damage Dealt Per Hit: {self.shop[i][1]}, Durability: {self.shop[i][2]}, Short Form: {self.shop[i][3]}')
        else:
            for i in self.upgrades:
                print(f'{i}- XP Cost: {self.upgrades[i][0]}, Damage Increase: {self.upgrades[i][1]}, Durability Increase: {self.upgrades[i][2]}')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    def purchase(self,player):
        self.displayShop("p")
        blade=validateInput("Please input the full name of the item you would like to buy: ", "Sorry, that is an invalid option, please enter the name of the item again: ", self.shop)
        if (blade in self.shop) and (blade not in player.weapons):
            if player.deductXP(self.shop[blade][0]):
                print(random.choice(self.choiceDiaP))
                # Damage/hit, current Dura, max Dura, name
                player.weapons[self.shop[blade][3]]=[self.shop[blade][1],self.shop[blade][2],self.shop[blade][2],blade]
                return 1
            else:
                print(random.choice(self.negativeDia))
        elif blade in player.weapons:
            print("You already have this weapon, you can't stack them...")

        else:
            print("Riz got tired of waiting and fell into a nap, try again later.")
        return 0
    
    def selectWeapon(self,player):
        player.displayWeapons()
        weapon=validateInput("Please input the weapon to be upgraded (battle code): ", "Please input a valid option (its battle code): ", player.weapons,5,str.upper)
        weapon=input("Please input the weapon to be upgraded (battle code): ").upper()
        if weapon in player.weapons:
            return weapon
        else:
            return None

    def upgrade(self,player):
        weapon=self.selectWeapon(player)
        if weapon!=None:
            self.displayShop("u")
            upgrade=validateInput("Please input the full name of the upgrade you want: ", "Please input a valid upgrade name: ",self.upgrades)
            if upgrade in self.upgrades:
                if player.deductXP(self.upgrades[upgrade][0]):
                    print(random.choice(self.choiceDiaU))
                    player.weapons[weapon][0]+=self.upgrades[upgrade][1]
                    duraDiff=player.weapons[weapon][3]-player.weapons[weapon][2]
                    if self.upgrades[upgrade][2]>=duraDiff:
                        player.weapons[weapon][1]=player.weapons[weapon][2]
                    else:
                        player.weapons[weapon][1]+=self.upgrades[upgrade][2]
                    return 1
                else:
                    print(random.choice(self.negativeDia))
            else:
                print("Riz fell asleep whilst waiting for you to choose an upgrade, try again later")
        else:
            print("Well, you can't really upgrade a weapon if you don't have it right? Try again later")
        return 0
    
    def uporbuy(self):
        print(random.choice(self.enterDia))
        print(random.choice(self.greetDia))
        choice=validateInput("Would you like to upgrade or purchase something? (U/P): ", "Please input a valid option from U or P: ", ["u","p"])
        if choice=="p":
            self.purchase()
        elif choice=="u":
            self.upgrade()
        else:
            print("Riz fell asleep whilst waiting for you to choose an upgrade, try again later")

class Trader:
    def __init__(self):
        self.name="Alara the Trader"
        #Three random trading pairs are chosen from the list in the format [[giveItem,amt,recieveItem,amt]]
        self.tradingPairs=[["wool",5,"rope",1],["paper",10,"empty book",1],["esperancan fabric",25,"samnan fabric",10],["samnan fabric",30,"potion of healing",1],["esperancan fabric",25,"dweller fabric",3],["dweller fabric",5,"hunting spear",1],["sticks",20,"stones",15],["stones",30,"the reaper's dagger",1]]
        #for selling & buying, the sell_price and buy_price are used from ItemsList.py and 3 items are randomly selected at a time to buy n sell
        self.enterDia=["*Talking to herself* Ahh, I just love this village, so MUCH business to do…heh…","*Talking to a customer* Look, you aren’t going to find a better price elsewhere, either you give the garment to me or you stop wasting my time.","*Talking to a customer* Well, I’m not paying THAT much for…whatever this is….actually, you can keep it.","*Looking through her inventory* Somehow, business has been amazing ever since Farben got plundered, I mean, I’m not complaining."]
        self.greetDia=["Oh hey there Ras, good morning! What can I do for you today?","Ahh, didn’t see you there, so what will it be today, a lengthy bargain or a civil barter?","There’s the village golden boy, how’s Esperanca treating you? I bet it's better than Ayutthaya. Anything I can do for you today?","There’s nothing I don’t have in stock, what can I do for you today Ras?"]
        self.barterPositiveDia=["Ahh, I love me a good deal, had a nice time doing business with a person who knows what to bring to the table.","Just like how our ancestors have been doing it for centuries now, right?","Now this is the kind of exchange that floats our economy, you get something, I get something. Great doin’ business with you."]
        self.sellPositiveDia=["Ahh yes…making the most out of the spoils of war…I see… no shame though, everyone’s gotta make a living right?","Another item to add to my already large collection, spread the word will ya? Mention that I don’t ask any questions too…you get me? Keeps the business afloat…","Appreciate you selling this to me, I was looking for it a while now, glad I didn’t have to go down to Samnan to get it and instead had an angel hand deliver it to me…heh"]
        self.buyPositiveDia=["Mmm…I just love the sound of XP, well it was amazing doing business with you, I guess the Ayutthayans are really more civilized.","I got you a good deal for that huh? Spread the word, will ya?","Well, that’s another item off the shelves, but I trust you’ll take good care of it…"]
        self.negativeDia=["Well, I can’t really do that, you see…you just don’t have enough. Come back when you have enough of the item.","You know that this is not how a transaction works, the deal is that you bring a specified amount of something and I give you something in return for it, you better come back next time with the proper amount.","It’s alright, the item isn’t going anywhere, unless it does…then whoops, come back later and try again.","Did you just…try to lowball me? Intentional or not, you don’t want to lose the best trader in the entire village."]

    def displayShop(self,choice:str,items:list):
        print("\n")
        print("~~~~~~~Alara's Marketplace~~~~~~~")
        allItems=ItemsList.weapons|ItemsList.items|ItemsList.potions
        if choice=="t":
            print("Items available for trade: ")
            for i in range(len(items)):
                print(f'{i+1}- You give {items[i][1]}x {items[i][0]} for {items[i][3]}x {items[i][2]}')
        elif choice=="b":
            print("Items available for buying: ")
            for i in range(len(items)):
                print(f'{i+1}- {items[i]} for {allItems[items[i]]["buy_price"]}XP')
        else:
            print("Items that Alara is willing to buy: ")
            for i in range(len(items)):
                print(f'{i+1}- {items[i]} for {allItems[items[i]]["sell_price"]}XP')
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def pickItems(self, SBorT):
        its=[]
        if SBorT=="t":
            for i in range(3):
                rdm=random.choice(self.tradingPairs)
                while rdm in its:
                    rdm=random.choice(self.tradingPairs)
                its.append(rdm)
        else:
            available=ItemsList.items.keys()
            for i in range(3):
                rdm=random.choice(available)
                while rdm in its:
                    rdm=random.choice(available)
                its.append(rdm)
        return its
    
    def trade(self,player):
        tradingPairs=self.pickItems("t")
        self.displayShop("t",tradingPairs)
        choice=validateInput("Please enter the number of the trade you would like to carry out: ", "Sorry, please enter a valid number from 1-3: ", ["1","2","3"])
        if choice in ["1","2","3"]:
            choice=int(choice)-1
            chosenPair=tradingPairs[choice]
            if chosenPair[2] not in player.weapons:
                if player.removefromInventory(chosenPair[0],chosenPair[1]):
                    print(random.choice(self.barterPositiveDia))
                    player.addtoInventory(chosenPair[2],chosenPair[3])
                else:
                    print("Well...you don't really have enough to offer now, do ya?")
            else:
                print("Woah woah calm down there...you can't stack weapons around here...")
        else:
            print("Alara got tired of waiting for you to choose and had 'other business to attend to'")

    def buy(self,player,):
        buyOptions=self.pickItems("b")
        self.displayShop("b",buyOptions)
        choice=validateInput("Please enter the number of the item you would like to buy from the list: ", "Sorry, please enter a valid number between 1-3: ", ["1","2","3"])
        if choice in ["1","2","3"]:
            choice=int(choice)-1
            buyingProd=buyOptions[choice]
            if player.deductXP(ItemsList.items[buyingProd]["buy_price"]):
                player.addtoInventory(buyingProd,1)
                print(random.choice(self.buyPositiveDia))
            else:
                print(random.choice(self.negativeDia))
        else:
            print("Alara got tired of waiting for you to choose and had 'other business to attend to'")
    
    def sell(self,player):
        sellOptions=self.pickItems("s")
        self.displayShop("s",sellOptions)
        choice=validateInput("Please enter the number of the item you would like to sell from the list: ", "Sorry, please enter a valid number between 1-3: ", ["1","2","3"])
        if choice in ["1","2","3"]:
            choice=int(choice)-1
            sellingProd=sellOptions[choice]
            if player.removefromInventory(sellingProd,1):
                print(random.choice(self.sellPositiveDia))
                player.xp+=ItemsList.items[sellingProd]["sell_price"]
            else:
                print(random.choice(self.negativeDia))
        else:
            print("Alara got tired of waiting for you to choose and had 'other business to attend to'")
    
    def sellbuyortrade(self):
        print(random.choice(self.enterDia))
        print(random.choice(self.greetDia))
        choice=validateInput("Would you like to sell something, buy or trade today? (S or B or T): ", "Please select a valid option from S, B or T: ", ["s","b","t"])
        if choice in ["s","b","t"]:
            if choice=="s":
                self.sell()
            elif choice=="b":
                self.buy()
            else:
                self.trade()
        else:
            print("Alara got tired of waiting for you to choose and had 'other business to attend to'")


class otherNPCs:
    def __init__(self):
        self.player=player
    
    def homelessMan(self):
        print("<You look towards a lamp post and see a homeless man resting on it>\n")
        time.sleep(0.65)
        print("<He looks at you>\n")
        time.sleep(0.35)
        print("Homeless Man:\nHey psst…come here…\n")
        time.sleep(0.4)
        print("Homeless Man:\nHey hey…you know…the end of the world is near…heheh….there is no worth in life or death…we are ALL going to die soon….HEH\n")
        time.sleep(0.2)
        print("Ras:\nSorry?\n")
        time.sleep(0.2)
        print("Homeless Man:\nArrrghhh why don’t you get it? We’re ALL going to DIE the end of the world as we know it is COMING\n")
        time.sleep(0.2)
        print("Ras:\nAnd…how do you know that?\n")
        time.sleep(0.2)
        print("Homeless Man:\nWell, my friend told me that it’s going to end…and I believe his intuition, smart guy really…\n")
        time.sleep(0.2)
        print("Ras:\nYeah…I don’t think so…\n")
        time.sleep(0.2)
        print("Homeless Man:\nArrgh you are all ignorant people…here…take this book written by my friend…read it and you’ll understand what I’m talking about….\n")
        time.sleep(0.2)
        print("<You open the book and it’s empty; there is nothing on any of the pages>")
        time.sleep(0.35)
        print("Homeless Man:\nYeah…you can keep that copy…spread the word…let EVERYONE know about the future…\n")
        time.sleep(0.2)
        print("Ras:\nUhh...yeah sure...\n")
        self.player.addtoInventory("empty book",1)
    
    def oldMan(self):
        print("<As you are walking towards the marketplace, you see an old man struggling to carry his groceries>")
        time.sleep(0.45)
        print("<You promptly run over to him, intending to help him>")
        time.sleep(0.2)
        print("Ras:\nSir, sir, let me help you there…\n")
        time.sleep(0.2)
        print("Old Man:\nReyes…is that you?\n")
        time.sleep(0.2)
        print("Ras:\nAhh…no sir, I’m Ras…can I help you with those bags?\n")
        time.sleep(0.2)
        print("Old Man:\nWell…aren’t you a kind soul?\n")
        time.sleep(0.2)
        print("<You take a few bags from him and start walking with him, matching his pace>")
        time.sleep(0.2)
        print("Old Man:\nAre you from around here son…? I’ve never seen you at any of our festivals…\n")
        time.sleep(0.2)
        print("Ras:\nNo sir…I’m an explorer hailing from Ayutthaya, I’m on a mission to learn more about the forest dwellers.\n")
        time.sleep(0.2)
        print("<He promptly looks at you>")
        time.sleep(0.2)
        print("Old Man:\nYou bear a very similar resemblance to one of my colleagues from back in the days…it’s exactly the same features too…\n")
        time.sleep(0.2)
        print("Ras:\nHaha sir, it’s alright, I get mistaken for a lot of people from time to time, I guess it’s my fate\n")
        time.sleep(0.2)
        print("Old Man:\nAhaha, you have a point there\n")
        time.sleep(0.1)
        print("Old Man:\nHere we are, can you help me to open the door son?\n")
        time.sleep(0.2)
        print("Ras:\nYes, yes of course\n")
        time.sleep(0.2)
        print("<You open the door to the house; it’s a humble cabin like yours, but with an interesting difference>")
        print("<The Old Man walks in to the house and puts the groceries on a table, and you do the same>")
        time.sleep(0.3)
        print("Ras:\nYou have a nice collection on the fireplace, are those like trophies of some sort?\n")
        time.sleep(0.2)
        print("Old Man:\nAhh…haha…yes they are,I served in the cavalry back in the days, my unit had successfully fended off a major dweller attack back in the days, and so we were awarded for it…\n")
        time.sleep(0.2)
        print("Old Man:\nBut then…I just got weaker, and took my leave from the army. Eventually though…I found work in the townhall, working alongside a fella named Reyes…yeah he was a kind soul…until he disappeared…\n")
        time.sleep(0.2)
        print("Ras:\nWow…I’m honestly impressed\n")
        time.sleep(0.2)
        print("Old Man:\nWhy? You think an Old Man like me can’t achieve stuff like this? Hehe\n")
        time.sleep(0.2)
        print("Ras:\nNo no, not that, it’s all really amazing stuff\n")
        time.sleep(0.2)
        print("Old Man:\nAhh, yes, I do agree on that…thank you for helping me son…here, take some XP\n")
        time.sleep(0.2)
        print("Ras:\nNo no sir, I can’t take your money\n")
        time.sleep(0.2)
        print("Old Man:\nArrrgh don’t worry about it, I can’t take it to the grave, here, take some…\n")
        time.sleep(0.1)
        print("<The Old Man gives you 35XP for helping him out; kindness truly has its rewards>")
        self.player.xp+=35
        time.sleep(0.1)
        print("Ras:\nThank you so much sir…I hope to see you around\n")
        time.sleep(0.2)
        print("Old Man:\nAhaha, goodbye! \n")

player=Player()
