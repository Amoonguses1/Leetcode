/*
This is an answer for
https://leetcode.com/problems/numbers-with-same-consecutive-differences

Time: O(2^^n)
Space: O(2^^n)
*/
package main

// Returns an array of all the integers of length n
// where the difference between every two consecutive digits is k.
func numsSameConsecDiff(n int, k int) []int {
	res := []int{}
	for i := 1; i < 10; i++ {
		res = append(res, generateNums(i, k, n-1)...)
	}
	return res
}

// generateNums is a recursive helper function
// that generates integers with a given number of digits,
// where the difference between every two consecutive digits is exactly `k`.
func generateNums(cur, diff, digits int) []int {
	if digits == 0 {
		return []int{cur}
	}

	res := []int{}
	if isOneDigitNumber(cur%10 - diff) {
		nextDigit := cur%10 - diff
		res = append(res, generateNums(cur*10+nextDigit, diff, digits-1)...)
	}
	if isOneDigitNumber(cur%10+diff) && diff != 0 {
		nextDigit := cur%10 + diff
		res = append(res, generateNums(cur*10+nextDigit, diff, digits-1)...)
	}
	return res
}

// Checks whether the given integer is one-digit integer.
func isOneDigitNumber(n int) bool {
	return 0 <= n && n < 10
}
