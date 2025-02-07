/*
This is an answer for
https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

Time: O(N)
Space: O(min(limit, N))
N = len(queries)
*/
package main

func queryResults(limit int, queries [][]int) []int {
	result := make([]int, len(queries))
	colorCount := make(map[int]int)
	colors := make(map[int]int)

	for i, query := range queries {
		// decrease the current color count
		if curColor, ok := colors[query[0]]; ok {
			colorCount[curColor]--
			if colorCount[curColor] == 0 {
				delete(colorCount, curColor)
			}
		}

		// Change the ball color
		colors[query[0]] = query[1]
		colorCount[query[1]]++

		// store the result of ith query
		result[i] = len(colorCount)
	}

	return result
}
