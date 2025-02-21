/*
This is an answer for
https://leetcode.com/problems/binary-watch/description/

Time: O(1)
Space: O(1)
*/
package main

import "fmt"

// readBinaryWatch return all possible times the watch could represent.
func readBinaryWatch(turnedOn int) []string {
	if turnedOn > 8 {
		return []string{}
	}

	res := []string{}
	for h := 0; h < 12; h++ {
		for m := 0; m < 60; m++ {
			if countBitOne(h)+countBitOne(m) == turnedOn {
				res = append(res, fmt.Sprintf("%d:%02d", h, m))
			}
		}
	}
	return res
}

// countBitOne count the number of 1's in a binary string of the given integer
func countBitOne(num int) int {
	res := 0
	for num > 0 {
		res += num % 2
		num /= 2
	}
	return res
}
