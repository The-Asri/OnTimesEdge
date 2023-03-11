import box
import border
import Player

def loadLevel(id, boxes, levelBorder, player):
    if id == 1:
        loadLevel1(boxes, levelBorder, player)

def loadLevel1(boxes, levelBorder, player):
    player.x = 50
    player.y = 80
    levelBorder.x = 500
    levelBorder.y = 150

    boxes.clear()
    boxes.append(box.Box(50, 100, 200, 25))
    boxes.append(box.Box(300, 100, 200, 25))
