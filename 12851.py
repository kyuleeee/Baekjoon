'''
숨바꼭질 2
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	512 MB	69245	19798	13710	25.996%
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

예제 입력 1 
5 17
예제 출력 1 
4
2
'''

#수빈이는 동생과 숨바꼭질을 하고 있다.
#수빈이는 N에 있고, 동생은 K에 있다.
#수빈이는 걷거나 순간이동을 할 수 있다.
#수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
#순간이동이라면 1초 후에 2*X의 위치로 이동하게 된다.

from collections import deque

N,K = map(int,input().split())

#이동방법 1 : 
#1초 후에 X-1 또는 X+1로 이동하게 된다.
#이동방법 2 : 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#이렇게 해서 그래프를 만들어야 한다.

# graph = {}
# def make_graph(N,graph,K):
#   if N not in graph:
#     graph[N] = []
#   if N-1 <= K :
#       graph[N].append(N-1)
#       make_graph(N-1)
#   if N+1 <= K :
#       graph[N].append(N+1)
#       make_graph(N+1)
#   if 2*N <= K :
#       graph[N].append(2*N)
#       make_graph(2*N)
#       return graph
# 이렇게 하면 그래프가 만들어지겠지?
# make_graph(N)
def bfs(N,K):
  queue = deque([N]) #일단 deque에 N을 넣고 
  visited = set()
  visited.add(N)
  time = 0
  count = 0
  while queue:
    size = len(queue)
    for _ in range(size):
      node = queue.popleft()
      if node == K: #만약 도달했다면 바로!!! 
        count += 1
        neighbors = [(node-1), (node+1), (2*node)]
      for neighbor in neighbors:
        if 0<= neighbor<=100000 and neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
    if count > 0:
      break
    time += 1
  return time,count

time,count = bfs(N,K)
print(time)
print(count)

"
