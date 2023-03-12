import box
import border
import Player

def loadLevel(id, boxesCity, boxesRuins, levelBorder, player):
    if id == 1:
        loadLevel1(boxesCity, boxesRuins, levelBorder, player)

def loadLevel1(boxesCity, boxesRuins, levelBorder, player):
    player.x = 100
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 500
    levelBorder.y = 150

    boxesCity.clear()
    boxesCity.append(box.Box(50, 100, 150, 25))
    boxesCity.append(box.Box(250, 100, 100, 25))
    boxesCity.append(box.Box(370, 70, 100, 50))

    boxesRuins.clear()
    boxesRuins.append(box.Box(50, 100, 150, 25))
    boxesRuins.append(box.Box(250, 100, 100, 25))
    boxesRuins.append(box.Box(170, 85, 100, 50))
