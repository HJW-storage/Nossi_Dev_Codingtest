# https://leetcode.com/problems/number-of-islands/

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def number_island_dfs(grid):
    row_len, col_len = len(grid), len(grid[0]) # 행, 열의 길이
    visited = [[False] * col_len for _ in range(row_len)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    def dfs(r, c):
        visited[r][c] = True
        
        for i in range(4):
            next_row, next_col = r + dr[i], c + dc[i]
            if 0 <= next_row < row_len and 0 <= next_col < col_len:     # 인덱스 범위 검사
                if grid[next_row][next_col] == "1":     # 갈 수 있는 길인지 검사
                    if not visited[next_row][next_col]:     # 방문 검사           
                        dfs(next_row, next_col)

    island_cnt = 0
    for i in range(row_len):
        for j in range(col_len):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j)
                island_cnt += 1
                
    return island_cnt


# BFS로 구현해보기 
# from collections import deque

# def number_island_bfs(grid):
#     row_len, col_len = len(grid), len(grid[0]) # 행, 열의 길이
#     visited = [[False] * col_len for _ in range(row_len)]
    
#     def bfs(r, c):
#         visited[r][c] = True    # 방문처리
#         q = deque()
#         q.append((r, c))
        
#         dr = [0, 1, 0, -1]
#         dc = [1, 0, -1, 0]

#         while q:
#             cur_row, cur_col = q.popleft()  # 현재 위치
#             for i in range(4):
#                 next_row, next_col = cur_row + dr[i], cur_col + dc[i]
#                 if 0 <= next_row < row_len and 0 <= next_col < col_len:     # 인덱스가 범위안에 있는지 
#                     if grid[next_row][next_col] == "1":     # 갈 수 있는 길인지
#                         if not visited[next_row][next_col]:     # 방문 검사
#                             q.append((next_row, next_col))
#                             visited[next_row][next_col] = True  # 방문처리
    
#     island_cnt = 0
#     for i in range(row_len):
#         for j in range(col_len):
#             if grid[i][j] == "1" and not visited[i][j]:
#                 bfs(i, j)
#                 island_cnt += 1
                
#     return island_cnt

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

print(number_island_bfs(grid))

