import pygame
import math
import random
import camera
import border
import eventHandler
import ImageAssets

def intro(screen, surface, cityBackground, ruinsBackground, w, h, upscale, clock, keyManager):
    logo = None
    background = None
    color = None

    tick = 0
    introcam = camera.Camera(w, h, border.Border(500, 500))
    introcam.y = 70

    if random.randint(0, 1) == 0:
        background = cityBackground
        logo = ImageAssets.loadImage(12)
        color = "Yellow"
    else:
        background = ruinsBackground
        logo = ImageAssets.loadImage(13)
        color = "darkmagenta"

    while True:
        eventHandler.eventHandler(keyManager)

        tick = (tick + 1)%360
        x = math.sin(tick/180 * math.pi) * 30 + 50
        introcam.x = x

        surface.blit(background, (-introcam.x, -introcam.y))
        font = pygame.font.SysFont(None, 20)
        img = font.render("Press [Enter] to start", False, color)
        surface.blit(img, (w / 2 - 64, h / 2 + 10))
        upscaled = pygame.transform.scale_by(surface, upscale)
        upscaled.blit(logo, (140, 80))
        screen.blit(upscaled, (0, 0))

        if keyManager.key_start:
            break

        pygame.display.update()

        clock.tick(20)