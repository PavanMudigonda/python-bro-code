def skip_elements(elements):
	new_elements = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			new_elements.append(element)
	return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
