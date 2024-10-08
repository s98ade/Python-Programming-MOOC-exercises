# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    seen = set()
    for num in row:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True

def column_correct(sudoku: list, column_no: int) -> bool:
    column = [row[column_no] for row in sudoku]
    seen = set()
    for num in column:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    block = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            block.append(sudoku[i][j])

    seen = set()
    for num in block:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True

def sudoku_grid_correct(sudoku: list) -> bool:
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(sudoku, i, j):
                return False
    
    return True