/*
This is an answer for
https://leetcode.com/problems/find-unique-binary-string/description/

Time: O(N)
Space: O(N)
N = len(nums) = len(nums[i]) for 0 <= i < n
*/
package main

import "strings"

// Returns a binary string of length n that does not appear in nums.
func findDifferentBinaryString(nums []string) string {
	var sb strings.Builder
	for i, num := range nums {
		if num[i] == '1' {
			sb.WriteByte('0')
		} else {
			sb.WriteByte('1')
		}
	}
	return sb.String()
}
