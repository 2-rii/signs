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
        self.shop={"Blade of Honor":[15,15,30,"BH"], "Blade of Glory":[15,30,15,"BG"], "Blade of the East":[30,30,30,"BE"], "Blade of Severance":[60,40,100,"BS"], "Ayutthayan Crossbow":[5,5,20,"AC"], "Riz's Bow":[10,10,20,"RB"], "Axe of the Millions":[15,20,5,"AM"], "The Reaper's Dagger":[2,5,10,"RD"], "Caroline's Mace":[20,30,2,"CM"], "Hunting Spear":[1,5,10,"HS"]}
        #Upgrade items in the format name:[XP cost, Damage Increase, Durability Increase (only if damaged)]
        self.upgrades={"Dementia's Curse":[5,5,0], "The Liquid of Uncertainty":[5,0,10], "The Liquid of Doubt":[10,5,15], "The Dweller's Intuition":[20,10,20], "Secrets of the Void":[30,15,40], "Voices of Catharsis":[15,0,40], "Messer's Kuss":[15,15,0]}


player=Player()
kaiser=Bartender()





print("The dark lingers...")
time.sleep(0.5)
lORo=input("Would you like to start a new game or load a previous one?: ")

while "new" not in lORo.lower() and "load" not in lORo.lower():
    lORo=input("Sorry, can you try again?: ")

