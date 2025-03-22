'''
문제
모양은 같으나, 무게가 모두 다른 N개의 구슬이 있다. N은 홀수이며, 구슬에는 번호가 1,2,...,N으로 붙어 있다. 이 구슬 중에서 무게가 전체의 중간인 (무게 순서로 (N+1)/2번째) 구슬을 찾기 위해서 아래와 같은 일을 하려 한다.

우리에게 주어진 것은 양팔 저울이다. 한 쌍의 구슬을 골라서 양팔 저울의 양쪽에 하나씩 올려 보면 어느 쪽이 무거운가를 알 수 있다. 이렇게 M개의 쌍을 골라서 각각 양팔 저울에 올려서 어느 것이 무거운가를 모두 알아냈다. 이 결과를 이용하여 무게가 중간이 될 가능성이 전혀 없는 구슬들은 먼저 제외한다.

예를 들어, N=5이고, M=4 쌍의 구슬에 대해서 어느 쪽이 무거운가를 알아낸 결과가 아래에 있다.

구슬 2번이 구슬 1번보다 무겁다.
구슬 4번이 구슬 3번보다 무겁다.
구슬 5번이 구슬 1번보다 무겁다.
구슬 4번이 구슬 2번보다 무겁다.
4 > 2 ,3 > 1 
5 > 1 
위와 같이 네 개의 결과만을 알고 있으면, 무게가 중간인 구슬을 정확하게 찾을 수는 없지만, 1번 구슬과 4번 구슬은 무게가 중간인 구슬이 절대 될 수 없다는 것은 확실히 알 수 있다. 1번 구슬보다 무거운 것이 2, 4, 5번 구슬이고, 4번 보다 가벼운 것이 1, 2, 3번이다. 따라서 답은 2개이다.

M 개의 쌍에 대한 결과를 보고 무게가 중간인 구슬이 될 수 없는 구슬의 개수를 구하는 프로그램을 작성하시오.

입력
첫 줄은 구슬의 개수를 나타내는 정수 N(1 ≤ N ≤ 99)과 저울에 올려 본 쌍의 개수 M(1 ≤ M ≤ N(N-1)/2)이 주어진다. 그 다음 M 개의 줄은 각 줄마다 두 개의 구슬 번호가 주어지는데, 앞 번호의 구슬이 뒤 번호의 구슬보다 무겁다는 것을 뜻한다.

출력
첫 줄에 무게가 중간이 절대로 될 수 없는 구슬의 수를 출력 한다.

예제 입력 1 
5 4
2 1
4 3
5 1
4 2
예제 출력 1 
2
'''

from collections import deque

# 입력 받기
N, M = map(int, input().split())
heavier = {i: [] for i in range(1, N+1)}  # 무거운 구슬 리스트
lighter = {i: [] for i in range(1, N+1)}  # 가벼운 구슬 리스트


#1. 그래프 만들기 
for _ in range(M):
    a, b = map(int, input().split())
    heavier[b].append(a)  # b보다 a가 무겁다 
    lighter[a].append(b)  # a보다 b가 가볍다
#하나의 그래프를 사용해서 "a → b (a가 b보다 무겁다)" 만 저장한다면, b보다 무거운 구슬을 찾는 것은 가능하지만, a보다 가벼운 구슬을 찾는 것은 불가능 

# 2. BFS 탐색 
def count_reachable(start, graph):
    visited = set()
    queue = deque([start])
    count = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                count += 1
    return count

# 3. 무게를 기준으로 정렬했을 때, 가운데 있는 구슬의 위치가 mid번째(홀수의 중앙)
mid = (N + 1) // 2
invalid_count = 0

for i in range(1, N + 1):
    heavier_count = count_reachable(i, heavier)  # i보다 무거운 구슬 개수 무거운 구슬 개수를 찾고 
    lighter_count = count_reachable(i, lighter)  # i보다 가벼운 구슬 개수 가벼운 구슬 개수를 찾는거지. 
    
    # 절반 이상 무겁거나, 절반 이상 가벼우면 중간이 될 수 없음
    if heavier_count >= mid or lighter_count >= mid: #만약에 절반 이상 무겁거나 or 절반 이상 가벼우면
        invalid_count += 1

print(invalid_count)