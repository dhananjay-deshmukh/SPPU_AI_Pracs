def solveNQueens(n: int) -> list[list[str]]:
    col = set()
    forwardDiag = set()  # -ve diagonal
    backwardDiag = set()  # +ve diagonal

    result = []
    board = [['.'] * n for i in range(n)]

    def backtracking(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for c in range(n):
            if c in col or (r - c) in forwardDiag or (r + c) in backwardDiag:
                continue

            col.add(c)
            backwardDiag.add(r + c)
            forwardDiag.add(r - c)
            board[r][c] = "Q"

            backtracking(r + 1)

            col.remove(c)
            backwardDiag.remove(r + c)
            forwardDiag.remove(r - c)
            board[r][c] = "."

    backtracking(0)
    return result

def main():
    n = int(input("Enter the value of n: "))

    solutions = solveNQueens(n)
    print("All solutions:")
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

if __name__ == '__main__':
    main()
