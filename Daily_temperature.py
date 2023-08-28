"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
날씨에 대한 온도가 리스트로 주어져 있을 때, 출력은 현재 날씨보다 더 따뜻한 날씨가 되려면 몇일이 걸리는지이다.

Example 1:
    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]

Example 2:
    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]

Example 3:
    Input: temperatures = [30,60,90]
    Output: [1,1,0]
 
Constraints:
    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100
"""

# 스택을 이용해서 풀어본다.
def cnt_hign_temperature(temp_list):
    n = len(temp_list)
    result = [0] * n # 출력 결과 저장 1차원 리스트 초기화. 
    cnt = 0
    
    # 시간복잡도 O(n)
    for i, _ in enumerate(temp_list):
        yesterday = []
        if i == 0:  # 인덱스 
            today_temp = temp_list.pop()
            result[n - i] = 0    # 문제 조건에서 가장 마지막 출력은 0으로 명시
        else:
            yesterday_temp = today_temp # 기존 온도는 어제의 온도로 저장.
            yesterday.append(yesterday_temp) 
            today_temp = temp_list.pop()  # 오늘의 온도 업데이트
            if today_temp < yesterday_temp:
                result[n - i] = 1
                cnt = 0
            else:
                # ...... 
                for j in yesterday[-len(yesterday):]:
                    cnt += 1
                    if today_temp < j:
                        result.append(cnt)

# def daily_temperatures(temperatures):
#     ans = [0] * len(temperatures)
#     stack = []
#     for day, temp in enumerate(temperatures):
#         while stack and stack[-1][1] < temp:    # stack and : 스택이 비어있지 않은 경우에. 
#             prev_day = stack.pop()[0]       # day 날짜 정보 추출 
#             ans[prev_day] = day - prev_day
#         stack.append((day, temp))
#     return ans