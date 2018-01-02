import unittest
from tdd.src import age_group_finder

class test_age_group_finder(unittest.TestCase):

	def test_age_group_baby(self):
		self.assertEqual('Baby', age_group_finder.find(0))
		self.assertEqual('Baby', age_group_finder.find(1))
		self.assertEqual('Baby', age_group_finder.find(2))
