# pytine python game-engine
# Copyright 2022 MIT License desvasicek

import pygame
from pygame.locals import *
from OpenGL.GL import *
import time, random
import threading
import PIL

pygame.init()

windows = []

enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()
class Image(object):
    def __init__(self, image_path):
        
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
            super().__init__()
    

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

class Sprite:
    class Player(pygame.sprite.Sprite):
        def __init__(self, health, accel, fric):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect()
        def move(self, x=0, y=0):
            pass
            
    class Enemy(pygame.sprite.Sprite):
        pass
    class Animal(pygame.sprite.Sprite):
        pass
    class Object(pygame.sprite.Sprite):
        pass
