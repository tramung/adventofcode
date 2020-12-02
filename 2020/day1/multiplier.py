class Multiplier():
  YEAR_FROM_HELL = 2020
  def __init__(self, num_list):
    self.num1 = -1
    self.num2 = -1
    self.result = -1
    self.num_list = num_list
    if self.summationCheck() == True:
      self.multiply()
  
  def summationCheck(self):
    for num in self.num_list:
      checker = self.YEAR_FROM_HELL - num
      if checker in self.num_list:
        self.num1 = num
        self.num2 = checker
        return True
    return False

  def multiply(self):
    self.result = self.num1 * self.num2
    return self.result