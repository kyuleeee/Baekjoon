'''
림
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	57102	25767	17492	43.512%
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

예제 입력 1 
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
예제 출력 1 
4
9
'''
from collections import deque

# 입력 받기
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  # 방문한 곳은 0으로 바꿔서 재방문 방지
    size = 1  # 그림 크기
    
    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):  # 네 방향 탐색
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0  # 방문 처리
                size += 1
    
    return size  # 탐색한 그림 크기 반환

# 그림 개수와 가장 큰 그림의 크기 구하기
count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:  # 아직 방문하지 않은 그림 시작점
            count += 1
            max_size = max(max_size, bfs(i, j))

print(count)
print(max_size)


