import random
import numpy as np

def is_valid(board, row, col, num):
    """Kiểm tra xem số 'num' có thể đặt vào ô (row, col) không"""
    if num in board[row]:  # Kiểm tra hàng
        return False
    if num in board[:, col]:  # Kiểm tra cột
        return False
    
    box_x, box_y = (row // 3) * 3, (col // 3) * 3
    if num in board[box_x:box_x+3, box_y:box_y+3]:  # Kiểm tra ô 3x3
        return False
    
    return True

def solve(board):
    """Giải Sudoku bằng đệ quy (backtracking)"""
    empty = np.where(board == 0)
    if len(empty[0]) == 0:
        return True  # Đã giải xong
    
    row, col = empty[0][0], empty[1][0]
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row, col] = num
            if solve(board):
                return True
            board[row, col] = 0  # Quay lui
    
    return False

def generate_sudoku():
    """Tạo bảng Sudoku hoàn chỉnh và xoá một số ô"""
    board = np.zeros((9, 9), dtype=int)
    for i in range(9):
        num = random.randint(1, 9)
        while not is_valid(board, i, i, num):
            num = random.randint(1, 9)
        board[i, i] = num
    
    solve(board)  # Điền bảng hoàn chỉnh
    
    # Xoá một số ô để tạo câu đố
    for _ in range(40):
        x, y = random.randint(0, 8), random.randint(0, 8)
        board[x, y] = 0
    
    return board

def print_board(board):
    """Hiển thị bảng Sudoku"""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i, j] if board[i, j] != 0 else "_", end=" ")
        print()

def play_game():
    """Chạy trò chơi Sudoku trên console"""
    board = generate_sudoku()
    solution = board.copy()
    solve(solution)  # Lưu lời giải đúng
    
    while True:
        print_board(board)
        try:
            row, col, num = map(int, input("Nhập (hàng, cột, số) [0-8 0-8 1-9] hoặc -1 để thoát: ").split())
            if row == -1:
                break
            if board[row, col] != 0:
                print("Ô này đã có số! Hãy chọn ô khác.")
                continue
            if num == solution[row, col]:
                board[row, col] = num
            else:
                print("Sai rồi! Hãy thử lại.")
            
            if np.array_equal(board, solution):
                print("Chúc mừng! Bạn đã giải xong Sudoku.")
                break
        except ValueError:
            print("Lỗi nhập liệu! Hãy nhập đúng định dạng.")

if __name__ == "__main__":
    play_game()
