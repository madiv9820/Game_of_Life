# [Game Of Life 🎮](https://leetcode.com/problems/game-of-life/description/?envType=study-plan-v2&envId=top-interview-150)

### 🧬 Conway's Game of Life
Welcome to the most famous "zero-player game" in computational history! Devised by the brilliant British mathematician John Horton Conway in 1970, this is a cellular automaton where you don't play to win—you set the stage and watch the universe evolve. 🌌

### 🗺️ The Setup
You are given a universe represented by an `m x n` grid. Every cell in this universe can only exist in one of two states:

* 1 = Alive 🟢
* 0 = Dead 💀

Every single cell is constantly influenced by its **8 immediate neighbors** (horizontal, vertical, and diagonal).

#### 📜 The Four Universal Rules
To figure out what the grid will look like in the next generation, the universe looks at the current board and strictly applies these four rules:

1. **Lonely Demise (Underpopulation): 🥶** <br>
Any live cell with *fewer than two* live neighbors dies, as if caused by isolation and loneliness.

2. **The Sweet Spot (Survival): 😌** <br>
Any live cell with exactly *two or three* live neighbors is perfectly content. It lives on to the next generation!

3. **Crushed (Overpopulation): 💥** <br>
Any live cell with *more than three* live neighbors dies, suffocated by overpopulation.

4. **The Miracle of Life (Reproduction): 🌱** <br>
Any dead cell with *exactly three* live neighbors springs to life, as if by reproduction.

#### ⚠️ The Ultimate Catch (The Challenge)
Here is where things get tricky: The universe ticks forward **simultaneously**. ⏱️

You cannot update a cell and then let the next cell look at that new data. Births and deaths happen at the exact same millisecond across the entire grid. Every calculation for the future must be based *strictly* on the present state of the board.

#### 🎯 Your Mission
Given the current state of the board, write an algorithm to step the universe forward by exactly one generation.

> ***Constraints:*** *Mutate the board strictly in-place.*
* Do not return anything! You are the architect of the universe; simply let the evolution happen.

#### 🧪 Test Your Universe (Examples)
**Example 1:** The Glider 🛸 <br>
If you look closely at the coordinates, this matrix is actually a "Glider" moving diagonally across the board! 
> **Input:**
> ```
> board = [
>  [0, 1, 0],
>  [0, 0, 1],
>  [1, 1, 1],
>  [0, 0, 0]
> ]
> ```
> **Output:**
> ```
> [
>  [0, 0, 0],
>  [1, 0, 1],
>  [0, 1, 1],
>  [0, 1, 0]
> ]
> ```
> **Visualization:**
> ```
> 💀 🟢 💀                💀 💀 💀
> 💀 💀 🟢    ------>     🟢 💀 🟢 
> 🟢 🟢 🟢                💀 🟢 🟢 
> 💀 💀 💀                💀 🟢 💀 
>```

**Example 2:** The Block Formation 🧱 <br>
Here, a missing corner piece is surrounded by exactly 3 alive neighbors, triggering the **Reproduction** rule to form a perfectly stable 2x2 block.
> **Input:**
> ```
> board = [
>   [1, 1],
>   [1, 0]
> ]
> ```
> **Output:**
> ```
> [
>   [1, 1],
>   [1, 1]
> ]
> ```
> **Visualization:**
> ```
> 🟢 🟢   ---->  🟢 🟢
> 🟢 💀          🟢 🟢
> ```

#### 🚧 The Laws of Physics (Constraints)
Before you build your algorithm, keep these physical limits of our universe in mind:
* `m == board.length` *(Rows)*
* `n == board[i].length` *(Columns)*
* `1 <= m, n <= 25`
    * *Developer Note:* Because the absolute maximum grid size is 25x25 (625 total cells), algorithmic time complexity isn't our primary bottleneck here. An $O(M \times N)$ solution is blazing fast. The real challenge is optimizing the Space Complexity to $O(1)$! 🧠
* `board[i][j]` is `0` or `1`
    * The universe is strictly binary. No quantum superposition allowed!

### 🚀 Approaches 
| Feature | [🧮 Extra Space](docs/extra-space.md) | [🧠 In-Place Mapping](docs/inplace.md) |
| :--- | :--- | :--- |
| **Core Concept** | Blank canvas (New `m x n` grid) | Dummy state mapping (`2` and `3`) |
| **Time Complexity** | `O(m * n)` | `O(m * n)` |
| **Space Complexity** | `O(m * n)` | `O(1)` *(Strictly in-place)* |
| **Grid Iterations** | 1 full pass (Reads original, writes new) | 2 full passes (Calculates, then finalizes) |
| **Readability** | High (Very intuitive and clean) | Medium (Requires knowing the state map) |
| **Bug Potential** | Low | Higher (Easy to mix up temporary states) |
| **Interview Value**| Baseline / Entry-level solution | Optimal / Senior-level optimization |

### 📂 Repository Structure
```text
📦 game-of-life
 ┣ 📂 docs                  # contains comprehensive markdown documentation
 ┃ ┣ 📜 extra-space.md  
 ┃ ┗ 📜 inplace.md
 ┣ 📂 source                # core application logic
 ┃ ┣ 📜 approaches.py       # houses the algorithmic implementations
 ┃ ┗ 📜 solution.py         # provides the main interface
 ┗ 📂 test                  # automated testing suite
   ┣ 📜 cases.json          # holds the structured mock data
   ┗ 📜 test.py             # validates the source code against these edge cases
```

#### 🚦 How to Run the Tests
To execute the test suite and validate the algorithms against the JSON test cases, run the following command from the root of the repository:
```bash
python3 -m test.test -v
```
---
