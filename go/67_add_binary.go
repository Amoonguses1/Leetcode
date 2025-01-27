// This code is an answer for
// https://leetcode.com/problems/add-binary/description/
// Time: O(N)
// Space: O(N)
// N = max(len(a), len(b))
package main

import "strings"

func addBinary(a string, b string) string {
	if len(a) < len(b) {
		a, b = b, a
	}

	aBools := stringToBools(reverseString(a))
	bBools := stringToBools(reverseString(b))

	carry := false
	var result []string

	for i := 0; i < len(aBools); i++ {
		add := false
		if i < len(bBools) {
			add = bBools[i]
		}
		digit, newCarry := fullAdder(aBools[i], add, carry)
		carry = newCarry
		result = append(result, digit)
	}

	if carry {
		result = append(result, "1")
	}

	return reverseString(strings.Join(result, ""))
}

func fullAdder(a, b, carry bool) (string, bool) {
	nextCarry := (a && b) || (b && carry) || (carry && a)
	sum := (a != b) != carry
	if sum {
		return "1", nextCarry
	}

	return "0", nextCarry
}

// Converts a binary string to a slice of bools.
func stringToBools(s string) []bool {
	result := make([]bool, len(s))
	for i, char := range s {
		result[i] = char == '1'
	}
	return result
}

// Converts a slice of bools to a binary string.
func boolsToBinaryString(bools []bool) string {
	var strResult []rune
	for i := len(bools) - 1; i >= 0; i-- {
		if bools[i] {
			strResult = append(strResult, '1')
		} else {
			strResult = append(strResult, '0')
		}
	}

	return string(strResult)
}

// Helper function to reverse a string
func reverseString(s string) string {
	runes := []rune(s)
	for i := len(runes)/2 - 1; i >= 0; i-- {
		opp := len(runes) - i - 1
		runes[i], runes[opp] = runes[opp], runes[i]
	}
	return string(runes)
}
