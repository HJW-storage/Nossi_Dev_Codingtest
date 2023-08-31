# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

# from collections import deque

# def shortest_path_bfs(grid):
#     n = len(grid)

#     # 처음과 끝을 확인
#     if grid[0][0] == 1 or grid[n-1][n-1] == 1:
#         return -1
    
#     q = deque()
#     q.append((0, 0))
    
#     # 8방향 이동
#     dx = [0, 1, 1,  1,  0, -1, -1, -1] # 행 이동
#     dy = [1, 1, 0, -1, -1, -1,  0,  1] # 열 이동
    
#     grid[0][0] = 1 # 시작점도 카운트하므로 1을 대입. # 방문처리. 
#     final_flag = False
#     while q:
#         x, y = q.popleft()  # 현재 행과 열의 위치
#         # 현재 위치에서 8방향 확인
#         for i in range(8):
#             next_x, next_y = x + dx[i], y + dy[i]
            
#             # (x == n-1 and y == n-1) <- grid가 1x1 인 상황을 고려한 예외처리.
#             if (x == n-1 and y == n-1) or (next_x == n-1 and next_y == n-1): # 최종지점까지 왔는지 확인
#                 final_flag = True
                
#             # 인덱스를 벗어나는 경우는 지나간다.
#             if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
#                 continue
#             # 진행할 수 없는 길 무시한다.
#             if grid[next_x][next_y] == 1:
#                 continue
            
#             if grid[next_x][next_y] == 0:
#                 grid[next_x][next_y] = grid[x][y] + 1   # 지나간 거리의 카운트 수를 입력해서 방문처리 진행.
#                 q.append((next_x, next_y))

#     # 최종 지점까지 길이 연결되서 최종 지점으로 왔는지 확인. 
#     if final_flag == True:           
#         return grid[n-1][n-1]  # 가장 오른쪽 아래까지의 최단거리 반환. 
#     else:
#         return -1

# grid =[[0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
# # grid = [[1,0,0],[1,1,0],[1,1,0]]
# # grid =[[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]]
# # print(len(grid))
# print(shortest_path_bfs(grid))

from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    visited = [[False] * n for _ in range(n)]  # 방문 처리 리스트

    def bfs(r, c):
        visited[r][c] = True    # 방문처리
        
        q = deque()
        q.append((r, c, 1)) 

        # 8방향 이동
        dr = [0, 1, 1,  1,  0, -1, -1, -1] # 행 이동
        dc = [1, 1, 0, -1, -1, -1,  0,  1] # 열 이동
        
        short_distance = 0
        while q:
            cur_row, cur_col, cur_distance = q.popleft()
            
            if cur_row == n-1 and cur_col == n-1:
                short_distance = cur_distance
                break
            
            for i in range(8):
                next_row = cur_row + dr[i]
                next_col = cur_col + dc[i]
                # 1. 인덱스 범위 초과하지 않는지.
                # 2. 갈 수 있는 길인지
                # 3. 처음 방문하는 곳인지
                if 0 <= next_row < n and 0 <= next_col < n:
                    if grid[next_row][next_col] == 0:
                        if not visited[next_row][next_col]:
                            q.append((next_row, next_col, cur_distance + 1))
                            visited[next_row][next_col] = True # 방문처리
        
        return short_distance
    
    return bfs(0, 0)


print(shortestPathBinaryMatrix(grid))


