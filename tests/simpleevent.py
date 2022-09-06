import Abinde as ab
import pygame # import pygame for event translations
game = ab.Game(log_to="file")
def checka(e):
        if e.key == ab.key.A:
                print("A Pressed!")
                print("Event " + str(pygame.event.event_name(e.type))) # A bit of pygame
        else:
                print("Sorry. Another key was pressed.")
                print("Event " + str(pygame.event.event_name(e.type))) # A bit of pygame
ab.OnKeyDown(game, checka)
ab.OnKeyUp(game, checka)
game.mainloop()
