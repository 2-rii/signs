#Rex, the game.
import time
import Signs
import TheForest
import os

print("The dark lingers...")
time.sleep(4)
print("Welcome to...REX")
time.sleep(4)
fileSub="rexData"

lOrO=Signs.validateInput("Would you like to start a new game, load a game or exit? (N,L or E): ","Please enter a valid option from N,L or E",["n","l","e"],999)

if lOrO=="n":
    counter=1
    while os.path.isfile(fileSub+str(counter)+".json"):
        counter+=1
    openedFile=open(fileSub+str(counter)+".json","w")
elif lOrO=="l":
    counter=1
    fileL=[]
    while os.path.isfile(fileSub+str(counter)+".json"):
        fileL.append(fileSub+str(counter))
        counter+=1
    print("~~~~~Your Saves~~~~~")
    for i in fileL:
        print(i)
    print("~~~~~~~~~~~~~~~~~~~~")
    numb=Signs.validateInput("Please enter the number of the save you would like to load","Sorry, please enter a valid number from the list",[str(i[7]) for i in fileL],999)
    openedFile=open(fileSub+numb+".json")
    Signs.player.loadGame(openedFile)

missions={1:TheForest.theFallingMysts,2:TheForest.villageofEsperanca,3:TheForest.betrayalofFate,4:TheForest.thekeepersoftheForest,5:TheForest.thetalesoftheForgotten,6:TheForest.lunarAbyss,7:TheForest.cuiBono,8:TheForest.operationDaybringer,9:TheForest.noMission}

while lOrO!="e":
    missions[Signs.player.currentMission]()
    lOrO=Signs.validateInput("Would you like to continue or exit and save? (C or E): ", "Please enter a valid option from C or E: ",["c","e"],999)
    if lOrO=="e":
        Signs.player.saveGame(openedFile)
