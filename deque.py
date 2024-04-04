from collections import deque

data = deque()
data.append("John")
element = data.popleft()
print(element ,data)