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

####### 내가 처음으로 구성한 코드는 최악의 경우에 Time Out이 발생하였다. #########
def Search_Sequence1(nums):
    cnt = 1     # 연속되는 수를 저장할 변수
    cnt_max = 0     # 연속되는 최대수 저장할 변수
    
    memo = dict()   # 딕셔너리 선언
    for k in nums:
        memo[k] = True  # 딕셔너리의 키(key) 저장이 핵심. 값(value)는 임의로 True로 저장한다. 
    
    for n in nums:
        while (n+cnt) in memo:  # 해쉬테이블 이용해서 연속된 수 조사.   ## 해당 while 문에서 시간 초과 발생한 것. 
            cnt += 1
        if cnt_max < cnt:   # 현재 조사한 값이 더 긴 연속된 수이면 cnt_max 값 변경. 
            cnt_max = cnt
        cnt = 1 # 초기화 
    return cnt_max
####### 내가 처음으로 구성한 코드는 최악의 경우에 Time Out이 발생하였다. #########

########################### 수정보완한 코드 ################################### 
def Search_Sequence2(nums):
    cnt = 1     # 연속되는 수를 저장할 변수
    cnt_max = 0     # 연속되는 최대수 저장할 변수
    
    memo = dict()   # 딕셔너리 선언
    for k in nums:
        memo[k] = True  # 딕셔너리의 키(key) 저장이 핵심. 값(value)는 임의로 True로 저장한다. 
    
    for n in nums:
        # n-1 : 조사할 데이터의 이전 값이 있다면 조사하지 않고 넘어간다. 시간 줄이는 방법. 
        #       조사할 데이터의 이전 값이 없는 경우가 연속된 수를 조사하기 시작할 첫번쨰 시작 수. 
        if n-1 not in memo: 
            while (n+cnt) in memo:  # 해쉬테이블 이용해서 연속된 수 조사. 
                cnt += 1
            if cnt_max < cnt:   # 현재 조사한 값이 더 긴 연속된 수이면 cnt_max 값 변경. 
                cnt_max = cnt
            cnt = 1 # 초기화 
    return cnt_max
########################### 수정보완한 코드 ###################################

# 정수형 배열 입력 받기
nums = list(map(int, input().split()))

# 결과 출력
result = Search_Sequence2(nums)
print("결과는 : {}".format(result))

