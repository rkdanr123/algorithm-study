https://github.com/JunKyungSeo/BOJ/tree/master/%EB%B0%B1%EC%A4%80/Silver/1260.%E2%80%85DFS%EC%99%80%E2%80%85BFS
```python
from collections import deque

def dfs(graph, start):
    visited = deque()
    stack = deque()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend([i for i in graph[node] if i not in visited])
    return visited


def bfs(graph, start):
    visited = deque()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([i for i in graph[node] if i not in visited])
    return visited

N, M, V = map(int, input().split())
graph = [[] for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
for i in range(N):
    graph[i].sort(reverse=True)

print(" ".join([str(i+1) for i in dfs(graph, V-1)]))
for i in range(N):
    graph[i].sort()
print(" ".join([str(i+1) for i in bfs(graph, V-1)]))
```
