
N = int(input())
tower = list(map(int, input().split()))

stack = []
answer = [0] * N

for i in range(N):
    while stack and tower[stack[-1]] < tower[i]:
        stack.pop()
    
    if stack:
        answer[i] = stack[-1] + 1
    
    stack.append(i)

print(*answer)
