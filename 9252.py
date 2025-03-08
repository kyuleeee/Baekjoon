'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
ACAK

'''
a_list, b_list = input().split(), input().split()

n, m = len(a_list), len(b_list)
d = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  if a[i - 1] == b[j - 1]:  # 문자가 같다면
            d[i][j] = d[i - 1][j - 1] + 1
        else:  # 다르면 위쪽과 왼쪽 중 큰 값 선택
            d[i][j] = max(d[i - 1][j], dp[i][j - 1])
            
print(d[n][m]) #이렇게 해 결국 그 값을 찾는 것이.다. 


#어려워서 GPT와 함께. 
#그러면 어떤 값이 나오는지?
lcs = []
i, j = n, m  # dp 테이블의 오른쪽 아래에서 시작

while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:  # 문자가 같으면 LCS에 추가
        lcs.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:  # 위쪽 값이 더 크면 위로 이동
        i -= 1
    else:  # 왼쪽 값이 더 크면 왼쪽으로 이동
        j -= 1

lcs.reverse()  # 거꾸로 저장됐으므로 뒤집기
print("".join(lcs))  # 리스트를 문자열로 변환해 출력