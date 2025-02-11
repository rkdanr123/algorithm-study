```python
import sys
from collections import deque

T = int(input())
for testcase in range(T):
    func = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    if N == 0:
        A = sys.stdin.readline().strip()
        print('error' if 'D' in func else '[]')
        continue
    num = deque(map(int, sys.stdin.readline().strip()[1:-1].split(',')))
    # print(f'num : {num}')
    cnt = 0
    iserror = False
    for i in range(len(func)):
        if func[i] == 'R':
            cnt = not cnt
        else:
            if len(num) > 0:
                if (cnt):
                    num.pop()
                else:
                    num.popleft()
            else:
                iserror = True
                print('error', end='')
                break
    if (cnt):
        num.reverse()
    if (not iserror) and (len(num) == 0):
        print('[]', end = '')
    print(f'[{",".join(map(str, num))}]' if len(num) != 0 else '')
```
