'''
문제
평소 반상회에 참석하는 것을 좋아하는 주희는 이번 기회에 부녀회장이 되고 싶어 각 층의 사람들을 불러 모아 반상회를 주최하려고 한다.

이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.

아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

제한
1 ≤ k, n ≤ 14
예제 입력 1 
2
1
3
2
3
예제 출력 1 
6
10

'''
  
# 반성
# 0. 처음부터 0층을 채움 
# 1. 층을 순회할 때 :  1층~max_k층까지 채워야 함. (1,max_k+1)이 맞음.
# 2. 호수를 순회할 때 : 1호~max까지 채워야 함. 그래서 (0,max)가 맞음.
  
  
T = int(input())

for _ in range(T):  
    k = int(input())
    n = int(input())
    people = [x for x in range(1, n+1)]  
    for _ in range(k):
        for i in range(1, n): 
            people[i] += people[i-1] 
    print(people[n-1])
# # 잘못된 풀이 
# T = int(input())
# d = [[0]*14 for i in range(0,14)] #14 x 14 matrix
# d[0] = [i for i in range(1,15)] #0층은 1부터 14까지 사람이 산다. d[0][0] = 0층 1호에 사는 사람 수 d[0][1] = 0층 2호에 사는 사람 수
# k_n = [(int(input()), int(input())) for _ in range(T)]
# max_k = max(k_n, key=lambda x: x[0])[0]  # 층 최대값
# max_n = max(k_n, key=lambda x: x[1])[1] 

# for a in range(1,max_k+1): #층(이미 1층부터는 채워져있으니까)
#   for b in range(0,max_n):#호수
#     if b == 0:
#             d[a][b] = d[a - 1][b]  # 1호는 바로 아래층의 사람 수와 같음
#         else:
#             d[a][b] = d[a][b - 1] + d[a - 1][b]  # 점화식 적용

# for (k,n) in k_n:
#   print(d[k][n-1])
# 🚀 핵심 차이점

# 공간 복잡도 차이
# 네 풀이: d라는 2차원 리스트(14x14) 를 만들어서 저장함. (메모리 사용 큼)
# 정답 풀이: 1차원 리스트(people) 만 사용하여 메모리 절약함.
# 👉 교훈: 꼭 필요한 데이터만 저장하자!
# 2차원 배열 없이, 필요한 부분만 업데이트하는 방식을 연습

# 점화식 적용 방식
# 네 풀이는 d[k][n] = d[k][n-1] + d[k-1][n]을 2차원 배열에 직접 적용.
# 정답 풀이는 people[i] += people[i-1]를 사용해 1차원 리스트에서 값을 누적.
# 👉 교훈: 배열을 줄이는 테크닉 배우기

# people[i] += people[i-1] 방식처럼, 계산에 필요한 최소한의 변수만 업데이트하는 방식 고민해 보기.

# 미리 저장 vs 실시간 계산
# 네 풀이는 최대 층수, 최대 호수를 미리 계산해서 d를 전부 채움.
# 정답 풀이는 각 테스트 케이스마다 바로 계산.
# 👉 교훈: 미리 계산할 필요가 없으면, 즉시 계산하는 방법 고려
# 모든 경우를 미리 계산하지 않고, 각 케이스에 맞춰 필요한 연산만 수행하는 방식이 더 효율적,..

