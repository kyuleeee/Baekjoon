"""

문제
스탠과 올리는 정수 맞추기 게임을 하고 있다. 스탠은 1과 10사이의 정수 하나를 생각하고, 올리는 스탠이 생각한 수를 맞춰야 한다. 올리가 수를 말할 때마다 스탠은 올리가 말한 수가 큰지, 작은지, 일치하는지를 말해준다.

게임이 몇 번 진행된 후 올리는 스탠이 거짓말을 하고 있다는 생각을 하게 되었다. 즉, 올리는 수를 말할때 마다 스탠이 자신이 생각한 수를 바꿀수도 있다는 생각을 했다. 이런 일이 실제로 벌어지는지 알아내기 위해서, 올리는 게임이 진행되면서 자신이 외친 수와 스탠이 말한 답변을 모두 적어놓았다.

올리가 외친 수와 스탠의 답변이 주어졌을 때, 스탠이 거짓말을 했는지 아닌지 알아내는 프로그램을 작성하시오.

입력
입력은 여러 개의 게임으로 이루어져 있다. 각 게임은 올리가 외친 수와 스탠의 답변으로 이루어져 있으며, 계속해서 번갈아가면서 주어진다.

올리가 외친 수는 1보다 크거나 같고, 10보다 작거나 같은 자연수이고, 스탠의 답변은 "too high", "too low", "right on" 중 하나이다.

"too high"는 올리가 외친 수가 스탠이 생각한 수보다 클 때, "too low"는 작을 때, "right on"은 일치할 때이다.

스탠의 답변이 "right on"이면, 게임이 끝난 것이다.

입력의 마지막 줄에는 0이 주어진다.

출력
각각의 게임에 대해서, 스탠이 거짓말을 한 적이 있다면 "Stan is dishonest"를, 없다면 "Stan may be honest"를 출력한다.


예제 입력 1 
10
too high
3
too low
4
too high
2
right on
5
too low
7
too high
6
right on
0


예제 출력 1 
Stan is dishonest
Stan may be honest

"""


num_list = [i for i in range(1, 11)]  # 1부터 10까지의 숫자 리스트
flag = True

while flag:
    while True:
        num = int(input())  # 숫자 입력 받기
        if num == 0:  # 0이면 종료
            flag = False
            break
        comment = input()  # 코멘트 입력 받기

        if comment == "too high":
            num_list = [i for i in num_list if i < num]  # num보다 작은 값만 남기기
        elif comment == "too low":
            num_list = [i for i in num_list if i > num]  # num보다 큰 값만 남기기
        elif comment == "right on":
            if num in num_list:  # num이 남아 있는지 확인
                print("Stan may be honest")
            else:
                print("Stan is dishonest")
            num_list = [i for i in range(1, 11)]  # 리스트 초기화 (새로운 게임 시작)
            break 


# 알아두어야 할 점
# remove 대신 저 list comprehension 쓰는 게 훨씬 낫다. 
