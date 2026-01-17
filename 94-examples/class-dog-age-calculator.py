class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7

fido=Dog()
fido.years=3
print(fido.dog_years())
