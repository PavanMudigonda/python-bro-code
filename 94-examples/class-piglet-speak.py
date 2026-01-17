class Piglet:
    name = 'piglet'
    year = '2'
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


hamlet = Piglet()
hamlet.name="Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name="Rambo"
petunia.speak()
