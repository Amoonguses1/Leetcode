/*
This is an answer for https://leetcode.com/problems/regions-cut-by-slashes/ .

Time: O(N^2)
Space: O(N^2)
N = len(grid)
*/
package main

func regionsBySlashes(grid []string) int {
	length := len(grid)
	regions := 0
	largeGrid := makeLargeGrid(length, convertToRunes(grid))

	for i := 0; i < 3*length; i++ {
		for j := 0; j < 3*length; j++ {
			regions += fillRegion(i, j, largeGrid)
		}
	}

	return regions
}

func makeLargeGrid(length int, runesGrid [][]rune) [][]int {
	largeGrid := make([][]int, 3*length)
	for i := 0; i < 3*length; i++ {
		largeGrid[i] = make([]int, 3*length)
	}
	for i := 0; i < length; i++ {
		for j := 0; j < length; j++ {
			if runesGrid[i][j] == rune('/') {
				largeGrid[3*i][3*j+2] = 1
				largeGrid[3*i+1][3*j+1] = 1
				largeGrid[3*i+2][3*j] = 1
			} else if runesGrid[i][j] == rune('\\') {
				largeGrid[3*i][3*j] = 1
				largeGrid[3*i+1][3*j+1] = 1
				largeGrid[3*i+2][3*j+2] = 1
			}
		}
	}

	return largeGrid
}

func convertToRunes(grid []string) [][]rune {
	runesGrid := make([][]rune, len(grid))
	for i, row := range grid {
		runesGrid[i] = []rune(row)
	}
	return runesGrid
}

func fillRegion(i, j int, largeGrid [][]int) int {
	if min(i, j) < 0 || max(i, j) >= len(largeGrid) || largeGrid[i][j] != 0 {
		return 0
	}

	largeGrid[i][j] = 1
	fillRegion(i, j-1, largeGrid)
	fillRegion(i, j+1, largeGrid)
	fillRegion(i-1, j, largeGrid)
	fillRegion(i+1, j, largeGrid)
	return 1
}
