/*
This is an answer for
https://leetcode.com/problems/happy-number/description/
Time: O(1)
Space: O(1)
*/
package main

func isHappy(n int) bool {
	seen := make(map[int]struct{})
	for n != 1 {
		if _, ok := seen[n]; ok {
			return false
		}
		seen[n] = struct{}{}
		nextNum := 0
		for n != 0 {
			nextNum += (n % 10) * (n % 10)
			n /= 10
		}
		n = nextNum
	}
	return true
}
