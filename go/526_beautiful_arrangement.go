/*
This is an answer for
https://leetcode.com/problems/beautiful-arrangement/description/

Time: O(N!)
Space: O(N)
*/
package main

func countArrangement(n int) int {
	return searchArrangement(n, n, 0)
}

func searchArrangement(n, pos, mask int) int {
	if pos < 2 {
		return 1
	}

	cnt := 0
	for i := n; i > 0; i-- {
		if (mask>>i)&1 == 0 && (pos%i == 0 || i%pos == 0) {
			cnt += searchArrangement(n, pos-1, mask|1<<i)
		}
	}
	return cnt
}
