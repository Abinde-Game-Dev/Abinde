import Abinde as ab
game = ab.Game(width=1000, height=1000)
player = ab.sprite.Player(ab.LoadImage("sample1.png"))
_object = ab.sprite.Object(ab.LoadImage("sample1.png"), pos=[500, 1100])
audio = ab.Audio("sample1.mp3")
audio.play()
game.mainloop()
