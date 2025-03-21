/*
This is an answer for
https://leetcode.com/problems/iterator-for-combination/description/

Time: O(2^N)
Space: O(2^N)
N = len(characters)
*/
package main

import (
	"bytes"
	"strings"
)

// CombinationIterator is a iterator
// that returns the combination of the specified length string from the given string.
// Methods:
// - next(): Returns the next combination of length combinationLength in lexicographical order.
// - hasNext(): Returns true if and only if there exists a next combination.
type CombinationIterator struct {
	Combinations []string
	Pos          int
}

// Initializes the object with a string characters of sorted distinct lowercase English letters
// and a number combinationLength as arguments.
func Constructor(characters string, combinationLength int) CombinationIterator {
	characters = strings.ToLower(characters)
	var buf bytes.Buffer
	res := []string{}
	calcSortedCharactersPermutations(characters, 0, combinationLength, buf, &res)
	return CombinationIterator{Combinations: res, Pos: 0}
}

// Generates all possible sorted permutations of characters from the given string,
// with the specified target length.
// Uses backtracking to build permutations
// and appends them to the result slice once the target length is reached.
func calcSortedCharactersPermutations(characters string, pos, targetLength int, buf bytes.Buffer, res *[]string) {
	if buf.Len() == targetLength {
		*res = append(*res, buf.String())
		return
	}

	for i := pos; i < len(characters); i++ {
		buf.WriteByte(characters[i])
		calcSortedCharactersPermutations(characters, i+1, targetLength, buf, res)
		buf.Truncate(buf.Len() - 1)
	}
}

// Returns the next combination of length combinationLength in lexicographical order.
func (this *CombinationIterator) Next() string {
	this.Pos += 1
	return this.Combinations[this.Pos-1]
}

// Returns true if and only if there exists a next combination.
func (this *CombinationIterator) HasNext() bool {
	return len(this.Combinations) > this.Pos
}

/**
 * Your CombinationIterator object will be instantiated and called as such:
 * obj := Constructor(characters, combinationLength);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
