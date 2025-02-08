```python
N = int(input())
number = [i for i in range(1, N+1)]

result = list()
pre_idx = 0
ispos = True

for i in range(N):
    num = int(input())
    idx = number.index(num)
    if (idx >= pre_idx):
        result += ["+"] * (idx - (pre_idx - 1)) + ["-"]
    else:
        if idx == pre_idx - 1:
            result.append("-")
        else:
            ispos = False
    del number[idx]
    pre_idx = idx
print("\n".join(result) if ispos else "NO") 
```
