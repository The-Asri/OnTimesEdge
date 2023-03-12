import box
import border
import Player
import ImageAssets

def loadLevel(id, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    if id == 1:
        loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)

def loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 300
    levelBorder.y = 180
    cityBackground = ImageAssets.loadImage(3)
    ruinsBackground = ImageAssets.loadImage(4)

    boxesCity.clear()
    # same
    boxesCity.append(box.Box(0, 100, 150, 100))
    boxesCity.append(box.Box(180, 90, 150, 100))
    # dif

    boxesRuins.clear()
    # same
    # dif
