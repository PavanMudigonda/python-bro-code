from collections import deque
items = deque([1, 2])
items.append(3)        # deque == [1, 2, 3]
items.rotate(1)        # The deque is now: [3, 1, 2]
items.rotate(-1)       # Returns deque to original state: [1, 2, 3]
item = items.popleft() # deque == [2, 3]