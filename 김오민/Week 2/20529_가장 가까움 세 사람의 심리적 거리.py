from itertools import combinations  #combination을 반복문 돌리면 백준이가 싫어해서 넣음

t = int(input())


def distance(a, b, c):
    count = 0
    for j in range(4):
        if a[j] != b[j]:
            count += 1
        if b[j] != c[j]:
            count += 1
        if a[j] != c[j]:
            count += 1
    return count


for _ in range(t):
    n = int(input())
    mbti_list = list(map(str, input().split()))
    if n <= 32: #사실상 이 문제의 핵심. 32를 넘어서는 순간부터는 비둘기집 원리에 따라 구할 필요가 없어진다.
        min_distance = 12
        for triplet in combinations(mbti_list, 3):
            min_distance = min(min_distance, distance(*triplet))
        print(min_distance)
    else:
        print(0)


#비둘기비둘기
