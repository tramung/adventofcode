class PassportChecker:
  def __init__(self):
    self.passport_field = {      "byr",
      "iyr",
      "eyr",
      "hgt",
      "hcl",
      "ecl",
      "pid",
    #   "byr": None,
    #   "iyr": None,
    #   "eyr": None,
    #   "hgt": None,
    #   "hcl": None,
    #   "ecl": None,
    #   "pid": None,
    #   "cid": None
    }

  def check_fields(self, input):
    for field in self.passport_field:
      if field not in input:
        return False
    return True
    # for field in input.split():
    #   colon_ind = field.index(':')
    #   key = field[:colon_ind]
    #   value = field[colon_ind:]
    #   self.passport_field.