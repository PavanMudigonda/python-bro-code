class Apple():
    def __init__(self, color, flavor):
        self.color=color
        self.flavor=flavor
    def __str__(self):
        return "This apple is {} and {}".format(self.color,self.flavor)

jonagold=Apple("red","sweet")

print(jonagold.color)

print(jonagold)


macintosh=Apple("green","sweet")

print(macintosh.flavor)

print(macintosh)
