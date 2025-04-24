from itertools import combinations
from collections import deque
import copy
def get_empty_positions(mapp):
	return [(i,j) for i in range(N) for j in range(M) if mapp[i][j] == 0]

def get_virus_positions(mapp):
	return [(i,j) for i in range(N) for j in range(M) if mapp[i][j] == 2]

def spread_virus(mapp,virus_positions):
	#1. 일단 바이러스를 BFS로 싹다 해버리는 것.  
	q = deque(virus_list)
	directions = [(-1,0),(1,0),(0,-1),(0,1)]
	
	#2. while
	while q : 
		x,y = q.popleft()
		for dx,dy in directions : 
				nx = x + dx 
				ny = y + dy 
				
				if 0 <= nx < N and 0 <= ny < M and mapp[x][y] == 0 :
				mapp[nx][ny] = 2 
				q.append((nx,ny))
				
#메인 코드 
#1. 배열 만들기 
N, M = map(int, input().split())  # N행 M열
mapp = []

for _ in range(N):  # N번 입력 받아야 함!
    mapp.append(list(map(int, input().split())))

#2
empty_positions = get_empty_positions(mapp)
virus_positions = get_virus_positions(mapp)

max_safe = 0 
#2-a 벽을 세울 수 있는 조합을 구한다
#2-b 각 조합에 대해:
for walls in combinations(empty_positions,3):
	#2-b-a 벽을 세운다
	#2-b-a-1 임시 배열 만듦 
	temp_mapp = copy.deepcopy(mapp)
	#2-b-a-2 그리고 나서 temp에 넣는다. 1을 
	for x,y in walls:
		temp_mapp[x][y] = 1 
	#2-b-b 바이러스 퍼뜨린다. 
	spread_virus(mapp,virus_positions) 
	#2-b-c 센다.  
	safe = count_safe_area(temp_mapp)
	#2-b-d 최댓값 저장 
	max_safe = max(max_safe,safe)

print(max_safe)	