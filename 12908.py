


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