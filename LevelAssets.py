import box
import border
import Player

def loadLevel(id, boxes, levelBorder, player):
    if id == 1:
        loadLevel1(boxes, levelBorder, player)

def loadLevel1(boxes, levelBorder, player):
    player.x = 100
    player.y = 100 - 12 - 1
    player.vx = 0
    player.vy = 0
    levelBorder.x = 500
    levelBorder.y = 150

    boxes.clear()
    boxes.append(box.Box(50, 100, 150, 25))
    boxes.append(box.Box(250, 100, 100, 25))
    boxes.append(box.Box(370, 70, 100, 50))
    boxes.append(box.Box(300, 50, 20, 30))
