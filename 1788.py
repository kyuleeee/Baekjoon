'''
수학에서, 피보나치 수는 위의 점화식과 같이 귀납적으로 정의되는 수열이다. 위의 식에서도 알 수 있듯이, 피보나치 수 F(n)은 0 이상의 n에 대해서만 정의된다.

하지만 피보나치 수 F(n)을 n이 음수인 경우로도 확장시킬 수 있다. 위의 식에서 n > 1인 경우에만 성립하는 F(n) = F(n-1) + F(n-2)를 n ≤ 1일 때도 성립되도록 정의하는 것이다. 예를 들어 n = 1일 때 F(1) = F(0) + F(-1)이 성립되어야 하므로, F(-1)은 1이 되어야 한다.

n이 주어졌을 때, 피보나치 수 F(n)을 구하는 프로그램을 작성하시오. n은 음수로 주어질 수도 있다.
입력
첫째 줄에 n이 주어진다. n은 절댓값이 1,000,000을 넘지 않는 정수이다.

출력
첫째 줄에 F(n)이 양수이면 1, 0이면 0, 음수이면 -1을 출력한다. 둘째 줄에는 F(n)의 절댓값을 출력한다. 이 수가 충분히 커질 수 있으므로, 절댓값을 1,000,000,000으로 나눈 나머지를 출력한다.

예제 입력 1 
-2
예제 출력 1 
-1
1
예제 입력 2 
0
예제 출력 2 
0
0
예제 입력 3 
10
예제 출력 3 
1
55
예제 입력 4 
-7
예제 출력 4 
1
13
'''
# 입력 받기
n = int(input())# 입력값 n을 정수로 변환
MOD = 1000000000  # 결과를 나눌 모듈러 값 (문제 조건)

# 음수 피보나치 처리하기 위해 절댓값 사용
n_abs = abs(n)  # n의 절댓값을 구해서 피보나치 계산에 사용

# 피보나치 수열을 저장할 리스트 (0부터 n_abs까지 필요)
fib = [0] * (n_abs + 1)  # 크기가 n_abs + 1인 리스트 생성 (0으로 초기화)

# 초기값 설정
fib[0] = 0  # F(0) = 0
if n_abs > 0:
    fib[1] = 1  # F(1) = 1

# 피보나치 수열을 DP(Dynamic Programming) 방식으로 계산
for i in range(2, n_abs + 1):  # 2부터 n_abs까지 반복
    fib[i] = (fib[i-1] + fib[i-2]) % MOD  # 점화식 적용 (나머지 연산으로 오버플로우 방지)

# 피보나치 결과의 부호 결정
if n == 0:
    print(0)  # F(0) = 0일 때 부호는 0 (출력 끝)
elif n > 0 or n % 2 == 1:  
    # (1) n이 양수이면 항상 F(n)은 양수 → 부호: 1
    # (2) n이 음수인데 홀수이면, (-1)^(n+1) * F(n)에서 부호가 유지됨 → 부호: 1
    print(1)
else:
    # n이 음수인데 짝수이면, (-1)^(n+1) * F(n)에서 부호가 반전됨 → 부호: -1
    print(-1)

# 최종 피보나치 수의 절댓값 출력
print(fib[n_abs])  # 미리 계산한 fib 값 출력
