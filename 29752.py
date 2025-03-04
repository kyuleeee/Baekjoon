'''
문제
solved.ac 사이트에는 문제를 며칠 연속으로 풀었는지 보여주는 지표가 있는데, 이를 스트릭이라고 한다. 총 x일 동안 매일 1문제 이상을 빠짐없이 풀었다면 x일이라고 한다.

최장 스트릭은 총 N일 기간 내에 달성한 스트릭 중 가장 큰 값을 의미한다. N일 동안의 푼 문제 수를 입력받아 최장 스트릭을 구하시오.

입력
첫 번째 줄에 N이 주어진다. (1 <= N <= 1000)

두 번째 줄에 $s_1$, $s_2$, $\cdots$, $s_N$이 공백으로 구분되어 주어진다. $s_i$는 $i$일차에 푼 문제 수를 의미한다. (0 <= s_i <= 100)

출력
최장 스트릭을 출력한다.

예제 입력 1 
4
1 4 0 1
예제 출력 1 
2
예제 입력 2 
5
1 6 3 8 3
예제 출력 2 
5

'''

N = int(input())
s = list(map(int,input().split()))
cur_cnt = 0
max_cnt = 0
for i in range(0,N):
    if s[i] == 0 :
      cur_cnt = 0
    else : 
      cur_cnt += 1
    if cur_cnt > max_cnt : #이건 공통되게 적용되는 것! 
      max_cnt = cur_cnt
print(max_cnt)

# 반성할 점
# 조금 저 반복문이 헷갈렸다. 공통되게 적용되는 게 뭔지 생각해 보는 게 젤 중요한 거 같다. 
# N = int(input())
# s = list(map(int,input().split()))
# cur_cnt = 0
# max_cnt = 0
# for i in range(0,N):
#     if s[i] == 0 :
#       cur_cnt = 0
#       max(cur_cnt,max_cnt)
#     else : 
#       cur_cnt += 1
#       max(cur_cnt,max_cnt)
# print(max_cnt)