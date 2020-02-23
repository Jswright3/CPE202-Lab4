"""CPE202
John Wright
Lab 4
"""
import unittest
from ordered_list import OrderedList


class MyTest(unittest.TestCase):

   def test_add(self):
      ordered_list = OrderedList()
      ordered_list.add(2)
      ordered_list.add(1)
      ordered_list.add(3)
      print(ordered_list.head.val)
      self.assertEqual(ordered_list.index(1), 0)
      self.assertEqual(ordered_list.index(2), 1)
      self.assertEqual(ordered_list.index(3), 2)

if __name__ == '__main__':
   unittest.main()
