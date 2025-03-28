'''
문제
상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다. 상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.

상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다. 이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다. 둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다. 다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. (1 ≤ ai < bi ≤ n) ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다. 

출력
첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.

예제 입력 1 
6
5
1 2
1 3
3 4
2 3
4 5
예제 출력 1 
3
예제 입력 2 
6
5
2 3
3 4
4 5
5 6
2 5
예제 출력 2 
0
'''

from collections import deque
n = int(input())
m = int(input())
graph = {}
for _ in range(m):
  ai,bi = map(int,input().split())
  if ai not in graph:
    graph[ai] = []
  if bi not in graph:
    graph[bi] = []
  graph[ai].append(bi)
  graph[bi].append(ai)

#첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다. 
#자신의 친구 + 친구의 친구 -> 일단 bfs?
# BFS 함수
def bfs(start):
    visited = [False] * (n + 1)  # 방문 체크 배열
    visited[start] = True
    queue = [(start, 0)]  # (노드, depth) 형태로 큐에 저장
    invite = set()  # 초대할 친구들을 저장할 집합
    
    while queue:
        node, depth = queue.pop(0)  # 큐에서 하나 꺼내기
        
        # 깊이가 2보다 커지면 더 이상 탐색하지 않음
        if depth > 2:
            continue
        
        for neighbor in graph[node]:  # 친구 탐색
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))
                
                # 상근이의 친구들
                if depth == 1:
                    invite.add(neighbor)
                # 상근이의 친구의 친구들
                elif depth == 2:
                    invite.add(neighbor)
    
    return invite


# BFS 시작: 상근이의 친구들 및 친구의 친구들 구하기
invite = bfs(1)

# 초대할 사람의 수 출력
print(len(invite))






# 상근이의 친구들
friends = graph[1] #상근이 친구들
invite = []
for friend in friends:
  if freind in invite:
    continue
  invite.append(friend)

#invite의 숫자세기 
print(len(invite))


