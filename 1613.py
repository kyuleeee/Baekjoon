'''
## 문제

역사, 그 중에서도 한국사에 해박한 세준이는 많은 역사적 사건들의 전후 관계를 잘 알고 있다. 즉, 임진왜란이 병자호란보다 먼저 일어났으며, 무오사화가 기묘사화보다 먼저 일어났다는 등의 지식을 알고 있는 것이다.

세준이가 알고 있는 일부 사건들의 전후 관계들이 주어질 때, 주어진 사건들의 전후 관계도 알 수 있을까? 이를 해결하는 프로그램을 작성해 보도록 하자.

## 입력

첫째 줄에 첫 줄에 사건의 개수 n(400 이하의 자연수)과 알고 있는 사건의 전후 관계의 개수 k(50,000 이하의 자연수)가 주어진다. 
다음 k줄에는 전후 관계를 알고 있는 두 사건의 번호가 주어진다. 이는 앞에 있는 번호의 사건이 뒤에 있는 번호의 사건보다 먼저 일어났음을 의미한다. 물론 사건의 전후 관계가 모순인 경우는 없다. 
다음에는 사건의 전후 관계를 알고 싶은 사건 쌍의 수 s(50,000 이하의 자연수)이 주어진다. 다음 s줄에는 각각 서로 다른 두 사건의 번호가 주어진다. 사건의 번호는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

## 출력

s줄에 걸쳐 물음에 답한다. 각 줄에 만일 앞에 있는 번호의 사건이 먼저 일어났으면 -1, 뒤에 있는 번호의 사건이 먼저 일어났으면 1, 어떤지 모르면(유추할 수 없으면) 0을 출력한다.

## 예제 입력 1

```
5 5
1 2 
1 3
2 3
3 4
2 4
3
1 5
2 4
3 1

```

## 예제 출력 1
0
-1
1

'''
from collections import deque 
n,k = map(int,input().split()) #n개의 사건, k개의 줄이 등장한다는 거임. 
graph = {i: [] for i in range(1, n + 1)}
for _ in range(k):
  a,b = map(int,input().split())
  graph[a].append(b) # 가 b보다 먼저 일어남. 
s = int(input()) #사건의 전후 관계를 알고 싶은 사건 쌍의 수 s

def bfs(start, end):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        
        # 다음 노드 탐색
        for neighbor in graph[node]:
            if neighbor == end:  # 목표 노드가 있으묜
                return -1  # start가 end보다 먼저 일어남 바로 리턴 
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return 0  # start → end 경로 없음 (모름)

for _ in range(s):
    x, y = map(int,input().split())

    # x → y로 가는 경로 확인
    result_xy = bfs(x, y)

    if result_xy == -1:
        print(-1)
    else:
        # y → x 경로 확인
        result_yx = bfs(y, x)
        if result_yx == -1:
            print(1)  # y가 x보다 먼저 일어남
        else:
            print(0)  # 관계를 알 수 없음    
      
'''
1. 그래프
    1. 일단, BFS로… 
2. 전후관계 알려주기
    1. BFS 탐색인데
        1. 먼저 일어났는지 안일어났는지는 가능 : visited에 있으면 ok? / neighbor에 있어야 ok?
        ⇒ 걍 neighbor. 
        2. 뒤에 있는 번호의 사건이 먼저? : 그냥 단순히 BFS(x,y)로 한다음에 그게 return이 -1이 안나오면 바로 뒤에 있다고 단정하면 안됨. 얘도  BFS(y,x)로 테스트해봐야함.
        3. 아예 유추 불가 : 1,2번 다 아닌 경우…
'''