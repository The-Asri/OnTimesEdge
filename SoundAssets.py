from pygame import mixer


class SoundHandler:
    def __init__(self):
        mixer.init()
        self.volume = 1
        self.sfx_volume = 1
        self.background_sfx = "./sounds/background.mp3"
        self.sfx = {
                    "jump": mixer.Sound("./sounds/jump.mp3"),
                    "death": mixer.Sound("./sounds/death.mp3"),
                    "walljump": mixer.Sound("./sounds/jump.mp3"),
                    "reset": mixer.Sound("./sounds/jump.mp3"),
                    "walk": mixer.Sound("./sounds/walk.mp3")
                    }
        mixer.Sound.set_volume(self.sfx["jump"], 0.1 * self.sfx_volume)
        mixer.Sound.set_volume(self.sfx["walljump"], 0.1 * self.sfx_volume)
        mixer.Sound.set_volume(self.sfx["death"], 0.1 * self.sfx_volume)
        mixer.music.load(self.background_sfx)

    def playBackground(self):
        mixer.music.set_volume(0.02 * self.volume)
        mixer.music.play(-1, 0, 200)

    def stopBackground(self):
        mixer.music.fadeout(100)

    def playSound(self, sound):
        self.sfx[sound].play()
