from pygame import mixer
background = False
jumpSound = None

def init():
    global jumpSound

    mixer.music.set_volume(0.1)

    jumpSound = mixer.Sound("./sounds/laser.wav")
    mixer.Sound.set_volume(jumpSound, 0.1)
def loadMusic(id):
    global background

    if id == 1:
        if not background:
            mixer.music.load("./sounds/background.wav")
            background = True
            mixer.music.play(-1, fade_ms=1000)
    if id == 2:
        if not background:
            background = mixer.music.load("./sounds/Wowkie_Zhang_HD_MV.mp3")
            background = True
            mixer.music.play(-1, fade_ms=1000)

def clearMusic():
    global background
    mixer.music.unload()
    background = False

def playSound(id):
    if id == 1:
        jumpSound.play()