/*
This is an answer for
https://leetcode.com/problems/path-with-maximum-gold/description/

Time: O(M^2N^2)
Space: O(M^2N^2)
M = len(grid), N = len(grid[0])
*/
package main

// Represents a cell with no gold.
const emptyCell = 0

// The helper variable to define movement directions (right, left, down, up).
var directions = [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

// Returns the maximum amount of gold you can collect.
//
// Restrictions
// Every time you are located in a cell you will collect all the gold in that cell.
// From your position, you can walk one step to the left, right, up, or down.
// You can't visit the same cell more than once.
// Never visit a cell with 0 gold.
// You can start and stop collecting gold from any position in the grid that has some gold.
func getMaximumGold(grid [][]int) int {
	res := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			res = max(collectGold(grid, i, j), res)
		}
	}

	return res
}

// Performs a DFS search to collect the maximum amount of gold
// starting from the given cell (row, col).
//
// The function marks the current cell as visited (by setting it to 0)
// to prevent revisiting within the same path, explores all four directions,
// and then restores the cell's original value after backtracking.
func collectGold(grid [][]int, row, col int) int {
	if !isValidPosition(row, col, grid) || isEmptyCell(row, col, grid) {
		return 0
	}

	currentPosAmount := grid[row][col]
	grid[row][col] = 0
	maxGold := 0
	for _, direction := range directions {
		nextRow, nextCol := row+direction[0], col+direction[1]
		maxGold = max(collectGold(grid, nextRow, nextCol), maxGold)
	}
	grid[row][col] = currentPosAmount
	return maxGold + currentPosAmount
}

// Checks if the given position is in the grid.
func isValidPosition(row, col int, grid [][]int) bool {
	return 0 <= row && row < len(grid) && 0 <= col && col < len(grid[0])
}

// Checks if the given cell contains no gold.
func isEmptyCell(row, col int, grid [][]int) bool {
	return grid[row][col] == emptyCell
}
