## 🧠 Approach 2: In-Place State Mapping

### 💡 Intuition
The core challenge of calculating the Game of Life in-place is that generations must happen **simultaneously**. If you immediately change a cell from Alive to Dead, the neighboring cells will read the wrong data when it is their turn to calculate. 

To solve this without using extra memory (`O(m*n)` space), we can use a **State Mapping trick**. 

Since the grid currently only uses `0` (Dead) and `1` (Alive), we have plenty of room in the integers to store *temporary* states. By using `2` and `3`, we can encode both a cell's **Present** state and its **Future** state simultaneously!

#### The State Map:
* **`0`**: Dead 💀 *(Stays Dead)*
* **`1`**: Alive 🟢 *(Stays Alive)*
* **`2`**: Dead $\rightarrow$ Alive 🧟‍♂️ *(Reproduction)*
* **`3`**: Alive $\rightarrow$ Dead 👻 *(Under/Overpopulation)*

Because `1` and `3` both represent cells that are *currently* alive in this generation, neighbors can just look for `1`s and `3`s to get an accurate count, completely ignoring what will happen in the future!

### 🚶‍♂️ Step-by-Step Logic
This algorithm requires two passes over the board:

#### Pass 1: Time Travel (Set Temporary States)
1. Loop through every cell `(i, j)` on the board.
2. Count the living neighbors by checking all 8 directions. 
   * *Crucial Difference:* A neighbor is considered "Alive" if its value is `1` **OR** `3`.
3. Apply the rules:
   * If the cell is Alive (`1`) and should die (neighbors < 2 or > 3), change it to **`3`**.
   * If the cell is Dead (`0`) and should live (neighbors == 3), change it to **`2`**.

#### Pass 2: Finalize the Future
1. Loop through the board one more time.
2. Convert all the temporary future states into their final reality:
   * If the cell is **`2`**, change it to **`1`** (It is now Alive).
   * If the cell is **`3`**, change it to **`0`** (It is now Dead).

### 💻 Pseudocode
```text
function gameOfLife(board):
    m = length(board)
    n = length(board[0])
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    // --- PASS 1: Apply rules and set dummy states ---
    for i from 0 to m - 1:
        for j from 0 to n - 1:
            alive_neighbors = 0
            
            // Count neighbors (treating 1 and 3 as alive)
            for (dr, dc) in directions:
                r = i + dr
                c = j + dc
                if (r, c) is inside bounds:
                    if board[r][c] == 1 or board[r][c] == 3:
                        alive_neighbors = alive_neighbors + 1
                        
            // Apply rules using dummy states
            if board[i][j] == 1:
                if alive_neighbors < 2 or alive_neighbors > 3:
                    board[i][j] = 3   // Mark as Alive -> Dead
            else:
                if alive_neighbors == 3:
                    board[i][j] = 2   // Mark as Dead -> Alive
                    
    // --- PASS 2: Finalize states ---
    for i from 0 to m - 1:
        for j from 0 to n - 1:
            if board[i][j] == 2:
                board[i][j] = 1       // Finally Alive
            else if board[i][j] == 3:
                board[i][j] = 0       // Finally Dead
```

### 📊 Complexity Analysis
* **Time Complexity:** `O(m * n)`
    * We visit every cell in the matrix exactly twice. During the first pass, we do 8 constant-time directional checks. Since `2 * m * n` scales linearly with the size of the grid, the Big-O time complexity remains strictly `O(m * n)`.

* **Space Complexity:** `O(1)`
    * **(Optimal)** We modify the grid strictly in-place. Because we hijacked the integer values to store our intermediate states instead of allocating a new array, the extra memory required is constant, regardless of how large the grid gets!
---
