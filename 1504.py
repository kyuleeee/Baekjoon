'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.

예제 입력 1 
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
예제 출력 1 
7
'''
import heapq 
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  
    #힙큐에 0이라는 
    distance[start] = 0 #일단 start는 0으로 두고 
    
    while q:
        dist, now = heapq.heappop(q) #q에서 dist랑 현재를 뽑는다.
        if dist > distance[now]: 
            continue
        
        for next_node, cost in graph[now]: #graph에 노드.(노드,초) 일케 되어 있으니
            new_dist = dist + cost #기존 dist랑 cost를 더해서 new_dist라고 치고
            if new_dist < distance[next_node]:  # 만약 더 짧은 경로를 발견햇다면
                distance[next_node] = new_dist 
                heapq.heappush(q, (new_dist, next_node)) #heapq로!
      return distance


  
N,E = map(int,input().split()) #1번 정점에서 N번정점으로 가고 싶어 한다. 그리고 간선의 개수 E 
INF = int(1e9)
#궁금했던점은, 양방향이니까 graph 자체도 뭔가 양방향으로 해야하는 게 아닐까? 크기를 늘려야하는 거 아닐까?
#근데, 사실 그냥 한지점에서 다른 지점까지의 거리니까. 
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split()) #반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2 -> start와 end가 아님. 이건 정점이야.
#주어진 두 정점을 반드시 거치면서~최단경로로 이동을 해야한다...! 
#그렇다면, 1에서 v1까지 갈때도 최소 + v1에서 v2까지도 최소 + v2에서 N까지도 최소가 되어야 겠군
# 각 경로를 순차적으로 계산할 경로 목록을 만든다.
start_nodes = [(1, v1), (v1, v2), (v2, N)]  # (시작 노드, 끝 노드) 튜플로 구성
total_distance = 0  # 총 거리를 계산할 변수

# 각 경로에 대해 다익스트라를 실행하고, 그 거리들을 합산
for start, end in start_nodes:
    distance = [INF] * (N + 1)  # 각 경로마다 거리 배열을 새로 초기화
    dijkstra(start)  # 다익스트라 실행
    total_distance += distance[end]  # 최단 거리를 더해준다
    
    if distance[end] == INF:  # 경로가 없으면 -1 출력
        print(-1)
        break
else:
    print(total_distance)  # 모든 경로가 유효하다면 총합을 출력