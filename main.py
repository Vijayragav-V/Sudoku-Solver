import tkinter as tk

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
	row, col = find_next_empty(puzzle)

	if row == None:
		return True 

	for guess in range(1,10):
		if is_valid(puzzle,guess,row,col):
			puzzle[row][col] = guess

			if solve_sudoku(puzzle):
				return True

		puzzle[row][col] = -1

	return False

def create_grid(root, rows, columns):
    entries = []
    for i in range(rows):
        row_entries = []
        for j in range(columns):
            entry = tk.Entry(root, width=4, font=('Arial', 14))
            entry.grid(row=i, column=j, padx=1, pady=1)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries

def get_values(entries):
    values = []
    for row in entries:
        row_values = []
        for entry in row:
            value = entry.get()
            if not value:
                value = "-1"
            row_values.append(int(value))
        values.append(row_values)
    return values

def solve():
    input_values = get_values(entries)
    if solve_sudoku(input_values):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(input_values[i][j]))
    else:
        print("No solution exists.")

def test():
    input_values = get_values(entries)
    solve_sudoku(input_values)
    print(input_values)


def print_board():
    input_values = get_values(entries)
    print(input_values)

def clear_board():
     for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)

def move_focus(event):
    widget = event.widget
    row, col = int(widget.grid_info()["row"]), int(widget.grid_info()["column"])
    if event.keysym == "Right" and col < 8:
        entries[row][col + 1].focus_set()
    elif event.keysym == "Left" and col > 0:
        entries[row][col - 1].focus_set()
    elif event.keysym == "Down" and row < 8:
        entries[row + 1][col].focus_set()
    elif event.keysym == "Up" and row > 0:
        entries[row - 1][col].focus_set()

root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("453x330")

root.resizable(False, False)

entries = create_grid(root, 9, 9)

solve_button = tk.Button(root, text="Solve Sudoku", command=solve)
solve_button.grid(row=9, columnspan=20, pady=10)

clear_button = tk.Button(root, text="Clear Board", command=clear_board)
clear_button.grid(row=9, columnspan=5, pady=10)

for i in range(9):
    for j in range(9):
        entries[i][j].bind("<Right>", move_focus)
        entries[i][j].bind("<Left>", move_focus)
        entries[i][j].bind("<Down>", move_focus)
        entries[i][j].bind("<Up>", move_focus)

root.mainloop()
