# Define rows and columns
ROWS = 6
COLUMNS = 7

# Create a board
def create_board():
  board = []
  for row in range(ROWS):
    board.append([None] * COLUMNS)
  return board

# Print the board
def print_board(board):
  for row in board:
    for cell in row:
      print(cell or " ", end=" ")  # Print empty cell as space
    print()

# Check if a column is valid
def is_valid_location(board, col):
  return board[0][col] == None  # Check if top row is empty

# Get the next open row in a column
def get_next_open_row(board, col):
  for row in range(ROWS - 1, -1, -1):
    if board[row][col] == None:
      return row
  return None  # Column full

# Drop a piece
def drop_piece(board, col, marker):
  row = get_next_open_row(board, col)
  if row != None:
    board[row][col] = marker

# Check for a winner
def winning_move(board, marker):
  # Check horizontal
  for row in board:
    for col in range(COLUMNS - 3):
      if row[col] == marker and row[col + 1] == marker and row[col + 2] == marker and row[col + 3] == marker:
        return True
  # Check vertical
  for col in range(COLUMNS):
    for row in range(ROWS - 3):
      if board[row][col] == marker and board[row + 1][col] == marker and board[row + 2][col] == marker and board[row + 3][col] == marker:
        return True
  # Check diagonals
  for col in range(COLUMNS - 3):
    for row in range(ROWS - 3):
      if board[row][col] == marker and board[row + 1][col + 1] == marker and board[row + 2][col + 2] == marker and board[row + 3][col + 3] == marker:
        return True
      if board[row + 3][col] == marker and board[row + 2][col + 1] == marker and board[row + 1][col + 2] == marker and board[row][col + 3] == marker:
        return True
  return False

# Main game loop
def main():
  board = create_board()
  game_over = False
  current_marker = "X"  # Start with player X

  while not game_over:
    print_board(board)
    # Get player input
    col = int(input(f"Player {current_marker}, choose a column (1-7): ")) - 1

    # Check for valid input
    while not is_valid_location(board, col):
      print("Column is full. Try again.")
      col = int(input(f"Player {current_marker}, choose a column (1-7): ")) - 1

    # Drop the piece
    drop_piece(board, col, current_marker)

    # Check for winner
    if winning_move(board, current_marker):
      print_board(board)
      print(f"Player {current_marker} wins!")
      game_over = True

    # Switch turns
    current_marker = "O" if current_marker == "X" else "X"

if __name__ == "__main__":
  main()
