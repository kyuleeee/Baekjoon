'''
문제
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

입력
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.


출력
세준이가 운전해야하는 거리의 최솟값을 출력하시오.

예제 입력 1 
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
예제 출력 1 
70
예제 입력 2 
2 100
10 60 40
50 90 20
예제 출력 2 
80
예제 입력 3 
8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0
예제 출력 3 
432
''' 
import heapq

# 입력 받기
# 일단, 입력받는 그런 다양한 애들을 하나의 '기점'이라고 보았음. 
# 예제 입력 1의 경우에는, 0,50,100,110,140,151 이런 애들이 하나의 기점인 거지. 

# 1. 입력 받기 
n, d = map(int,input().split())
graph = {}
for _ in range(n):
        a, b, c = map(int, input().split())
        if b > m or b - a <= c:  # 유효하지 않은 지름길은 제외
            continue
        if a not in graph: # 없으면 추가하기 
            graph[a] = []
        graph[a].append((b, c))
        
# 예시로 보자면, graph = {
#     0: [(50, 10), (50, 20)],
#     50: [(100, 10)],
#     100: [(151, 10)]
# }
        
        
# 최단 거리 배열 초기화
INF = float('inf')
dist = [INF] * (d + 1) #dist는 각 위치에 도달하는 최단 거리를 저장
dist[0] = 0

# 우선순위 큐 (거리, 현재 위치)
pq = [(0, 0)]  #pq는 탐색할 위치들을 넣고 꺼내는 곳

while pq:
    cur_dist, cur_pos = heapq.heappop(pq) #큐에서 가장 작은 값(거리) 꺼내기
    #일단 현재 거리, 그리고 현재 위치를 뽑는다.

    if cur_dist > dist[cur_pos]: #이미 더 짧은 경로가 있다면 무시
        continue
    #이미 그 위치로 가는 더 짧은 경로가 있으면, 지금 꺼낸 경로는 다시 계산하지 않도록...

    # 일반 도로 이동 (한 칸씩 이동)
    if cur_pos + 1 <= d and dist[cur_pos + 1] > cur_dist + 1:
        dist[cur_pos + 1] = cur_dist + 1
        heapq.heappush(pq, (dist[cur_pos + 1], cur_pos + 1))

    # 지름길 이동
    if cur_pos in graph: #현재 위치에 지름길이 있다면, 그 지름길을 고려해 이동
        for next_pos, shortcut_dist in graph[cur_pos]:
            if dist[next_pos] > cur_dist + shortcut_dist:
                dist[next_pos] = cur_dist + shortcut_dist
                heapq.heappush(pq, (dist[next_pos], next_pos))

# 최단 거리 출력
print(dist[d])