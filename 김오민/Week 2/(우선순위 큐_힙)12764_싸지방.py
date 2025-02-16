import sys
import heapq

n = int(input())
computer_use_count = [0] * n  # 각 컴퓨터의 사용 횟수 트랙킹 [1,2,1,4,2,1....0]
computer_time_left = []  # (종료시간, 컴퓨터 번호) 형태의 튜플 저장
computer_available = list(range(n))  # 사용 가능한 컴퓨터 [1,2,3,4...,n]
heapq.heapify(computer_available)

time = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
time_sort = sorted(time, key=lambda x: x[0])  # 시작 시간 순 정렬

for trooper in time_sort:
    # 새로운 병사가 싸지방에 들어온 시간을 기준으로 컴퓨터 상태 최신화
    while len(computer_time_left) > 0 and computer_time_left[0][0] <= trooper[0]:
        temp = heapq.heappop(computer_time_left)
        heapq.heappush(computer_available, temp[1])

    computer = heapq.heappop(computer_available)  # 안쓰는 컴퓨터 중 번호 젤 작은거
    heapq.heappush(computer_time_left, (trooper[1], computer))  #컴퓨터 활성화 및 종료시간 기록 
    computer_use_count[computer] += 1 # 사용 횟수 트랙킹

used = n - computer_use_count.count(0)
print(used)
print(' '.join(map(str,computer_use_count[:used])))


# 리스트 index()의 사용은 너무나도 큰 시간복잡도 아마 n^2 heap을 이용해 유동적 관리 짱짱
