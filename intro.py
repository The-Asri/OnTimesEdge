import pygame
import math
import camera
import border
import eventHandler
import ImageAssets

def intro(screen, surface, background, w, h, upscale, clock, keyManager):
    logo = ImageAssets.loadImage(12)

    tick = 0
    introcam = camera.Camera(w, h, border.Border(500, 500))
    introcam.y = 70

    while True:
        eventHandler.eventHandler(keyManager)

        tick = (tick + 1)%360
        x = math.sin(tick/180 * math.pi) * 30 + 50
        introcam.x = x

        surface.blit(background, (-introcam.x, -introcam.y))
        font = pygame.font.SysFont(None, 20)
        img = font.render("Press [Enter] to start", False, "Yellow")
        surface.blit(img, (w / 2 - 64, h / 2 + 20))
        upscaled = pygame.transform.scale_by(surface, upscale)
        upscaled.blit(logo, (-12, 0))
        screen.blit(upscaled, (0, 0))

        if keyManager.key_start:
            break

        pygame.display.update()

        clock.tick(20)