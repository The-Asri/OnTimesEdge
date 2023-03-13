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
        loadLevel3(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)

def loadLevel1(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 350
    levelBorder.y = 180
    cityBackground = ImageAssets.loadImage(7)
    ruinsBackground = ImageAssets.loadImage(8)

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
    player.x = 40
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 380
    levelBorder.y = 200
    cityBackground = ImageAssets.loadImage(1)
    ruinsBackground = ImageAssets.loadImage(2)

    boxesCity.clear()
    #same
    boxesCity.append(box.Box(20, 100, 110, 150))
    boxesCity.append(box.Box(240, 140, 60, 150))
    boxesCity.append(box.Box(320, 110, 100, 150))
    #dif
    boxesCity.append(box.Box(126, 55, 4, 45, "Unslideable"))

    boxesCity.append(box.Box(170, 110, 8, 150, "Unslideable"))
    boxesCity.append(box.Box(150, 115, 20, 12, "Unslideable"))
    boxesCity.append(box.Box(178, 115, 20, 12, "Unslideable"))

    boxesCity.append(box.Box(280, 95, 4, 45))
    boxesCity.append(box.Box(280, 90, 4, 5, "Spike"))
    boxesCity.append(box.Box(305, 0, 10, 20, "Unslideable"))
    boxesCity.append(box.Box(335, 60, 4, 50, "Spike"))

    boxesRuins.clear()
    #same
    boxesRuins.append(box.Box(20, 100, 110, 150))
    boxesRuins.append(box.Box(240, 140, 60, 150))
    boxesRuins.append(box.Box(320, 110, 100, 150))
    #dif
    boxesRuins.append(box.Box(95, 96, 35, 4, "Unslideable"))


def loadLevel3(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 200 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 430
    levelBorder.y = 300
    cityBackground = ImageAssets.loadImage(7)
    ruinsBackground = ImageAssets.loadImage(8)

    boxesCity.clear()
    # same
    boxesCity.append(box.Box(100, 190, 10, 10, "Spike"))
    boxesCity.append(box.Box(0, 0, 180, 140))
    boxesCity.append(box.Box(180, 0, 70, 120))
    boxesCity.append(box.Box(0, 200, 150, 150))
    boxesCity.append(box.Box(240, 200, 40, 105))
    boxesCity.append(box.Box(280, 150, 200, 200))
    boxesCity.append(box.Box(280, 70, 200, 40))
    boxesCity.append(box.Box(360, 110, 200, 40))
    # dif
    boxesCity.append(box.Box(195, 130, 50, 15))
    boxesCity.append(box.Box(285, 110, 5, 40, "Unslideable"))
    boxesCity.append(box.Box(280, 35, 5, 35, "Unslideable"))

    boxesRuins.clear()
    # same
    boxesRuins.append(box.Box(0, 0, 180, 140))
    boxesRuins.append(box.Box(180, 0, 70, 120))
    boxesRuins.append(box.Box(0, 200, 150, 150))
    boxesRuins.append(box.Box(240, 200, 40, 105))
    boxesRuins.append(box.Box(280, 150, 200, 200))
    boxesRuins.append(box.Box(280, 70, 200, 40))
    boxesRuins.append(box.Box(360, 110, 200, 40))
    # dif
    boxesRuins.append(box.Box(135, 190, 60, 10))
    boxesRuins.append(box.Box(230, 130, 15, 50))
    boxesRuins.append(box.Box(250, 80, 30, 20))
    boxesRuins.append(box.Box(330, 140, 10, 10))
    boxesRuins.append(box.Box(340, 125, 15, 25))


