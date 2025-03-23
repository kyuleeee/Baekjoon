'''
텔레포트 3
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	1310	600	493	47.358%
문제
수빈이는 크기가 무한대인 격자판 위에 살고 있다. 격자판의 각 점은 두 정수의 쌍 (x, y)로 나타낼 수 있다.

제일 처음에 수빈이의 위치는 (xs, ys)이고, 집이 위치한 (xe, ye)로 이동하려고 한다.

수빈이는 두 가지 방법으로 이동할 수 있다. 첫 번째 방법은 점프를 하는 것이다. 예를 들어 (x, y)에 있는 경우에 (x+1, y), (x-1, y), (x, y+1), (x, y-1)로 이동할 수 있다. 점프는 1초가 걸린다.

두 번째 방법은 텔레포트를 사용하는 것이다. 텔레포트를 할 수 있는 방법은 총 세 가지가 있으며, 미리 정해져 있다. 텔레포트는 네 좌표 (x1, y1), (x2, y2)로 나타낼 수 있으며, (x1, y1)에서 (x2, y2)로 또는 (x2, y2)에서 (x1, y1)로 이동할 수 있다는 것이다. 텔레포트는 10초가 걸린다.

수빈이의 위치와 집의 위치가 주어졌을 때, 집에 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 xs와 ys가, 둘째 줄에 xe, ye가 주어진다. (0 ≤ xs, ys, xe, ye ≤ 1,000,000,000)

셋째 줄부터 세 개의 줄에는 텔레포트의 정보 x1, y1, x2, y2가 주어진다. (0 ≤ x1, y1, x2, y2 ≤ 1,000,000,000)

입력으로 주어지는 모든 좌표 8개는 서로 다르다.

출력
수빈이가 집에 가는 가장 빠른 시간을 출력한다.

예제 입력 1 
3 3
4 5
1000 1001 1000 1002
1000 1003 1000 1004
1000 1005 1000 1006
예제 출력 1 
3
예제 입력 2 
0 0
20 20
1 1 18 20
1000 1003 1000 1004
1000 1005 1000 1006
예제 출력 2 
14
예제 입력 3 
0 0
20 20
1000 1003 1000 1004
18 20 1 1
'''

import heapq

#다익스트라 알고리즘 
def dijkstra(start, graph,dist):
    dist[start] = 0 #일단 0으로 만들어버리고! (튜플이니까 괜춘)
    pq = [(0, start)] #일단 priority queue 만들구
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        # 지금까지의 시간과 지금 현재 있는 그 노드 
        if current_dist > dist[current_node]:
            continue
        # 위아래양옆은 그냥 graph에서 따오는 게 아니라 진짜 그냥 흠 그래프에서 따와야 하나? => 메모리 이슈로 너무 오래 걸린다
        # 
        for neighbor, time in graph[current_node]:
            distance = current_dist + time #일단 distance를 구해보고
            if distance < dist[neighbor]: #만약 
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return dist

#distance만들기  => 근데 distance를 어떻게 만들어야 할지도 핵심
xs,ys = map(int,input().split())
xe,ye = map(int,input().split())
graph = [[] for _ in range(3)] 
#distance 만들기 => 근데 distance어떻게 만들지도 조금 생각하기 힘들었음. 
dist = [INF] * (abs(xs-xe) + 1) * (abs(ys-ye) + 1)
#어차피 튜플로 할거니까, 굳이 2차원 배열로 dist를 만들지 않아도 될듯!(취소)
#차라리 2차원 배열로 만드는 게 나을 거 같다. 

for i in range((xs,ys),(xe,ye)):
#graph 만들기 : 타임머신 graph로 만들어주기 
for _ in range(3):
    x1,y1,x2,y2 = map(int,input().split())
    #만약 graph가 기존의 규칙보다 더 오래 걸린다면 : pass 
    #만약 end까지 가는 길에 없으면 : pass
    

dijkstra((xs,ys),graph,dist)
print(distance[(xe,ye)])