# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = [row[:] for row in sudoku]
    grid_copy[row_no][column_no] = number
    return grid_copy
