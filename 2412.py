'''
# 암벽 등반 다국어

| 시간 제한 | 메모리 제한 | 제출 | 정답 | 맞힌 사람 | 정답 비율 |
| --- | --- | --- | --- | --- | --- |
| 2 초 | 128 MB | 4193 | 1351 | 937 | 31.969% |

## 문제

어떤 암벽에 n(1 ≤ n ≤ 50,000)개의 홈이 파져 있다. 각각의 홈의 좌표는 (x, y)와 같이 표현되는데, |a - x| ≤ 2이고 |b - y| ≤ 2이면 (x, y)에서 (a, b)로 이동할 수 있다. 이와 같이 홈들을 이용하여 이동하면서 y = T(1 ≤ T ≤ 200,000)일 때까지, 즉 암벽의 정상까지 오르려고 한다.

현재 당신이 있는 위치는 (0, 0)이다. 이 위치에서 시작하여 이동 회수를 최소로 하면서 정상에 오르려고 한다. 정상에 오를 때의 x좌표는 아무 것이나 되어도 상관이 없다.

## 입력

첫째 줄에 n, T가 주어진다. 다음 n개의 줄에는 각 점의 x, y좌표가 주어진다. 두 좌표는 모두 0이상이며, x좌표는 1,000,000이하, y좌표는 T이하이다. 입력에 현재 위치인 (0, 0)은 주어지지 않는다.

## 출력

첫째 줄에 최소 이동 회수를 출력한다. 만약, 정상에 오를 수 없으면 -1을 출력한다.

## 예제 입력 1

```
5 3
1 2
6 3
4 1
3 2
0 2

```

## 예제 출력 1
4
'''
from collections import deque

n, T = map(int,input().split())
graph = {}
for _ in range(n):
    x, y = map(int, input().split())
    if y not in graph:
        graph[y] = []
    graph[y].append(x)


queue = deque([(0, 0, 0)])  # (현재 x, 현재 y, 이동 횟수)
visited = set()
visited.add((0, 0))

while queue:
    x, y, moves = queue.popleft() #이러면 당연히 0,0,0이 나오겠지. 

    # 만약 정상 도착하면 종료
    if y >= T:
        print(moves)
        exit()

    # 일단, 내 위치에서 갈 수 있는 ny들을 본다. (y-2 ~ y+2)
    for ny in range(y - 2, y + 3):
        if ny in graph:  # 만약, 저기 그래프에 ny가 있다면 
            for nx in graph[ny]: #근데, 그 ny에 해당하는 nx들을 다 본다.
                if (nx, ny) not in visited and abs(nx - x) <= 2: #근데 만약, 방문하지 않았음 + x좌표 차이가 2이하라면
                    visited.add((nx, ny))
                    queue.append((nx, ny, moves + 1))
