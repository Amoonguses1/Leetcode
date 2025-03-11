/*
This is an answer for
https://leetcode.com/problems/circular-permutation-in-binary-representation/description/

Time: O(2^^n)
Space: 0(2^^n)
*/
package main

// Return any permutation p of (0,1,2.....,2^n -1) such that:
//
// p[0] = start
// p[i] and  p[i+1] differ by only one bit in their binary representation.
// p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
func circularPermutation(n int, start int) []int {
	numGrayCodes := 1 << n
	circularGray := make([]int, numGrayCodes)

	for i := 0; i < numGrayCodes; i++ {
		gray := i ^ (i >> 1)
		circularGray[i] = gray ^ start
	}

	return circularGray
}
