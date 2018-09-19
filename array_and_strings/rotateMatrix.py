# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Time O(n^2)
# Space O(1)
def rotateMatrix(matrix):
  n = len(matrix)
  for x in range (0, n / 2):
    for y in range(x, n - 1 - x):
      temp = matrix[y][n - 1 - x]

      matrix[y][n - 1 - x] = matrix[x][y]
      matrix[x][y] =  matrix[n - 1 - y][x]
      matrix[n - 1 - y][x] =  matrix[n - 1 - x][n - 1 - y]
      matrix[n - 1 - x][n - 1 - y] = temp
  return matrix

# Time O(n^2)
# Space O(n^2) creates a new 2d array
def rotateMatrix2(matrix):
  return [list(elem) for elem in zip(*matrix[::-1])]

if __name__ == "__main__":
  print(rotateMatrix([[1,2,3], [4,5,6], [7,8,9]]))
  print(rotateMatrix([[1, 2], [3, 4]]))
  print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
  print(rotateMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))     
  print(rotateMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))          
  print(rotateMatrix([]))
  print(rotateMatrix([[]]))
  print(rotateMatrix([[1]]))
  print(rotateMatrix2([[1,2,3], [4,5,6], [7,8,9]]))
  print(rotateMatrix2([[1, 2], [3, 4]]))
  print(rotateMatrix2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
  print(rotateMatrix2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))     
  print(rotateMatrix2([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]))          
  print(rotateMatrix2([]))
  print(rotateMatrix2([[]]))
  print(rotateMatrix2([[1]]))