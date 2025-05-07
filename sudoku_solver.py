
def isSafe (i, j, num, row, col, box):
    return not ((row[i] & 1<<num) or (col[j] & 1<<num) or (box[i//3 *3 + j//3] & 1<<num))

def sudokuSolverRec(grid, i, j, row, col, box):
    n = len(grid)

    if i==n-1 and j==n:
        global ans
        ans += int("".join(map(str, grid[0][:3])))
        return True
    
    if j==n:
        i+=1
        j = 0

    if grid[i][j] != 0:
        return sudokuSolverRec(grid, i, j+1, row, col, box)

    for num in range(1, n+1):
        if isSafe(i, j, num, row, col, box):
            grid[i][j] = num
            row[i]|= (1<<num)
            col[j]|= (1<<num)
            box[i//3 * 3 + j//3]|= (1<<num)

            if sudokuSolverRec(grid, i, j, row, col, box):
                return True
            
            grid[i][j] = 0
            row[i] &= ~(1<<num)
            col[j] &= ~(1<<num)
            box[i//3 * 3 + j//3] &= ~(1<<num)
    return False

def solveSudoku(grids):
    for grid in grids:
        n = len(grid)
        row = [0]*n
        col = [0]*n
        box = [0]*n

        for i in range(n):
            for j in range(n):
                if grid[i][j]!=0:
                    row[i] |= (1<<grid[i][j])
                    col[j] |= (1<<grid[i][j])
                    box[int(i//3 * 3 + j//3)] |= (1<<grid[i][j])
        
        sudokuSolverRec(grid, 0, 0, row, col, box)



