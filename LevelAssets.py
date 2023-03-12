import box
import border
import Player
import ImageAssets

def loadLevel(id, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    if id == 1:
        loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)

def loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 100
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 500
    levelBorder.y = 150
    cityBackground = ImageAssets.loadImage(1)
    ruinsBackground = ImageAssets.loadImage(2)

    boxesCity.clear()
    boxesCity.append(box.Box(50, 100, 150, 25))
    boxesCity.append(box.Box(250, 100, 100, 25))
    boxesCity.append(box.Box(370, 70, 100, 50))

    boxesRuins.clear()
    boxesRuins.append(box.Box(50, 100, 150, 25))
    boxesRuins.append(box.Box(250, 100, 100, 25))
    boxesRuins.append(box.Box(370, 70, 100, 50))
    boxesRuins.append(box.Box(300, 50, 20, 30))
    boxesRuins.append(box.Box(370, 40, 20, 30, "Unslideable"))
