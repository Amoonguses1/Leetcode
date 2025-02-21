/*
This is an answer for
https://leetcode.com/problems/most-common-word/

Time: O(N+M)
Space: O(N+M)
N = len(paragraph), M = len(banned)
*/
package main

import (
	"regexp"
	"strings"
)

var re = regexp.MustCompile(`^[a-z]$`)

// Returns the most common word from the given paragraph that is not banned.
func MostCommonWord(paragraph string, banned []string) string {
	wordsCounter := getWordsFrequency(paragraph)
	bannedWordsMap := getBannedWordsMap(banned)
	maxFreq := 0
	res := ""
	for word, freq := range wordsCounter {
		_, isBanned := bannedWordsMap[word]
		if !isBanned && maxFreq < freq {
			maxFreq = freq
			res = word
		}
	}

	return res
}

// Returns a case-insensitive word frequency map.
// A word is defined as a sequence of alphabetic characters (A-Z, a-z).
func getWordsFrequency(paragraph string) map[string]int {
	wordsCounter := make(map[string]int)
	cur := ""
	for i := 0; i < len(paragraph); i++ {
		ch := strings.ToLower(string(paragraph[i]))
		if re.MatchString(ch) {
			cur += ch
		} else if len(cur) > 0 {
			wordsCounter[cur]++
			cur = ""
		}
	}
	if len(cur) > 0 {
		wordsCounter[cur]++
	}
	return wordsCounter
}

// Returns a map with the banned words as keys.
func getBannedWordsMap(banned []string) map[string]struct{} {
	bannedWordsMap := make(map[string]struct{})
	for _, word := range banned {
		bannedWordsMap[strings.ToLower(word)] = struct{}{}
	}

	return bannedWordsMap
}
