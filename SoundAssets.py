from pygame import mixer


class SoundHandler:
    def __init__(self):
        mixer.init()
        self.volume = 0.05
        self.sfx_volume = 0.05
        self.background_sfx = "./sounds/ohio.mp3"
        self.sfx = {
                    #"jump": mixer.Sound("./sounds/jump.mp3"),
                    #"death": mixer.Sound("./sounds/death.mp3"),
                    "jump": mixer.Sound("./sounds/bui.mp3"),
                    "death": mixer.Sound("./sounds/funny.mp3"),
                    "wallJump": mixer.Sound("./sounds/ahh.mp3"),
                    }
        mixer.music.load(self.background_sfx)

    def playBackground(self):
        mixer.music.set_volume(self.volume)
        mixer.music.play(-1, 0, 200)

    def stopBackground(self):
        mixer.music.fadeout(100)

    def playSound(self, sound):
        mixer.Sound.set_volume(self.sfx[sound], self.sfx_volume)
        self.sfx[sound].play()
