import box
import border
import Player
import ImageAssets

def loadLevel(id, boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    if id == 1:
        loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
    if id == 2:
        loadLevel2(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)
    if id == 3:
        loadLevel2(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)

def loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 350
    levelBorder.y = 180
    cityBackground = ImageAssets.loadImage(3)
    ruinsBackground = ImageAssets.loadImage(4)

    boxesCity.clear()
    # same
    boxesCity.append(box.Box(0, 100, 150, 100))
    # dif
    boxesCity.append(box.Box(180, 90, 170, 100))
    boxesCity.append(box.Box(180, -50, 170, 100))
    boxesCity.append(box.Box(180, 50, 5, 40, type="Unslideable"))

    boxesRuins.clear()
    # same
    boxesRuins.append(box.Box(0, 100, 150, 100))
    # dif
    boxesRuins.append(box.Box(180, 90, 60, 100))
    boxesRuins.append(box.Box(180, -50, 60, 100))
    boxesRuins.append(box.Box(280, 90, 70, 100))
    boxesRuins.append(box.Box(280, -50, 70, 100))
    boxesRuins.append(box.Box(280, 65, 15, 25, type="Unslideable"))

def loadLevel2(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    pass

def loadLevel3(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    pass

