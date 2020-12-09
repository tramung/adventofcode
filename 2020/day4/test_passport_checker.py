import unittest
from passport_checker import PassportChecker

class PassportCheckerTestCase(unittest.TestCase):
  # def test_policy_checkers_passed(self):

  # def test_policy_checkers_failed(self):

  def test_adventofcode_input(self):
    with open('day4/input.txt', 'r') as fh:
      counter = 0
      input = ''
      for line in fh:
        input += line
        if line == '\n':
          test = PassportChecker()
          counter += 1 if test.check_fields(input) else 0
          input = ''
      self.assertEqual(counter, 519)

  # def test_adventofcode_input_part2(self):
  #   with open('day2/input.txt', 'r') as fh:
  #     counter = 0
  #     for line in fh:
  #       cri, char, input = line.split()
  #       test = PasswordPolicy(char, cri, input)
  #       counter += 1 if test.policyCheckerpart2() else 0
  #     self.assertEqual(counter, 708)

if __name__ == '__main__': 
  unittest.main() 