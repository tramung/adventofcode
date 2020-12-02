import unittest
from passwordpolicy import PasswordPolicy

class PasswordPolicyTestCase(unittest.TestCase):
  def test_policy_checkers_passed(self):
    cri, char, input = '1-3 a: abcde'.split()
    test = PasswordPolicy(char, cri, input)
    self.assertTrue(test.policyChecker())

  def test_policy_checkers_failed(self):
    cri, char, input = '1-3 b: cdefg'.split()
    test = PasswordPolicy(char, cri, input)
    self.assertFalse(test.policyChecker())

if __name__ == '__main__': 
  unittest.main() 