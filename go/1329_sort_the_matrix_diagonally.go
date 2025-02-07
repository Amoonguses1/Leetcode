/*
This is an answer for
https://leetcode.com/problems/sort-the-matrix-diagonally/

Time: O((rows+cols)log(rows+cols))
Space: O(rows*cols)
rows = len(mat), col = len(mat[0])
*/
package main

import "sort"

func DiagonalSort(mat [][]int) [][]int {
	rows, cols := len(mat), len(mat[0])
	sortVartical(&mat, rows, cols)
	sortHorizontal(&mat, rows, cols)

	return mat
}

func sortVartical(mat *[][]int, rows, cols int) {
	for i := 0; i < rows; i++ {
		diagonalBound := min(cols, rows-i)
		targetSlice := make([]int, diagonalBound)
		for j := 0; j < diagonalBound; j++ {
			targetSlice[j] = (*mat)[i+j][j]
		}

		sort.Slice(targetSlice, func(i, j int) bool { return targetSlice[i] < targetSlice[j] })
		for j := 0; j < diagonalBound; j++ {
			(*mat)[i+j][j] = targetSlice[j]
		}
	}
}

func sortHorizontal(mat *[][]int, rows, cols int) {
	for i := 0; i < cols; i++ {
		diagonalBound := min(rows, cols-i)
		targetSlice := make([]int, diagonalBound)
		for j := 0; j < diagonalBound; j++ {
			targetSlice[j] = (*mat)[j][i+j]
		}

		sort.Slice(targetSlice, func(i, j int) bool { return targetSlice[i] < targetSlice[j] })
		for j := 0; j < diagonalBound; j++ {
			(*mat)[j][i+j] = targetSlice[j]
		}
	}
}
