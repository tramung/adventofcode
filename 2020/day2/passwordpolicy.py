class PasswordPolicy:
  def __init__(self, char, criterion, input):
    self.char = char.strip(':')
    dash_index = criterion.index('-')
    self.lower_lim = int(criterion[0:dash_index])
    self.upper_lim = int(criterion[dash_index+1:])
    self.input = input
  
  def policyChecker(self):
    return self.lower_lim <= self.input.count(self.char) <= self.upper_lim
  