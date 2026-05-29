"""
================================================================================
📄 File: solution.py
================================================================================
Description: 
    The main entry point and runner for Conway's Game of Life (LeetCode 289).
    This file handles the specific interface expected by the caller/tester 
    and delegates the heavy algorithmic lifting to the Approaches class.

Usage:
    Instantiate the Solution class and call the `gameOfLife(board)` method.
    You can easily test different time/space complexities by commenting/uncommenting
    which underlying approach is executed inside the method! 🧪
================================================================================
"""
from typing import List
from .approaches import Approaches

class Solution(Approaches):
    # 🧩 By inheriting from Approaches, this class automatically gains access 
    # to all the simulation algorithms we built in `approaches.py`!
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Calculates the next state of Conway's Game of Life.
        Do not return anything, modify the board in-place instead.
        """
        
        # 📦 Bind the input board to our instance state so the hidden 
        # approach methods can seamlessly access and mutate it.
        self._board = board
        
        # 🚀 EXECUTION BLOCK
        # Choose your fighter! Comment/uncomment to swap the active algorithm.
        
        # self._approach_01_extra_space()    # 🧮 The standard O(m*n) memory simulation
        self._approach_02_inplace()          # 🧠 The optimal O(1) in-place state mapping trick
        