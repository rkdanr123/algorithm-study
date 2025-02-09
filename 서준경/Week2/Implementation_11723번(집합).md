https://github.com/JunKyungSeo/BOJ/tree/master/%EB%B0%B1%EC%A4%80/Silver/11723.%E2%80%85%EC%A7%91%ED%95%A9
```python
import sys
N = int(sys.stdin.readline())
S = set()

for rpt in range(N):
    order = sys.stdin.readline().strip()
    if order == "all":
        S = set([i for i in range(1, 21)])
    elif order == "empty":
        S = set()
    else:
        first, second = order.strip().split(" ")
        second = int(second)
        if first == "add":
            S.add(second)
        elif first == "remove":
            if second in S:
                S.remove(second)
        elif first == "check":
            print("1" if second in S else "0")
        elif first == "toggle":
            if second in S:
                S.remove(second)
            else:
                S.add(second)
```
