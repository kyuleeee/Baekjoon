'''
명제 증명
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	3786	1128	899	29.739%
문제
수학, 혹은 논리학에서 만약 무엇 이라면 뭣 일 것이다 하는 식의 명제가 널리 쓰인다. 예를 들어 "P이면 Q일 것이다." 라는 명제는 “P => Q” 라는 기호로 표현된다. 이때의 P를 전건, Q를 후건이라고 한다.

논리학에서 어떤 명제를 증명할 때 가장 널리 쓰이는 방법 중 한 가지가 바로 삼단 논법이다. 만약 두 명제 “P => Q", "Q => R" 가 모두 참이면, 명제 "P => R"이 역시 참이 된다. 이러한 방법을 사용했을 때 명제 ”P => R"이 증명되었다고 한다.
```
어떤 참인 명제가 주어졌을 때, 이 명제가 참이므로 이 명제 자체도 증명될 수 있다고 할 수 있다. 하지만 “P => P”와 같은 명제는 항상 참이 되는데, 이런 식으로 전건과 후건이 같은 경우는 출력하지 않기로 한다.

N개의 참인 명제들이 주어졌을 때, 증명될 수 있는 명제를 모두 구해내는 프로그램을 작성하시오. 명제를 증명하는 방법은 여러 가지가 있을 수 있지만, 위에서 언급한 방법만을 사용하기로 한다.

입력
첫째 줄에 정수 N(1 ≤ N ≤ 10,000)이 주어진다. 다음 N개의 줄에는 참인 명제들이 주어진다. 명제는 "P => Q"의 꼴로 주어지는데, “=>”는 앞뒤가 공백으로 구분되어 있다. P나 Q는 명제를 나타내는 문자인데, 알파벳 대소문자 한 글자를 사용한다. 같은 명제가 여러 번 주어질 수도 있다.

출력
첫째 줄에 출력할 명제의 개수 X개를 출력한다. 다음 X개의 줄에 증명될 수 있는 명제를 한 줄에 하나씩 출력한다. 명제를 출력할 때에는 전건 순으로 정렬하고, 전건이 같은 경우에는 후건 순으로 정렬한다. 알파벳은 대문자가 소문자에 우선한다. 즉, 정렬했을 때 A, B, …, Z, a, b, …, z 순서로 나와야 한다.

예제 입력 1 
2
A => b
b => C
예제 출력 1 
3
A => C
A => b
b => C
'''
# 증명될 수 있는 명제를 모두 구해내는 프로그램
def floyd_warshall(graph, nodes):
    reachable = {node: set() for node in nodes}

    for node in graph:
        reachable[node] = set(graph[node])

    for k in nodes:
        for i in nodes:
            if k in reachable[i]:  
                reachable[i] |= reachable[k]  # i에서 k로 갈 수 있다면, k의 모든 뒤에 있는 애들도 연결

    return reachable 

N = int(input())
graph = {}
nodes = set() #여기서 nodes를 만들어야 했어.

for _ in range(N):
    a, _, b = input().split()
    if a not in graph:
        graph[a] = set()
    graph[a].add(b)
    nodes.add(a)
    nodes.add(b)

reachable = floyd_warshall(graph, nodes)
result = []

#애초에 nodes가 있어야지 for문을 돌릴 수  있음 
for i in sorted(nodes, key=lambda x: (x.islower(), x)):
    for j in sorted(reachable[i], key=lambda x: (x.islower(), x)): #reachable한 애들을 이제 result에 넣는겨
        if i != j:
            result.append(f"{i} => {j}")

print(len(result))
for r in result:
    print(r)
  