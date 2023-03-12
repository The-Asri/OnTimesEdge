import box
import border
import Player
import ImageAssets

def loadLevel(id, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    if id == 1:
        loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
    if id == 2:
        loadLevel2(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)

def loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 330
    levelBorder.y = 180
    cityBackground = ImageAssets.loadImage(3)
    ruinsBackground = ImageAssets.loadImage(4)

    boxesCity.clear()
    # same
    boxesCity.append(box.Box(0, 100, 150, 100))
    boxesCity.append(box.Box(180, 90, 150, 100))
    boxesCity.append(box.Box(180, -50, 150, 100))
    # dif
    boxesCity.append(box.Box(180, 50, 5, 40, type="Unslideable"))

    boxesRuins.clear()
    # same
    boxesRuins.append(box.Box(0, 100, 150, 100))
    boxesRuins.append(box.Box(180, 90, 150, 100))
    boxesRuins.append(box.Box(180, -50, 150, 100))
    # dif

def loadLevel2(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 300
    levelBorder.y = 150
    cityBackground = ImageAssets.loadImage(1)
    ruinsBackground = ImageAssets.loadImage(2)

    boxesCity.clear()
    #same
    boxesCity.append(box.Box(25, 100, 185, 50))
    boxesCity.append(box.Box(225, 40, 75, 110))
    #dif
    boxesCity.append(box.Box(175, 20, 10, 80))
    boxesCity.append(box.Box(225, 0, 10, 40, "Unslideable"))

    boxesRuins.clear()
    #same
    boxesRuins.append(box.Box(25, 100, 185, 50))
    boxesRuins.append(box.Box(225, 40, 75, 110))
    #dif

