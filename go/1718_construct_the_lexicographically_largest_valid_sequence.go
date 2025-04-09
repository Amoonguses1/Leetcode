/*
This is an answer for
https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

Time: O(n!)
Space: O(n)
*/
package main

// Finds a sequence with elements in the range [1, n]
// that satisfies all of the following:
//
// The integer 1 occurs once
// Each integer between 2 and n occurs twice
// every integer i between 2 and n,
// the distance between the two occurrences of i is exactly i
func constructDistancedSequence(n int) []int {
	res := make([]int, 2*n-1)
	used := make([]bool, n+1)
	isValidArrangement(res, used, n, 0)
	return res
}

// Checks if the current slice cur is the valid sequence.
// if the current sequence is valid, the result sequence is in cur.
func isValidArrangement(cur []int, used []bool, n, index int) bool {
	for index < len(cur) && cur[index] != 0 {
		index += 1
	}
	if index == len(cur) {
		return true
	}

	for i := n; i > 0; i-- {
		if used[i] {
			continue
		}

		if i == 1 {
			cur[index] = 1
			used[1] = true
			if isValidArrangement(cur, used, n, index+1) {
				return true
			}
			cur[index] = 0

			used[1] = false
		} else if index+i < len(cur) && cur[index+i] == 0 {
			cur[index], cur[index+i] = i, i
			used[i] = true
			if isValidArrangement(cur, used, n, index+1) {
				return true
			}
			cur[index], cur[index+i] = 0, 0
			used[i] = false
		}
	}

	return false
}
