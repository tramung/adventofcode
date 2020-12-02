import unittest
from multiplier import Multiplier

class MultiplierTestCase(unittest.TestCase):
  def test_summation_check_passed(self):
    test = Multiplier([1721, 979, 366, 299, 675, 1456])
    self.assertTrue(test.summationCheck())
    self.assertEqual(test.result, 1721*299)

  def test_summation_check_failed(self):
    test = Multiplier([1721, 366, 0, 675])
    self.assertFalse(test.summationCheck())
    self.assertEqual(test.result, -1)

if __name__ == '__main__': 
  unittest.main() 