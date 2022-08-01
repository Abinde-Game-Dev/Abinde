import unittest
import Firestorm as fs

class TestGame(unittest.TestCase):
	
	def test_game_init(self):
		self.assertEqual(Game(), "")