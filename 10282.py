'''
## 문제

최흉최악의 해커 yum3이 네트워크 시설의 한 컴퓨터를 해킹했다! 이제 서로에 의존하는 컴퓨터들은 점차 하나둘 전염되기 시작한다. 어떤 컴퓨터 a가 다른 컴퓨터 b에 의존한다면, b가 감염되면 그로부터 일정 시간 뒤 a도 감염되고 만다. 이때 b가 a를 의존하지 않는다면, a가 감염되더라도 b는 안전하다.

최흉최악의 해커 yum3이 해킹한 컴퓨터 번호와 각 의존성이 주어질 때, 해킹당한 컴퓨터까지 포함하여 총 몇 대의 컴퓨터가 감염되며 그에 걸리는 시간이 얼마인지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 개수는 최대 100개이다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

- 첫째 줄에 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터의 번호 c가 주어진다(1 ≤ n ≤ 10,000, 1 ≤ d ≤ 100,000, 1 ≤ c ≤ n).
- 이어서 d개의 줄에 각 의존성을 나타내는 정수 a, b, s가 주어진다(1 ≤ a, b ≤ n, a ≠ b, 0 ≤ s ≤ 1,000). 이는 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨을 뜻한다.

각 테스트 케이스에서 같은 의존성 (a, b)가 두 번 이상 존재하지 않는다.

## 출력

각 테스트 케이스마다 한 줄에 걸쳐 총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간을 공백으로 구분지어 출력한다.

## 예제 입력 1

```
2
3 2 2
2 1 5
3 2 5
3 3 1
2 1 2
3 1 8
3 2 4

```

## 예제 출력 1

```
2 5
3 6
```
'''
import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (거리, 노드)
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

        
N = int(input())  # 테스트 케이스 개수
INF = int(1e9)
for _ in range(N):  
    n, d, c = map(int, input().split())  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호(start라고 치면 될듯)
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for _ in range(d):  
        a, b, s = map(int, input().split())  
        graph[b].append((a, s))  # b가 감염되면 s초 후 a가 감염됨

    dijkstra(c)  

    # 감염된 컴퓨터 수와 최종 감염 시간 계산
    infected_count = sum(1 for d in distance if d < INF)
    max_time = max(d for d in distance if d < INF) #if가 필요함. 
    #max(0,4,6) 이렇게 되어서 max인 6만 뽑히는 것임

    print(infected_count, max_time)
    