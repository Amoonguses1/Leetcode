/*
This is an answer for
https://leetcode.com/problems/letter-case-permutation/description/

Time: O(2^^N)
Space: O(2^^N)
N = len(s)
*/
package main

import (
	"bytes"
	"regexp"
	"strings"
)

var isDigit = regexp.MustCompile(`^[1-9]$`)

// Returns a list of all possible strings to create from the given string.
// Transforms every letter individually to be lowercase or uppercase to create another string.
func letterCasePermutation(s string) []string {
	var buf bytes.Buffer
	res := []string{}
	s = strings.ToLower(s)
	permutations(s, 0, buf, &res)
	return res
}

// Creates other strings from the given string.
func permutations(s string, pos int, buf bytes.Buffer, res *[]string) {
	if pos >= len(s) {
		*res = append(*res, buf.String())
		return
	}

	for pos < len(s) && isDigit.MatchString(string(s[pos])) {
		buf.WriteString(string(s[pos]))
		pos++
	}

	if pos >= len(s) {
		*res = append(*res, buf.String())
		return
	}

	buf.WriteString(string(s[pos]))
	permutations(s, pos+1, buf, res)
	buf.Truncate(buf.Len() - 1)
	buf.WriteString(strings.ToUpper(string(s[pos])))
	permutations(s, pos+1, buf, res)
}
