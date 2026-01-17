class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color='brown'
table.material='wood'

couch = Furniture()
couch.color='red'
couch.color='leather'

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color,piece.material))

print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"
