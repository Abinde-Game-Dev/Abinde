import Abinde as ab
game = ab.Game()
player = ab.sprite.Rectangle()
def move(keys):
    if keys[ab.key.UP]:
        if not player.get_pos()[1] <= 0:
            player.move([0, -8])
    if keys[ab.key.DOWN]:
        if not player.get_pos()[1] >= game.get_size()[1] - player.get_size()[1]:
            player.move([0, 8])
    if keys[ab.key.LEFT]:
        if not player.get_pos()[0] <= 0:
            player.move([-8, 0])
    if keys[ab.key.RIGHT]:
        if not player.get_pos()[0] >= game.get_size()[0] - player.get_size()[0]:
            player.move([8, 0])

ab.OnKeyPress(game, move)
game.mainloop()
