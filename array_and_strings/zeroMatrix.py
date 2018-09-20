# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

# Time O(M * N)
# Space O(M + N)
def zeroMatrix(matrix):
  rowLength = len(matrix)
  colLength = len(matrix[0])
  rowMatrix = [0] * rowLength #initialize array of rows with 0s
  colMatrix = [0] * colLength #initialize array of cols with 0s

  for i in range(0, rowLength):
    for j in range(0, colLength):
      if matrix[i][j] == 0:
        rowMatrix[i] = 1
        colMatrix[j] = 1

  for i in range(0, rowLength):
    if rowMatrix[i] == 1:
      matrix[i] = [0] * colLength

  for j in range(0, colLength):
    if colMatrix[j] == 1:
       for i in range (0, rowLength):
        matrix[i][j] = 0
  return matrix

# Time O(M * N)
# Space O(1)
def zeroMatrixInPlace(matrix):
  rowLength = len(matrix)
  colLength = len(matrix[0])

  firstRowFlag = False 
  firstColFlag = False 

  for j in range(0, colLength): #checks if first row needs to become 0
    if matrix[0][j] == 0:
      firstRowFlag = True
      break
  for i in range(0, rowLength): #checks if first col needs to become 0
    if matrix[i][0] == 0:
      firstColFlag = True
      break
  
  for i in range(1, rowLength): #goes through all elems and sets 0 to first row/col if elem is 0
    for j in range(1, colLength):
      if matrix[i][j] == 0:
        matrix[i][0] = 0
        matrix[0][j] = 0

  for i in range(1, rowLength): # set row to 0
    if matrix[i][0] == 0:
      for j in range(1, colLength):
        matrix[i][j] = 0
  
  for j in range(1, colLength): # set col to 0
    if matrix[0][j] == 0:
      for i in range(1, rowLength):
        matrix[i][j] = 0
  
  if firstRowFlag: # set row to 0 if first row has 0
    matrix[0] = [0] * colLength
  if firstColFlag: # set col to 0 if first row has 0
    for i in range(0, rowLength):
      matrix[i][0] = 0
  return matrix

if __name__ == "__main__":
  print(zeroMatrix([[1,2,3],[4,5,0],[7,8,9],[0,11,12]]))
  print(zeroMatrix([[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]))
  print(zeroMatrixInPlace([[1,2,3],[4,5,0],[7,8,9],[0,11,12]]))
  print(zeroMatrixInPlace([[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]))