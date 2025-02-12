/*
This is an answer for
https://leetcode.com/problems/shortest-completing-word/description/

Time: O(MN)
Space: O(N)
M is the number of words. N is the average length of words.
*/
package main

import (
	"math"
	"regexp"
	"strings"
)

// ShortestCompletingWord finds the shortest completing word.
// A completing word is a word that contains all letters in licensePlate.
// Ignore numbers and spaces in licensePlate, and treat that letters are
// case insensitive.
func ShortestCompletingWord(licensePlate string, words []string) string {
	re := regexp.MustCompile(`[0-9]`)
	alphabeticalMap := getAlphabet(formatWord(licensePlate, re))

	// Store result
	result := ""
	stringLength := math.MaxInt

	// Iterate the given words
	for _, word := range words {
		if isCompletingWord(formatWord(word, re), alphabeticalMap) {
			if stringLength > len(word) {
				result = word
				stringLength = len(word)
			}
		}
	}

	return result
}

// formatWord formats the given word by removing spaces and numbers,
// and converting all letters to lowercase.
func formatWord(word string, re *regexp.Regexp) string {
	lowerWord := strings.ToLower(word)
	wordWithoutSpace := strings.Replace(lowerWord, " ", "", -1)

	return re.ReplaceAllString(wordWithoutSpace, "")
}

// getAlphabet returns a frequency map of each letter in the given string.
func getAlphabet(licensePlate string) map[byte]int {
	alphabetMap := make(map[byte]int)
	for i := 0; i < len(licensePlate); i++ {
		alphabetMap[licensePlate[i]]++
	}

	return alphabetMap
}

// isCompletingWord checks if a word contains all letters from the given frequency map.
func isCompletingWord(word string, alphabeticalMap map[byte]int) bool {
	for key, val := range alphabeticalMap {
		if strings.Count(word, string(key)) < val {
			return false
		}
	}
	return true
}
