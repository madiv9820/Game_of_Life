## 🧮 Approach 1: The Standard Simulation (Extra Space)

### 🧠 Intuition
The biggest trap in the Game of Life is that the universe ticks forward **simultaneously**. 

If you loop through the grid and update a cell's state from Alive to Dead immediately, the *next* cell you visit will look at that neighbor and get the wrong count! It will see a Dead cell when it was supposed to see an Alive cell for that generation.

The simplest, most foolproof way to solve this is the **Blank Canvas Method**. Instead of trying to update the board while we are actively reading it, we create a brand new, empty board of the exact same size. We read the rules from the original board, draw the results onto the new board, and then replace the old board when we are done.

### 🚶‍♂️ Step-by-Step Logic
1. **Set Up the Canvas:** Create a `next_generation` matrix of the same dimensions (`m x n`) as the original board, completely filled with `0`s (Dead cells).
2. **Define Directions:** Set up an array of 8 coordinate pairs representing the 8 directions to check around any given cell (Up, Down, Left, Right, and the 4 diagonals).
3. **Loop the Grid:** Iterate through every single row `i` and column `j` in the original board.
4. **Count Neighbors:** For the current cell `(i, j)`, loop through the 8 directions. If a neighboring cell is within the grid boundaries and is currently alive (`1`), increment our `alive_neighbors` counter.
5. **Apply the Rules of Life:**
   * **Survival:** If the current cell is Alive (`1`) and has `2` or `3` alive neighbors, it survives. Set `next_generation[i][j] = 1`.
   * **Reproduction:** If the current cell is Dead (`0`) and has exactly `3` alive neighbors, it is born. Set `next_generation[i][j] = 1`.
   * *(Note: Because our canvas is already filled with `0`s, Underpopulation and Overpopulation take care of themselves—we just leave those cells alone!)*
6. **Overwrite the Board:** Once the entire original board has been processed, loop through it one last time and overwrite every cell with the values we calculated in `next_generation`.

### 💻 Pseudocode

```text
function gameOfLife(board):
    m = length(board)
    n = length(board[0])
    
    // 1. Create a blank canvas
    next_gen = matrix of size m x n filled with 0s
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    // 2. Read the present, draw the future
    for i from 0 to m - 1:
        for j from 0 to n - 1:
            alive_neighbors = 0
            
            // Count living neighbors
            for (dr, dc) in directions:
                r = i + dr
                c = j + dc
                if (r, c) is inside bounds AND board[r][c] == 1:
                    alive_neighbors = alive_neighbors + 1
                    
            // Apply rules
            if board[i][j] == 1:
                if alive_neighbors == 2 or alive_neighbors == 3:
                    next_gen[i][j] = 1
            else:
                if alive_neighbors == 3:
                    next_gen[i][j] = 1
                    
    // 3. Update the original board
    for i from 0 to m - 1:
        for j from 0 to n - 1:
            board[i][j] = next_gen[i][j]
```

### 📊 Complexity Analysis
* **Time Complexity:** `O(m * n)`
    * We iterate through every cell in the `m x n` grid. For each cell, we perform exactly 8 constant-time boundary and neighbor checks. Finally, we iterate through the grid one more time to overwrite it. Since the 8 checks are a constant, it simplifies to strictly `O(m * n)`.

* **Space Complexity:** `O(m * n)`
    * We allocate a completely new 2D array (`next_gen`) of the exact same size as the input board to store the intermediate states. This is safe and readable, but not strictly optimal for massive grids!
---
