'''
문제
월드컵 축구의 응원을 위한 모임에서 회장을 선출하려고 한다. 이 모임은 만들어진지 얼마 되지 않았기 때문에 회원 사이에 서로 모르는 사람도 있지만, 몇 사람을 통하면 모두가 서로 알 수 있다. 각 회원은 다른 회원들과 가까운 정도에 따라 점수를 받게 된다.

예를 들어 어느 회원이 다른 모든 회원과 친구이면, 이 회원의 점수는 1점이다. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임을 말한다. 또한 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임을 말한다.

4점, 5점 등은 같은 방법으로 정해진다. 각 회원의 점수를 정할 때 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면, 이 두사람은 친구사이라고 본다.

회장은 회원들 중에서 점수가 가장 작은 사람이 된다. 회장의 점수와 회장이 될 수 있는 모든 사람을 찾는 프로그램을 작성하시오.

입력
입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데, 이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.

출력
첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.

예제 입력 1 
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
예제 출력 1 
2 3
2 3 4
'''
from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]

# 친구 관계 입력
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

# 각 회원의 점수 계산
def bfs(start):
    visited = [-1] * (N + 1) # 여기서 set을 사용하지 않고 리스트로 방문 여부를 체크
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    
    # start에서 가장 멀리 있는 회원까지의 거리 (점수)
    return max(visited[1:])  # 0번은 무시

scores = [0] * (N + 1)
min_score = float('inf')

for i in range(1, N + 1):
    score = bfs(i)
    scores[i] = score
    min_score = min(min_score, score)

# 회장 후보 리스트 추출
candidates = [i for i in range(1, N + 1) if scores[i] == min_score]

# 출력
print(min_score, len(candidates))
print(" ".join(map(str, candidates)))
