/*
This is an answer for
https://leetcode.com/problems/reverse-prefix-of-word/description/

Time: O(N)
Space: O(N)
*/
package main

import "strings"

func reversePrefix(word string, ch byte) string {
	var builder strings.Builder
	for i := 0; i < len(word); i++ {
		builder.WriteByte(word[i])
		if word[i] == ch {
			return reverseString(builder.String()) + word[i+1:]
		}
	}
	return word
}

func reverseString(word string) string {
	n := len(word)
	res := make([]byte, n)
	for i := 0; i < n; i++ {
		res[i] = word[n-1-i]
	}
	return string(res)
}
