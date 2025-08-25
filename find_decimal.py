# 프로그래머스 소수 찾기
from itertools import permutations

def solution(numbers):
    def is_prime(n):
        if n < 2:  # 0, 1, 음수는 소수가 아님
            return False
        for i in range(2, int(n**0.5) + 1):  # √n까지만 확인
            if n % i == 0:
                return False
        return True

    primes = []
    primes = set(primes)
    digits = [int(c) for c in numbers]
    
    for pick_size in range(1, len(digits) + 1):
        #[(1,2,3,4),(1,2,3,5),(1,2,3,6),(2,3,4,5),(2,3,4,6)]
        digit_combinations = permutations(digits, pick_size) 
        
        # (1,2,3,4)
        for comb in digit_combinations:
            formed_number = 0 
            position = 0
            for digit in comb:
                formed_number += (10 ** position) * digit
                position += 1
            
            if is_prime(formed_number):  # 소수 판별 함수 있다고 가정
                primes.add(formed_number)
    print(primes)
    len_p =len(primes)
    return len_p