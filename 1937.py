'''
욕심쟁이 판다
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	256 MB	50911	16843	11162	30.177%
문제
n × n의 크기의 대나무 숲이 있다. 욕심쟁이 판다는 어떤 지역에서 대나무를 먹기 시작한다. 그리고 그 곳의 대나무를 다 먹어 치우면 상, 하, 좌, 우 중 한 곳으로 이동을 한다. 그리고 또 그곳에서 대나무를 먹는다. 그런데 단 조건이 있다. 이 판다는 매우 욕심이 많아서 대나무를 먹고 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 많이 있어야 한다.

이 판다의 사육사는 이런 판다를 대나무 숲에 풀어 놓아야 하는데, 어떤 지점에 처음에 풀어 놓아야 하고, 어떤 곳으로 이동을 시켜야 판다가 최대한 많은 칸을 방문할 수 있는지 고민에 빠져 있다. 우리의 임무는 이 사육사를 도와주는 것이다. n × n 크기의 대나무 숲이 주어져 있을 때, 이 판다가 최대한 많은 칸을 이동하려면 어떤 경로를 통하여 움직여야 하는지 구하여라.

입력
첫째 줄에 대나무 숲의 크기 n(1 ≤ n ≤ 500)이 주어진다. 그리고 둘째 줄부터 n+1번째 줄까지 대나무 숲의 정보가 주어진다. 대나무 숲의 정보는 공백을 사이로 두고 각 지역의 대나무의 양이 정수 값으로 주어진다. 대나무의 양은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에는 판다가 이동할 수 있는 칸의 수의 최댓값을 출력한다.

예제 입력 1 
4
14 9 12 10
1 11 5 4
7 15 2 13
6 3 16 8
예제 출력 1 
4
'''
from collections import deque
#nxn크기의 대나무숲이 있다.
n = int(input())
#그곳의 대나무를 다 먹어치우면 상,하,좌,우 중 한곳으로 이동! 
#과연 어떤지점에 처음에 풀어놓아야 하는걸까? 
#어떤 곳으로 이동을 시켜야 판다가! 최대한 많은칸을 방문할 수 있을지...-> visit_count가 젤 크도록. 

# 흠 가능한 화살표가 있고 아닌 화살표가 있겠네 
# 일단 중요한건, 저 숫자가 아니고 화살표로 갈 수 있느냐 마느냐다. 진심.
# 그렇다면, 화살표 그래프를 만들어볼까?
graph = [[[] for _ in range(n)] for _ in range(n)]


# 대나무 숲 정보 입력
bamboo = [list(map(int, input().split())) for _ in range(n)] #요거 조금 힘듦

# 상하좌우 방향 (dx, dy)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 대나무 양을 기준으로 갈 수 있는 방향을 화살표 그래프 형식으로 만들어보기
for i in range(n):
    for j in range(n):
        # 상하좌우 방향 탐색
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            # 범위 내에 있고, 대나무 양이 더 많은 곳으로만 이동 가능
            if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[i][j]:
                graph[i][j].append((nx, ny))  # (nx, ny)로 갈 수 있다!
                
                
visited = [[False] * n for _ in range(n)]

#dfs
def dfs(x,y,depth):
	visited[x][y] = True
	max_depth = 1
	
	#일단 상하좌우 neighbor들이,그래프에 있다면 
	for nx,ny in graph[x][y] : #해당하는 nx,ny가 나오겠지? 
			if visited[nx][ny] == False :
						max_depth = max(max_depth, 1 + dfs(nx, ny))
	
	visited[x][y] = False  # 다른 경로를 위해 방문 기록을 초기화
  
  return max_depth

#max_result 만들기 
max_result = 0
for i in range(n):
	for j in range(n):
			max_result = max(max_result, dfs(i, j))
			
print(max_result)