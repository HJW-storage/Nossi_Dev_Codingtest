"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: True
    
Example 2:
    Input: nums = [3,2,4], target = 6
    Output: True

Example 3:
    Input: nums = [3,3], target = 7
    Output: False
    
Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
"""

# 완전탐색은 시간이 부족할 수 있다. 시간을 줄이는 방법을 생각해본다. 
def two_sum_idx(nums_list, target):
    # 오름차순으로 정렬한다. 시간복잡도 O(nlogn)
    nums_list.sort()
    
    # 시작과 끝 인덱스를 선언.
    start_idx = 0
    end_idx = len(nums_list) - 1
    
    result_flag = False
    for _ in range(len(nums_list)):
        # target 과 비교해서 시작과 끝 인덱스를 변화시키며 검사한다.
        if nums_list[start_idx] + nums_list[end_idx] > target:
            end_idx -= 1
        elif nums_list[start_idx] + nums_list[end_idx] < target:
            start_idx += 1
        else:
            result_flag = True
        
        # 시작과 끝 인덱스가 같아지면 target을 만들지 못 한 경우이다.
        if end_idx <= start_idx:
            result_flag = False
        
    return result_flag

# 숫자 배열 입력 받기
nums_list = list(map(int, input().split()))
# print(len(nums))

# target 입력 받기
target = int(input())
# print(target)

result = two_sum_idx(nums_list, target)
print(result)
