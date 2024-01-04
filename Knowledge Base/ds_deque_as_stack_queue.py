# Need to check if deque is null or len(deque) == 0 otherwise will throw an index out of range error

#### Queues ####

from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)

q.popleft()
# q.popleft()

print(q, len(q), q[0])


#### Stacks ####

s = deque()
s.append(1)
s.append(2)
s.append(3)

print("popped: ", s.pop())
print(s[-1])