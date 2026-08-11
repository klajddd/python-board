# time O(n)
# space O(n) where n is the total number of elements in the 2D array
def spiralTraverse(array):
    # Write your code here.
    result = []

    startRow, endRow = 0, len(array) - 1  # 1, 1
    startCol, endCol = 0, len(array[0]) - 1  # 1, 2

    while startRow <= endRow and startCol <= endCol:

        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        for col in range(endCol - 1, startCol - 1, -1):
            if startRow == endRow:  # handle case with single row in the middle of the matrix, prevents double appending the row
                break
            result.append(array[endRow][col])

        for row in range(endRow - 1, startRow, -1):
            if startCol == endCol:  # handle case with single column in the middle of the matrix, prevents double appending the column
                break
            result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result



'''
input
{
  "array": [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]
  
output  
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

}

'''