"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""

# stack 이용
def decision_valid(list_s, cnt1_left, cnt1_right, cnt2_left, cnt2_right, cnt3_left, cnt3_right):
    n = len(list_s) # 문자열 길이
    # print("문자열 길이 : {}".format(n))
    
    # 시간복잡도 O(n) / 문자열 리스트를 한번 훎으며 조사한다. 
    for _ in range(n):
        pop_s = list_s.pop()    # 스택에서 문자 꺼내기
        
        # 소괄호( ), 중괄호{ }, 대괄호[ ] 개수를 세기 위한 cnt
        if pop_s == '(': 
            cnt1_left += 1
        elif pop_s == ')': 
            cnt1_right += 1
        elif pop_s == '{': 
            cnt2_left += 1
        elif pop_s == '}': 
            cnt2_right += 1    
        elif pop_s == '[':
            cnt3_left += 1
        elif pop_s == ']':
            cnt3_right += 1    
            
        # 꺼낸 문자를 비교했을 때, 닫히는 괄호보다 (, {, [ 열리는 괄호가 먼저 나온 경우 바로 False 반환
        if (cnt1_left > cnt1_right) or (cnt2_left > cnt2_right) or (cnt3_left > cnt3_right) :
            print("문자열 조사중에 규칙을 어겼기에 이후 검사 없이 바로 종료합니다.")
            return False
        
    # 입력 받은 문자열의 괄호 개수를 조사한다. 열림, 닫힘 괄호의 개수가 동일하면 True, 다르면 False
    if cnt1_left == cnt1_right and cnt2_left == cnt2_right and cnt3_left == cnt3_right :
        return True
    else:
        return False
        


cnt1_left, cnt1_right, cnt2_left, cnt2_right, cnt3_left, cnt3_right = 0, 0, 0, 0, 0, 0  # 소괄호( ), 중괄호{ }, 대괄호[ ] 개수를 세기 위한 cnt 초기화 

# 문자열 입력 받기
s = list(input())
# print(s)
result = decision_valid(s, cnt1_left, cnt1_right, cnt2_left, cnt2_right, cnt3_left, cnt3_right)
print("valid_Parentheses 결과는 : {}".format(result))
