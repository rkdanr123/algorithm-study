https://github.com/JunKyungSeo/BOJ/blob/master/%EB%B0%B1%EC%A4%80/Silver/1654.%E2%80%85%EB%9E%9C%EC%84%A0%E2%80%85%EC%9E%90%EB%A5%B4%EA%B8%B0/README.md
```python
K, N = map(int, input().split())
lanlen = [int(input()) for i in range(K)]
lanlen.sort()
start = 1
end = sum(lanlen) // N + 1
mid = int((start + end) / 2)
while (start < mid):
    mid = int((start + end) / 2)
    if (sum([i // mid for i in lanlen]) >= N):
        start = mid
    else:
        end = mid
    mid = int((start + end) / 2)
print(mid)
```
