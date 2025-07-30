'''
문제
N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 수가 주어진다.

출력
첫째 줄에 정답 정사각형의 크기를 출력한다.

예제 입력 1 
3 5
42101
22100
22101
예제 출력 1 
9
예제 입력 2 
2 2
12
34
예제 출력 2 
1
# '''

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
matrix = [[int(cell) for cell in row] for row in matrix]


max_size = 1 
for i in range(N):
    for j in range(M): 
      start = matrix[i][j]
      for length in range(1,min(N-i, M-j)):
          if start == matrix[i][j+length] == matrix[i+length][j] == matrix[i+length][j+length]:
              max_size = max(max_size, (length + 1) ** 2)
              
print(max_size)
