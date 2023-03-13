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
    if id == 4:
        loadLevel4(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player)

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
    levelBorder.x = 430
    levelBorder.y = 200
    cityBackground = ImageAssets.loadImage(1)
    ruinsBackground = ImageAssets.loadImage(2)

    boxesCity.clear()
    #same
    boxesCity.append(box.Box(20, 100, 110, 150))
    boxesCity.append(box.Box(260, 140, 70, 150))
    boxesCity.append(box.Box(350, 110, 100, 150))
    #dif
    boxesCity.append(box.Box(125, 55, 5, 45, "Unslideable"))

    boxesCity.append(box.Box(170, 110, 8, 150, "Unslideable"))
    boxesCity.append(box.Box(150, 115, 20, 12, "Unslideable"))
    boxesCity.append(box.Box(178, 115, 20, 12, "Unslideable"))

    boxesCity.append(box.Box(290, 95, 5, 45))
    boxesCity.append(box.Box(290, 90, 5, 5, "Spike"))
    boxesCity.append(box.Box(355, 65, 5, 45, "Spike"))

    boxesRuins.clear()
    #same
    boxesRuins.append(box.Box(20, 100, 110, 150))
    boxesRuins.append(box.Box(260, 140, 70, 150))
    boxesRuins.append(box.Box(350, 110, 100, 150))
    #dif
    boxesRuins.append(box.Box(95, 95, 35, 5, "Unslideable"))


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
    boxesCity.append(box.Box(380, 55, 20, 15))
    # dif
    boxesCity.append(box.Box(195, 130, 50, 15))
    boxesCity.append(box.Box(285, 110, 5, 40, "Unslideable"))
    boxesCity.append(box.Box(280, 30, 5, 40, "Unslideable"))
    boxesCity.append(box.Box(280, 25, 5, 5, "Spike"))

    boxesRuins.clear()
    # same
    boxesRuins.append(box.Box(0, 0, 180, 140))
    boxesRuins.append(box.Box(180, 0, 70, 120))
    boxesRuins.append(box.Box(0, 200, 150, 150))
    boxesRuins.append(box.Box(240, 200, 40, 105))
    boxesRuins.append(box.Box(280, 150, 200, 200))
    boxesRuins.append(box.Box(280, 70, 200, 40))
    boxesRuins.append(box.Box(360, 110, 200, 40))
    boxesRuins.append(box.Box(380, 55, 20, 15))
    # dif
    boxesRuins.append(box.Box(135, 190, 60, 10))
    boxesRuins.append(box.Box(230, 130, 15, 50))
    boxesRuins.append(box.Box(250, 60, 30, 20))
    boxesRuins.append(box.Box(330, 140, 10, 10))
    boxesRuins.append(box.Box(340, 125, 15, 25))

def loadLevel4(boxesCity, boxesRuins, levelBorder, cityBackground, ruinsBackground, player):
    player.x = 50
    player.y = 200 - 12 - 1 + 200
    player.vx = 0
    player.vy = 0
    levelBorder.x = 700
    levelBorder.y = 450
    cityBackground = ImageAssets.loadImage(7)
    ruinsBackground = ImageAssets.loadImage(8)

    boxesCity.clear()
    # same
    # floor1
    boxesCity.append(box.Box(0, 200 + 200, 250, 150))
    boxesCity.append(box.Box(635, 400, 90, 90))
    # roof1
    boxesCity.append(box.Box(200, 125 + 200, 50, 40))
    boxesCity.append(box.Box(0, 50 + 200, 200, 100))
    boxesCity.append(box.Box(250, -55 + 200, 125, 20))
    boxesCity.append(box.Box(375, -75 + 200, 125, 20))
    boxesCity.append(box.Box(500, -55 + 200, 135, 20))
    # spikes
    boxesCity.append(box.Box(590, 30 + 200, 20, 10, "Spike"))
    boxesCity.append(box.Box(615, 90 + 200, 20, 10, "Spike"))
    boxesCity.append(box.Box(590, 150 + 200, 20, 10, "Spike"))
    # elevator
    boxesCity.append(box.Box(290, 0 + 200, 300, 300))
    boxesCity.append(box.Box(200, -100 + 200, 50, 190))
    # elevator2
    boxesCity.append(box.Box(635, 165, 100, 200))
    # diff
    #blockade1
    boxesCity.append(box.Box(240, 90 + 200, 10, 35, "Unslideable"))
    # elevator2
    boxesCity.append(box.Box(590, 200, 45, 10))
    boxesCity.append(box.Box(625, 200 - 35, 10, 35))
    #door1
    boxesCity.append(box.Box(240, 165 + 200, 10, 35, "Unslideable"))
    boxesCity.append(box.Box(250, 0 + 200, 40, 50))

    boxesRuins.clear()
    # same
    # floor1
    boxesRuins.append(box.Box(0, 200 + 200, 250, 150))
    boxesRuins.append(box.Box(635, 400, 90, 90))
    # roof1
    boxesRuins.append(box.Box(200, 125 + 200, 50, 40))
    boxesRuins.append(box.Box(0, 50 + 200, 200, 100))
    boxesRuins.append(box.Box(250, -55 + 200, 125, 20))
    boxesRuins.append(box.Box(375, -75 + 200, 125, 20))
    boxesRuins.append(box.Box(500, -55 + 200, 135, 20))
    #spikes
    boxesRuins.append(box.Box(590, 30 + 200, 20, 10, "Spike"))
    boxesRuins.append(box.Box(615, 90 + 200, 20, 10, "Spike"))
    boxesRuins.append(box.Box(590, 150 + 200, 20, 10, "Spike"))
    # elevator
    boxesRuins.append(box.Box(290, 0 + 200, 300, 300))
    boxesRuins.append(box.Box(200, -100 + 200, 50, 190))
    # elevator2
    boxesRuins.append(box.Box(635, 165, 100, 200))
    # diff
    # spike1
    boxesRuins.append(box.Box(250, 75 + 200, 10, 15, "Spike"))
    boxesRuins.append(box.Box(635, 365, 10, 35, "Unslideable"))
    # door1
    boxesRuins.append(box.Box(290, -35 + 200, 10, 35, "Unslideable"))

