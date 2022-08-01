# pytine python game-engine
# Copyright 2022 MIT License desvasicek

import pygame
from pygame.locals import *
from OpenGL.GL import *
import time, random
import threading
import PIL
import warnings

pygame.init()

windows = []

warnings.simplefilter("once")

enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()
class Image(object):
    def __init__(self, path):
        self.path = path
        self.isimageobj = True
        self.image = Image.open(path)
        self.mode = image.mode
        self.size = image.size
        self.data = image.tostring()
        return pygame.image.fromstring(self.data, self.size, self.mode)
        
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
            super().__init__("Please only have 1 instance open at once.")
    class ImageError(Exception):
        def __init__(self):
            super().__init__("Please use Image class for sprite images.")

class warn:
    
    class ImageWarning(DeprecationWarning):
        def __init__(self):
            warnings.warn("Using anything other than the Image class is highly advised against.", DeprecationWarning)
    

class Game(object):
    def __init__(self, title="New Pytine Instance", width=500, height=600, bg=(0, 0, 0)):
        """
        Create the window object.
        """

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
        self.looping = False
        self.bg = bg
        
        windows.append(self)
        
    def loop(self):
        """
        Not for development use.
        """
        while self.looping:
            
            try:
                self.root.fill(self.bg)
            except:
                raise error.BackgroundError
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.looping = True
            
            self.fps.tick(60)
            
            try:
                pygame.display.flip()
            except:
                pass
            
    def mainloop(self):
        """
        Start the window
        """
        
        self.looping = True
        
        thread_loop = threading.Thread(target=self.loop, daemon=True)
        thread_loop.start()

# DO NOT USE

class sprite:
    class Player(pygame.sprite.Sprite):
        def __init__(self, image, health=10, accel=1, fric=.9):
            super().__init__()
            try:
                if image.isimageobj:
                    self.image = image
                    self.rect = self.image.get_rect()
                else:
                    warn.ImageWarning()
            except:
                raise error.ImageError
        def move(self, x=0, y=0):
            pass
            
    class Enemy(pygame.sprite.Sprite):
        pass
    class Animal(pygame.sprite.Sprite):
        pass
    class Object(pygame.sprite.Sprite):
        pass

# END DO NOT USE
