```python
import sys
# sys.stdin.readline().strip()

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(lambda x : int(x) % M, sys.stdin.readline().strip().split()))
skajwl = [0]*M
skajwl[nums[0]] += 1
for i in range(1, N):
    nums[i] = (nums[i] + nums[i-1]) % M
    skajwl[nums[i]] += 1

cnt = skajwl[0]

for i in range(M):
     if skajwl[i] > 1:
        cnt += int(skajwl[i] * (skajwl[i]-1) * 0.5)
print(cnt)
```
