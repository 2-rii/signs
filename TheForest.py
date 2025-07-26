#Missions for the forest stage

from Signs import validateInput as vl
from Signs import player 

def doPlayerTurn(battleCode,enemyHealth):
    enemyHealth-=player.weapons[battleCode][0]
    player.weapons[battleCode][1]-=1
    if player.weapons[battleCode][1]==0:
        del player.weapons[battleCode]

    return True if enemyHealth<=0 else False

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

