"""
================================================================================
📄 File: approaches.py
================================================================================
Description: 
    Solutions for Conway's Game of Life (often recognized as LeetCode 289).
    This classic cellular automaton simulates generations of cells based on 
    underpopulation, survival, overpopulation, and reproduction.

Approaches Included:
    1. _approach_01_extra_space -> The standard simulation using an O(m*n) grid. 🧮
    2. _approach_02_inplace     -> The optimized O(1) space trick using state mapping! 🧠

State Mapping Legend (For In-Place Logic):
    0: Dead  -> Stays Dead
    1: Alive -> Stays Alive
    2: Dead  -> Comes to Life (Reproduction) 🧟‍♂️
    3: Alive -> Dies (Under/Overpopulation) 👻
================================================================================
"""
from typing import List, Tuple

class Approaches:
    def _approach_01_extra_space(self) -> None:
        # 🧮 APPROACH 1: The Standard Simulation (Extra Space)
        # We create a brand new blank canvas to draw the next generation, 
        # ensuring we don't accidentally overwrite the present while looking at it!
        
        m: int = len(self._board)
        n: int = len(self._board[0])
        
        # 🖼️ Create our blank canvas for the next generation
        next_generation: List[List[int]] = [[0] * n for _ in range(m)]
        
        # 🧭 The 8 directions (horizontal, vertical, diagonal) to find our neighbors
        directions: Tuple[Tuple[int]] = ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1))

        # 🔍 Loop through every single cell on the board
        for i in range(m):
            for j in range(n):
                alive_neighbors: int = 0
                
                # 👀 Look around in all 8 directions
                for dr, dc in directions:
                    r: int = i + dr
                    c: int = j + dc

                    # Is this neighbor on the board? And are they alive?
                    if 0 <= r < m and 0 <= c < n and self._board[r][c] == 1: 
                        alive_neighbors += 1

                # ⚖️ Apply the Rules of Life!
                if self._board[i][j] == 1: 
                    # Rule: Survival (2 or 3 neighbors)
                    if 2 <= alive_neighbors <= 3:
                        next_generation[i][j] = 1
                else:
                    # Rule: Reproduction (Exactly 3 neighbors)
                    if alive_neighbors == 3:
                        next_generation[i][j] = 1

        # 🔄 Overwrite the original board with our newly calculated generation
        for i in range(m):
            for j in range(n):
                self._board[i][j] = next_generation[i][j]

        # 🧹 Clean up the extra memory
        del(next_generation)


    def _approach_02_inplace(self) -> None:
        # 🧠 APPROACH 2: In-Place State Mapping
        # We save O(m*n) memory by using dummy states (2 and 3) to remember 
        # what the cell *used* to be, while updating what it *will* be!
        
        m: int = len(self._board)
        n: int = len(self._board[0])
        directions: Tuple[Tuple[int]] = ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1))

        # 🔄 PASS 1: Apply rules and set temporary states
        for i in range(m):
            for j in range(n):
                alive_neighbors: int = 0

                # 👀 Count the living neighbors
                for dr, dc in directions:
                    r: int = i + dr
                    c: int = j + dc

                    if 0 <= r < m and 0 <= c < n:
                        # 💡 If a cell is NOT 0 (Dead) and NOT 2 (Dead->Alive), 
                        # it means it is either 1 (Alive) or 3 (Alive->Dead).
                        # In either case, it is currently alive in THIS generation!
                        if not (self._board[r][c] == 0 or self._board[r][c] == 2):
                            alive_neighbors += 1
                
                # ⚖️ Apply the rules using our temporary state mapping
                if self._board[i][j] == 1:
                    # Rule: Under/Overpopulation (Dies) -> Mark as 3 👻
                    if not 2 <= alive_neighbors <= 3:
                        self._board[i][j] = 3
                else:
                    # Rule: Reproduction (Lives) -> Mark as 2 🧟‍♂️
                    if alive_neighbors == 3:
                        self._board[i][j] = 2
        
        # 🔄 PASS 2: Time travel! Finalize the future states
        for i in range(m):
            for j in range(n):
                if self._board[i][j] == 2: 
                    self._board[i][j] = 1  # 🧟‍♂️ Successfully resurrected
                elif self._board[i][j] == 3: 
                    self._board[i][j] = 0  # 👻 Has passed on
