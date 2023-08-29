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

# 완전탐색은 시간이 부족할 수 있다. 시간을 줄이는 방법을 생각해본다. 
def two_sum_idx(nums_list, target):
    # 문제에서 인덱스를 출력으로 원한다. 
    # 기존 인덱스 정보를 유지하면서 데이터 기준으로 오름차순 정렬이 필요하다. 
    nums_list = [[i, n] for i, n in enumerate(nums_list)] # nums_list = [[idx, data], [idx, data], ...] 형태로 저장.
    nums_list.sort(key=lambda x: x[1])  # 람다식 정렬 기준 설정. 
    left_idx, right_idx = 0, len(nums_list) - 1 # 왼쪽 시작, 오른쪽 끝 인덱스 초기화 
    result_idx = []
    
    for _ in range(len(nums_list)):
        if nums_list[left_idx][1] + nums_list[right_idx][1] > target:
            right_idx -= 1
        elif nums_list[left_idx][1] + nums_list[right_idx][1] < target:
            left_idx += 1
        elif nums_list[left_idx][1] + nums_list[right_idx][1] == target:
            result_idx = [nums_list[left_idx][0], nums_list[right_idx][0]]
        if right_idx <= left_idx:
            result_idx = None   # 원소 합 조합으로 target이 없는 경우는 반환값 없음. 
    
    return result_idx    
        
# 숫자 배열 입력 받기
nums_list = list(map(int, input().split()))
# print(len(nums_list))

# target 입력 받기
target = int(input())
# print(target)

result = two_sum_idx(nums_list, target)
print(result)

############################ 모범 답안 ##############################################################
# def two_sum_idx(nums_list, target):
#     # 문제에서 인덱스를 출력으로 원한다. 
#     # 기존 인덱스 정보를 유지하면서 데이터 기준으로 오름차순 정렬이 필요하다. 
#     nums_list = [[n, i] for i, n in enumerate(nums_list)] # 결과적으로 nums_list = [[data, idx], [data, idx], ...] 형태로 저장.
#     nums_list.sort(key=lambda x: x[0])  # 람다식 정렬 기준 설정. 
#     l, r = 0, len(nums_list) - 1

#     while l < r:
#         num_sum = nums_list[l][0] + nums_list[r][0] # 데이터 + 데이터
#         if num_sum == target:
#             return [nums_list[l][1], nums_list[r][1]]   # 인덱스 반환
#         elif num_sum > target:
#             r -= 1
#         else:
#             l += 1
            
# # 숫자 배열 입력
# nums_list = list(map(int, input().split()))
# # print(len(nums_list))
# target = int(input())
# # print(target)
# result = two_sum_idx(nums_list, target)
# print(result)
# ############################ 모범 답안 ##############################################################