/*
This is an answer for
https://leetcode.com/problems/letter-tile-possibilities/description/

Time: O(N!)
Space: O(N!)
N = len(tiles)
*/
package main

// The number of types of characters that may be given in the input (A-Z)
const stringTypes = 26

// The smallest string code
const baseRune = 'A'

// Returns the number of possible non-empty sequences of letters
// using the letters printed on the given string 'tiles'
//
// Each letter in 'tiles' can be used at most as many times as it appears.
// The order of letters matters.
func numTilePossibilities(tiles string) int {
	counter := make([]int, stringTypes)
	for _, tile := range tiles {
		counter[tile-baseRune]++
	}
	return countPossibilityStringfromTile(counter)
}

// countPossibilityStringfromTile performs a backtracking search to count all possible
// non-empty sequences of letters using the available letter frequencies.
//
// This function recursively selects a letter that is still available in 'counter',
// decreases its count, explores further possibilities, and then restores the count
// (backtracking).
func countPossibilityStringfromTile(counter []int) int {
	var res int
	for i, cnt := range counter {
		if cnt != 0 {
			res++
			counter[i]--
			res += countPossibilityStringfromTile(counter)
			counter[i]++
		}
	}
	return res
}
