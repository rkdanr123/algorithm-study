```python
import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

matrix = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

result = 0

for i in range(len(B)):
    for j in range(len(A)):
        if A[j] == B[i]:
            matrix[i+1][j+1] = matrix[i][j] + 1
            result = max(result,matrix[i+1][j+1])
            
        if (len(B)-(i+1)) == result:
            break

print(result)
```

- 처음 풀이는 이렇게 풀었는데 시간 초과
- 첨에는 비둘기집 원리때처럼 이미 답을 찾으면 더 시간 낭비를 안하게끔 최적화를 해보는 시도 등을 해봤는데 여전히 시간 초과
- 처음에 matrix를 만드는 과정이 시간 초과의 원인이라고 판단하고
- 다른 방식으로 Longest Common String을 찾아가야 한다고 판단
- 어차피 전줄과 이번줄과의 비교만을 계속 지속하는 방식이고 문자가 일치하지 않으면 0으로 초기화되기 때문에 matrix의 모든 행과 열을 가지고 갈 필요가 없음.
- 아래와 같은 풀이를 생각함.

```python
import sys

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

if len(A) < len(B):
    A, B = B, A

prev = [0] * (len(A) + 1)
current = [0] * (len(A) + 1)
result = 0

for i in range(len(B)):
    for j in range(len(A)):
        if A[j] == B[i]:
            current[j+1] = prev[j] + 1
            result = max(result, current[j+1])
        else:
            current[j+1] = 0
    prev, current = current, prev

print(result)
```
