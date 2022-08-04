# Abinde python game-engine
# Copyright 2022 MIT License desvasicek

from PIL import Image as PILImage
import pygame
from pygame.locals import *
import time, random
import threading
import warnings

pygame.init()

windows = []
players = []
drawings = []

warnings.simplefilter("once")

enemies = pygame.sprite.Group()
objects = pygame.sprite.Group()

game_quit = False


class color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)


def pil_image_to_surface(pilImage):
    """
    Not for development use.
    """
    return pygame.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()

def LoadImage(path, mode="PIL"):
    """
    Load an image
    """
    if mode == "PIL":
        return pil_image_to_surface(PILImage.open(path))
    elif mode == "pygame":
        return pygame.image.load(path)
    else:
        raise error.SetModeError
        
        
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
            super().__init__("You can only have 1 window open at once.")
    class ImageError(Exception):
        def __init__(self):
            super().__init__("Use Image class for sprite images.")
    class MultiplePlayerError(Exception):
        def __init__(self):
            super().__init__("You can only have 1 player object in use at once.")
    class SetModeError(Exception):
        def __init__(self):
            super().__init__("Only options 'PIL' and 'pygame' are supported.")

class warn:
    
    class ImageWarning(DeprecationWarning):
        def __init__(self):
            warnings.warn("Using anything other than the Image class is highly advised against.", DeprecationWarning)
    

class Game(object):
    """
    Create the window object.
    """
    def __init__(self, title="New Abinde Instance", width=500, height=600, bg=color.BLACK):
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
        self.root.fill(bg)
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
                        self.looping = False
                for player in players:
                    player.move()
                    player.draw(self)
                for drawing in drawings:
                    drawing.draw(self)
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
        # To fix bug on mac run loop on Main Thread.
        self.loop()
        

# DO NOT USE

class sprite:
    class Player(pygame.sprite.Sprite):
        """
        User-playable object
        """
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
            self.rect.center = self.pos
            
        def move(self):
            """
            Not for development use.
            """
            try:
                self.k_pressed = pygame.key.get_pressed()
            except:
                pass
            if self.k_pressed[K_LEFT]:
                self.VEL[0] -= self.ACC
            if self.k_pressed[K_RIGHT]:
                self.VEL[0] += self.ACC
            self.VEL[0] *= self.FRIC
            self.rect.move_ip(VEL[0], VEL[1])
            
        def draw(self, game):
            """
            Not for development use.
            """
            try:
                game.root.blit(self.image, self.rect)
            except:
                pass
            
        def kill(self):
            """
            Remove the sprite
            """
            players.remove(self)
            del self

            
    class Enemy(pygame.sprite.Sprite):
        """
        Enemy object that can hurt the player
        """
        def __init__(self):
            super().__init__()
            global enemies
            enemies.add(self)

            
    class Animal(pygame.sprite.Sprite):
        """
        Animal object that wanders around.
        """
        def __init__(self):
            super().__init__()

            
    class Object(pygame.sprite.Sprite):
        """
        Platforms.
        """
        def __init__(self):
            super().__init__()
            global objects
            objects.add(self)

# END DO NOT USE

            
    class Rectangle(object):
        """
        Draw a rectangle
        """
        def __init__(self, pos=[40, 40], size=[50, 50], color=color.WHITE, title="Rectangle"):
            self._x = pos[0]
            self._y = pos[1]
            self._width = size[0]
            self._height = size[1]
            self.color = color
            self.title = title
            drawings.append(self)
            self.rect = pygame.Rect(self._x, self._y, self._width, self._height)
            
        def draw(self, game):
            pygame.draw.rect(game.root, self.color, self.rect)

            
    class Line(object):
        """
        Draw a line
        """
        def __init__(self, pos=[40, 40], length=[50, 50], color=color.WHITE, title="Line"):
            self._x = pos[0]
            self._y = pos[1]
            self._start = length[0]
            self._end = length[1]
            self.color = color
            self.title = title
            drawings.append(self)
            
        def draw(self, game):
            pygame.draw.line(game.root, self.color, [self._x, self._y], [self._start, self._end])

            
    class Ellipse(object):
        """
        Draw an ellipse
        """
        def __init__(self, pos=[40, 40], size=[50, 50], color=color.WHITE, title="Ellipse"):
            self._x = pos[0]
            self._y = pos[1]
            self._width = size[0]
            self._height = size[1]
            self.color = color
            self.title = title
            drawings.append(self)
            
        def draw(self, game):
            pygame.draw.ellipse(game.root, self.color)
            
