/*
This is an answer for
https://leetcode.com/problems/number-of-1-bits/description/

Time: O(logn)
Space: O(1)
*/
package main

func hammingWeight(n int) int {
	count := 0
	for n > 0 {
		count += n % 2
		n = n / 2
	}
	return count
}
