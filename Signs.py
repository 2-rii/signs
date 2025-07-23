import time
import os
import random
import RexC

#Rex..

class Player:
    def __init__(self):
        self.name="Ras"
        self.xp=0.0
        self.maxStamina=100.0
        self.currentStamina=0.0
        self.maxHealth=100.0
        self.currentHealth=100.0
        self.inventory={}
        self.weapons={}
        self.spawnRoom="Home"
        self.currentRoom="Home"
    
    def death(self):
        self.currentRoom="Home"
        self.currentHealth=self.maxHealth
        print(f'Yikes, you took a heavy fall there, you\'re back to {self.maxHealth} health and of course, safe and sound at home')
    
    def takeDamage(self,DamageTaken:float):
        if DamageTaken>=self.currentHealth:
            self.death()
        else:
            self.currentHealth-=DamageTaken
            print(f'Ouch! You took {DamageTaken} damage, you have {self.currentHealth} health left')
    
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
            return True
        else:
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
        erCount=0
        drink=input("What would you like to get today?: ")
        while (drink not in self.bar) and (erCount<5):
            erCount+=1
            drink=input("Sorry, please enter a valid drink option: ")
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
        erCount=0
        self.displayShop()
        potionName=input("Please enter the name of the potion you would like to buy: ")
        while (potionName not in self.shop) and (erCount<5):
            potionName=input("Sorry, please enter a valid potion name: ")
            erCount+=1

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
        erCount=0
        print("Welcome...to Dementia's Domicile")
        time.sleep(0.5)
        print(f'Dementia the Witch: \n{random.choice(self.enterDia)}')
        print(f'Dementia the Witch: \n{random.choice(self.greetDia)}')
        print(f'Dementia the Witch: \nI have a rather...special offer for you my dear...why don\'t you join me in a game of Rex? No harm in it, you win you get something, you lose...I get something. Of course you don\'t have to, but it\'s up to you...')
        playornot=input("So...what will it be? Rex or Buy? (R/B): ")
        while (playornot.lower() not in ["r","b"]) and (erCount<5):
            playornot=input("Please enter a valid choice (R or B): ")
            erCount+=1
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
        erCount=0
        self.displayShop("p")
        blade=input("Please input the full name of the item you would like to buy: ")
        while (blade not in self.shop) and (erCount<5):
            blade=input("Sorry, that is an invalid option, please enter the name of the item again: ")
            erCount+=1
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
        erCount=0
        player.displayWeapons()
        weapon=input("Please input the weapon to be upgraded (battle code): ").upper()
        while (weapon not in player.weapons) and (erCount<5):
            weapon=input("Please input a valid weapon (its battle code): ").upper()
            erCount+=1
        if weapon in player.weapons:
            return weapon
        else:
            return None

    def upgrade(self,player):
        weapon=self.selectWeapon(player)
        if weapon!=None:
            erCount=0
            self.displayShop("u")
            upgrade=input("Please input the full name of the upgrade you want: ").lower()
            while (upgrade not in self.upgrades) and (erCount<5):
                upgrade=input("Please input a valid upgrade name: ").lower()
                erCount+=1
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
        erCount=0
        print(random.choice(self.enterDia))
        print(random.choice(self.greetDia))
        choice=input("Would you like to upgrade or purchase something? (U/P): ")
        while (choice.lower() not in ["u,p"]) and (erCount<5):
            choice=input("Please input a valid option from U or P: ").lower()
            erCount+=1
        if choice=="p":
            self.purchase()
        elif choice=="u":
            self.upgrade()
        else:
            print("Riz fell asleep whilst waiting for you to choose an upgrade, try again later")

class Trader:
    def __init__(self):
        self.name="Alara the Trader"
        #self.recieve contains items Alara can recieve, and self.give contains items the player can give, pairs are later randomly chosen from both lists (3 pairs ig), this is for the trading interaction
        #Items in the format itemname:amount to recieve or give. Dicts are limited as of right now due to the scale of the game.
        self.recieve={"sticks":25, "stones":25, "esparancan fabric":15, "potion of epiphany":1, "hunting spear":1, "dweller fabric":10 }
        self.give={"blade of honor":1, "potion of healing":1, "sticks":20, "stones":20, "ayutthayan fabric":10, "farben fabric":5 }
        #Trading system needs a rehaul work later
        #self.sell will use an external file containing all items to value them, which is another thing to work on
        self.sell={}
        





player=Player()
kaiser=Bartender()





print("The dark lingers...")
time.sleep(0.5)
lORo=input("Would you like to start a new game or load a previous one?: ")

while "new" not in lORo.lower() and "load" not in lORo.lower():
    lORo=input("Sorry, can you try again?: ")

