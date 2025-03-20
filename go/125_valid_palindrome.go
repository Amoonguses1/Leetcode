/*
This is an answer for
https://leetcode.com/problems/valid-palindrome/

Time: O(N)
Space: O(N)
N = len(s)
*/
package main

import (
	"regexp"
	"strings"
)

var re = regexp.MustCompile(`^[a-z0-9]$`)

// Checks if a phrase
// after converting all uppercase letters into lowercase letters
// and removing all non-alphanumeric characters is a palindrome.
func isPalindrome(s string) bool {
	formattedString := formatString(s)
	length := len(formattedString)
	for i := 0; i < length/2; i++ {
		if formattedString[i] != formattedString[length-i-1] {
			return false
		}
	}
	return true
}

// formatString converts all uppercase letters in the input string to lowercase
// and removes non-alphanumeric characters, keeping only lowercase letters and digits.
func formatString(s string) string {
	var result strings.Builder
	for _, ch := range s {
		ch := strings.ToLower(string(ch))
		if re.MatchString(ch) {
			result.WriteString(ch)
		}
	}
	return result.String()
}
