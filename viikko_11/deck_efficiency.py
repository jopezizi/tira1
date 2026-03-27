from collections import deque
import time

p = deque()
n = 10 ** 5

start1 = time.time()
for i in range(n):
    p.append(i)

end1 = time.time()
addtime = end1-start1

start2 = time.time()
while p:
    p.popleft()

end2 = time.time()
poptime = end2-start2

print(addtime)
print(poptime)