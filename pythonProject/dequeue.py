from collections import deque

queue = deque()

deque([])

queue.append("Monkey1")
queue.append("Monkey2")
queue.append("Monkey3")

deque(["Monkey1", "Monkey2", "Monkey3"])
queue.popleft()
