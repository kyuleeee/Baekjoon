import sys
input = sys.stdin.readline

N = int(input())
student_num = [input().strip() for _ in range(N)]

for k in range(1, len(student_num[0]) + 1):  # 최대 자릿수까지만 탐색
    seen = set()
    for num in student_num:
        seen.add(num[-k:])
    if len(seen) == N:
        print(k)
        break
