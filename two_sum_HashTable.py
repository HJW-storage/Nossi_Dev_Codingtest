"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
 
Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
"""

def two_sum_HashTable(nums_list, target):
    memo = dict() # 해쉬 테이블 이용. dict 선언. memo = {} 동일   
    result = False # 결과 저장 변수 선언
    
    # 메모리 저장
    for idx, data in enumerate(nums_list):
        memo[data] = True  # 딕셔너리의 키(key) 저장이 핵심. 값(value)는 임의로 True로 저장한다. 
    # print(memo)
    
    # 딕셔너리를 for 문을 돌리면 딕셔너리의 키(key) 값이 할당. 
    for key in nums_list:
        search_key = target - key
        if search_key in memo:  # 해시 테이블에서 key 값 조사. 
            result = True   # 문제 조건 달성. return 으로 종료. 
            return result    
        
    return result  
                
        
# 정수형 배열 입력 받기
nums = list(map(int, input().split()))

# 타겟 입력 받기
target = int(input())

# 결과 출력
result = two_sum_HashTable(nums, target)
print("결과는 : {}".format(result))
