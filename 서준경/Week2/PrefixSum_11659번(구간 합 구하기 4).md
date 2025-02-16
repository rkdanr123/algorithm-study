```python
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
nums = deque(map(int, sys.stdin.readline().strip().split()))
S = deque()
S.append(nums[0])
for i in range(1, N):
    S.append(S[i-1] + nums[i])
for rpt in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(S[j-1]-S[i-2] if i >= 2 else S[j-1])
```
