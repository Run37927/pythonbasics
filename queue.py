from collections import deque

# so you can add and remove from both ends of the list

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
print(type(queue))

x = queue.popleft()
# takes item off from the front of the queue
print(x)
print(queue)