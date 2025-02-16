```python
import sys
from collections import deque
# sys.stdin.readline().strip()

N, M = map(int, sys.stdin.readline().strip().split())
nums = deque()
for i in range(N):
    nums.append(deque(map(int, sys.stdin.readline().strip().split())))
# print(nums)
for i in range(N):
    if i == 0:
        for j in range(1, N):
            nums[i][j] += nums[i][j-1]
        continue
    nums[i][0] += nums[i-1][0]
    for j in range(1, N):
        nums[i][j] += nums[i][j-1] + nums[i-1][j] - nums[i-1][j-1]
# print(nums)
for rpt in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    result = nums[x2-1][y2-1] - (nums[x1-2][y2-1] if x1>1 and y2>0 else 0) - (nums[x2-1][y1-2] if x2>0 and y1>1 else 0) + (nums[x1-2][y1-2] if x1>1 and y1>1 else 0)
    print(result)
```
