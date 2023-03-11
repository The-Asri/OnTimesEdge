import pygame
import eventHandler
import KeyManager

screen = None
clock = None
keyManager = None

def init():
    global screen
    global clock
    global keyManager
    pygame.init()
    screen = pygame.display.set_mode((600, 500))
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()
    keyManager = KeyManager.KeyManager()


def main():
    eventHandler.eventHandler(keyManager)
    if keyManager.key_jump:
        print("Jumping!")
    #
    #
    pygame.display.update()
    clock.tick(30)


init()

while True:
    main()
