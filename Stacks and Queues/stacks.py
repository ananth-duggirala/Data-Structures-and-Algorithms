# Stack can be implemented as a list in python. Push: append(), Pop: pop(). 
# However, this can run into speed issues as the stack grows, due to memory allocations.
# Alternatively, use deque(): quicker append and pop operations

from collections import deque

stack = deque()
stack.append(1)
print(stack.pop())
