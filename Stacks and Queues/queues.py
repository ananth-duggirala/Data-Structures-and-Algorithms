# Lists are bad for implementing queues because insertion/deletion takes O(n) time

from collections import deque

queue = dequeue()
queue.append(1)
print(queue.popleft())