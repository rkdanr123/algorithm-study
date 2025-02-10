https://github.com/JunKyungSeo/BOJ/tree/master/%EB%B0%B1%EC%A4%80/Gold/1074.%E2%80%85Z
```python
def func(N, r, c):
    if N == 1:
        if r and c:
            return 4
        elif r and not c:
            return 3
        elif not r and c:
            return 2
        else:
            return 1
    elif N == 0:
        return 1
        
    x = 2**(N-1)
    y = 2**(N-1)
    a = 0
    b = 0
    if (c >= x):
        a = 0
    else:
        a = 1
    if (r >= y):
        b = 0
    else:
        b = 1
    if a and b:
        return func(N-1, r, c)
    elif a and not b:
        return 2 * 4**(N-1) + func(N-1, r - y, c)
    elif not a and b:
        return 4**(N-1) + func(N-1, r, c - x)
    else:
        return 3 * 4**(N-1) + func(N-1, r - y, c - x)

N, r, c = map(int, input().split())
print(func(N, r, c) - 1)
```
