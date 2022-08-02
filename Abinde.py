# Abinde python game-engine
# Copyright 2022 MIT License desvasicek

from PIL import Image as PILImage
import pygame
from pygame.locals import *
from OpenGL.GL import *
import time, random
import threading
import warnings

pygame.init()

windows = []
players = []

warnings.simplefilter("once")

enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()

game_quit = False

def pil_image_to_surface(pilImage):
    """
    Not for development use.
    """
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
def LoadImage(path):
    return pil_image_to_surface(PILImage.open(path))
        
        
class error:
    
    class TitleError(Exception):
        def __init__(self):
            super().__init__("Title must be single-line string.")

    class BackgroundError(Exception):
        def __init__(self):
            super().__init__("Background must be rgb tuple.")

    class SizeError(Exception):
        def __init__(self):
            super().__init__("Width and height must be integers.")
    class MultipleInstanceError(Exception):
        def __init__(self):
            super().__init__("Please only have 1 window open at once.")
    class ImageError(Exception):
        def __init__(self):
            super().__init__("Please use Image class for sprite images.")
    class MultiplePlayerError(Exception):
        def __init__(self):
            super().__init__("Please only have 1 player object in use.")

class warn:
    
    class ImageWarning(DeprecationWarning):
        def __init__(self):
            warnings.warn("Using anything other than the Image class is highly advised against.", DeprecationWarning)
    

class Game(object):
    def __init__(self, title="New Pytine Instance", width=500, height=600, bg=(0, 0, 0)):
        """
        Create the window object.
        """
        global windows

        try:
            if len(windows) <= 1:
                self.root = pygame.display.set_mode((width, height))
            else:
                raise error.MultipleInstanceError
        except:
            raise error.SizeError
        
        try:
            pygame.display.set_caption(title)
        except:
            raise error.TitleError
        
        self.fps = pygame.time.Clock()
        self.looping = True
        self.bg = bg
        
        windows.append(self)
        
    def loop(self):
        """
        Not for development use.
        """
        global game_quit
        
        while self.looping:
            if not game_quit:
                
                try:
                    self.root.fill(self.bg)
                except:
                    raise error.BackgroundError
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        game_quit = True

                for player in players:
                    player.move()
                    player.draw(self)
                
                try:
                    pygame.display.flip()
                    self.fps.tick(60)
                except:
                    pass
            
    def mainloop(self):
        """
        Start the window
        """
        
        self.looping = True
        
        self.thread_loop = threading.Thread(target=self.loop, daemon=True)
        self.thread_loop.start()

# DO NOT USE

class sprite:
    class Player(pygame.sprite.Sprite):
        def __init__(self, image, pos=[20, 20], title="Sprite", FRIC=0.9, ACC=1):
            
            super().__init__()
            
            global players
            players.append(self)

            if not len(players) <= 1:
                raise error.MultiplePlayerError

            try:
                self.image = image
            except:
                warn.ImageWarning()

            self.rect = self.image.get_rect()
            self.title = title
            self.VEL = [0, 0]
            self.ACC = ACC
            self.FRIC = FRIC
            self.pos = pos
            
        def move(self):

            try:
                self.k_pressed = pygame.key.get_pressed()
            except:
                pass
            
            if self.k_pressed[K_LEFT]:
                self.VEL[0] -= self.ACC
            if self.k_pressed[K_RIGHT]:
                self.VEL[0] += self.ACC

            self.VEL[0] *= self.FRIC
            self.pos[0] += self.VEL
            self.rect.midbottom = self.pos

        def draw(self, game):

            try:
                game.root.blit(self.image, self.rect)
            except:
                pass
            
    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            global enemies
            enemies.add(self)
    class Animal(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
    class Object(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            global objects
            objects.add(self)

# END DO NOT USE
