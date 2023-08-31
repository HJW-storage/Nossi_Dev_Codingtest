# https://leetcode.com/problems/climbing-stairs/

memo = dict()   # 메모리 생성

def climb_stair(n):
    # memo = dict()   # 메모리 생성  # 내부에 선언하면 재귀함수가 실행될때마다 초기화 되므로 바깥쪽 전역에서 선언한다.
    
    # base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n not in memo:
        memo[n] = climb_stair(n - 1) + climb_stair(n-2)
    
    return memo[n]


print(climb_stair(38))