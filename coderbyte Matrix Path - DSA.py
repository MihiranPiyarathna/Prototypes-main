"""
mediumDiscussion Solutions 
Matrix Path

Have the function MatrixPath(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's of some arbitrary size, and determine if a path of 1's exists from the top-left of the matrix to the bottom-right of the matrix while moving only in the directions: up, down, left, and right. If a path exists your program should return the string true, otherwise your program should return the number of locations in the matrix where if a single 0 is replaced with a 1, a path of 1's will be created successfully. If a path does not exist and you cannot create a path by changing a single location in the matrix from a 0 to a 1, then your program should return the string not possible. For example: if strArr is ["11100", "10011", "10101", "10011"] then this looks like the following matrix:

1 1 1 0 0
1 0 0 1 1
1 0 1 0 1
1 0 0 1 1

For the input above, a path of 1's from the top-left to the bottom-right does not exist. But, we can change a 0 to a 1 in 2 places in the matrix, namely at locations: [0,3] or [1,2]. So for this input your program should return 2. The top-left and bottom-right of the input matrix will always be 1's.
Examples
Input: ["10000", "11011", "10101", "11001"]
Output: 1
Input: ["1000001", "1001111", "1010101"]
Output: not possible
Tags
matrixsearchingGoogleMicrosoft
"""
# strArr =  ["11100", 
#            "10011", 
#            "10101", 
#            "10011"] # 2
"""
[['L', 'L', 'L', '0', '0'], 
['L', '0', '0', 'R', 'R'], 
['L', '0', '1', '0', 'R'], 
['L', '0', '0', 'R', 'R']]
"""

# strArr =  ["10000", "11011", "10101", "11001"] # 1
# strArr =  ["1000001", "1001111", "1010101"] # not possible
# strArr = ["100", 
#           "100", 
#           "111"] # true
strArr = ["1110", 
          "1010", 
          "1001", 
          "0111"] # 4 #### my solution return 5


def MatrixPath_my(strArr):
    success = 0
    for i in range(len(strArr)):
        strArr[i] = list(strArr[i])
    
    # dfs
    def dfs(row, col, path):
        nonlocal success
        # paths = d4L, d4R knight
        tgt = '1' if 'd4' in path else 'R'
        if 'd4' in path:
            delta_r = [-1, 0, 1, 0]
            delta_c = [0, 1, 0, -1]
        else:
            delta_r = [-1, 1, 1, -1, -1, -1, 1, 1 ,-2, 0, 2, 0]
            delta_c = [1, 1, -1, -1, -1, 1, 1, -1 , 0, 2, 0, -2]
        
        if path == 'd4L':
            strArr[row][col] = 'L'
            if row == len(strArr)-1 and col== len(strArr[0])-1:
                success += 1
                # return True
        elif path == 'd4R':
            strArr[row][col] = 'R'

        for i in range(len(delta_r)):
            nrow = row + delta_r[i] 
            ncol = col + delta_c[i]
            if 0<= nrow< len(strArr) and 0<= ncol< len(strArr[0]) and strArr[nrow][ncol]==tgt:
                if 'd4' in path: 
                    # return dfs(nrow, ncol, path)
                    dfs(nrow, ncol, path)
                else: 
                    success += 1

    # if dfs(0,0, 'd4L'): return True
    dfs(0,0, 'd4L')
    if success>0 : return True
    dfs(len(strArr)-1, len(strArr[0])-1, 'd4R')
    for r in range(len(strArr)):
        for c in range(len(strArr[0])):
            if strArr[r][c] == 'L': dfs(r,c,'knight')
    return success if success>0 else 'not possible'

print(MatrixPath_my(strArr))

##########
  # code goes here
def MatrixPath_websolution(strArr):
  import numpy as np
  def path_check(b):
    stack = [(0,0)]
    while stack:
      i, j = stack.pop()
      if b[i][j] == '1':
        if i == len(b)-1 and j == len(b[0])-1:
          return True
        b[i][j] = '0'
        for (di,dj) in [(0,1), (0,-1), (1, 0), (-1, 0)]:
          if i + di >= 0 and i + di < len(b) and j + dj >=0 and j + dj < len(b[0]):
            stack.append((i+di, j+dj))
    return False

  arr = [[c for c in row] for row in strArr]
  b = np.copy(arr)
  if path_check(b) == True:
    return "true"

  res = 0
  for i in range(len(strArr)):
    for j in range(len(strArr[0])):
      b = np.copy(arr)
      if arr[i][j] == '0':
        b[i][j] = '1'
        if path_check(b) == True:
          res += 1

  return "not possible" if res == 0 else res

print(MatrixPath_websolution(strArr))
