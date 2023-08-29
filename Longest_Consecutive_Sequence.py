"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""

# 시간복잡도 O(n)으로 풀어보기 
def Search_Sequence(nums):
    cnt = 1     # 연속되는 수를 저장할 변수
    cnt_max = 0     # 연속되는 최대수 저장할 변수
    
    memo = dict()   # 딕셔너리 선언
    for k in nums:
        memo[k] = True  # 딕셔너리의 키(key) 저장이 핵심. 값(value)는 임의로 True로 저장한다. 
    
    for n in nums:
        while (n+cnt) in memo:  # 해쉬테이블 이용해서 연속된 수 조사. 
            cnt += 1
        if cnt_max < cnt:   # 현재 조사한 값이 더 긴 연속된 수이면 cnt_max 값 변경. 
            cnt_max = cnt
        cnt = 1 # 초기화 
    return cnt_max

# 정수형 배열 입력 받기
nums = list(map(int, input().split()))

# 결과 출력
result = Search_Sequence(nums)
print("결과는 : {}".format(result))

