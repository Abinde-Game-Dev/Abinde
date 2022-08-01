import unittest
import Pytine as pt

class TestGame(unittest.TestCase):
	
	def test_game_init(self):
		self.assertEqual(Game(), "")
