import Abinde as ab
game = ab.Game("Audio Test")
text = ab.sprite.Text("Sans-Serif", "Just Listen.", 70, color=ab.color.RED)
audio = ab.Audio("sample1.mp3")
audio.play()
game.mainloop()
