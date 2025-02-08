```python
from collections import Counter
import sys
n = int(input())
if (n == 0):
    print(0)
else:
    counts = Counter(list(map(int, sys.stdin.read().split())))
    level = sorted(counts.elements())
    down = int(n*0.15) if n*0.15 % 1 < 0.5 else int(n*0.15) + 1
    result = sum(level[down:n-down]) / (n - 2 * down)
    print(int(result) if result % 1 < 0.5 else int(result) + 1)
```
