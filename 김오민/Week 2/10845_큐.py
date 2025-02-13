from collections import deque #처음에는 멋도 모르고 list로 하다가 시간 초과, collections 잘 씁시다
import sys #deque 써도 런타임 에러 떠서 명령을 한번에 받아버리기로함

que = deque()
n = int(input())
command_input = sys.stdin.read().splitlines()

for i in range(n):
    command = command_input[i]
    if command[:4] == "push":
        que.append(command.split()[1])
    elif command == "pop":
        print(que.popleft() if que else -1)
    elif command == "size":
        print(len(que))
    elif command == "empty":
        print(1 if not que else 0)
    elif command == "front":
        print(que[0] if que else -1)
    elif command == "back":
        print(que[-1] if que else -1)
