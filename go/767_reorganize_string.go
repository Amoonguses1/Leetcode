package main

import (
	"container/heap"
	"errors"
	"regexp"
)

// Represents a character and its frequency.
type charFrequency struct {
	char      byte
	frequency int
}

// charactersFrequencyHeap is a max-heap of charFrequency elements,
// where elements are ordered by frequency in descending order.
//
// This heap implements the heap.Interface from the "container/heap" package
// and can be used with heap.Push and heap.Pop.
type charactersFrequencyHeap []charFrequency

// Returns the number of elements the charactersFrequencyHeap
func (h charactersFrequencyHeap) Len() int { return len(h) }

// Defines the max-heap property: higher frequency has higher priority.
func (h charactersFrequencyHeap) Less(i, j int) bool { return h[i].frequency > h[j].frequency }

// Swaps two elements in charactersFrequencyHeap.
func (h charactersFrequencyHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

// Push adds an element to the heap.
func (h *charactersFrequencyHeap) Push(x any) {
	*h = append(*h, x.(charFrequency))
}

// Removes and returns the largest element.
func (h *charactersFrequencyHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// wraps heap.Push(charactersFrequencyHeap, any) to detect the wrong type
func pushCharFrequency(h *charactersFrequencyHeap, cc charFrequency) {
	heap.Push(h, cc)
}

// wraps heap.Pop(charactersFrequencyHeap) to detect the wrong type
func popCharFrequency(h *charactersFrequencyHeap) (charFrequency, error) {
	x := heap.Pop(h)
	cc, ok := x.(charFrequency)
	if !ok {
		return charFrequency{}, errors.New("charactersFrequencyHeap: invalid type in Pop")
	}
	return cc, nil
}

// hasNonLowerAlphabet is a regular expression that matches any character
// that is not a lowercase English letter (a-z).
var hasNonLowerAlphabet = regexp.MustCompile(`[^a-z]`)

// Rearrange the characters of s so that any two adjacent characters are not the same.
func RearrangeDistinctAdjacent(s string) (string, error) {
	if hasNonLowerAlphabet.MatchString(s) {
		return "", errors.New("input must be only lower case alphabet")
	}

	// There is another way that the process of creating a heap is divided into another function,
	// but that approach makes it hard to judge there is no possible arrangement.
	charactersFrequency := make(map[byte]int)
	for i := range s {
		charactersFrequency[s[i]]++
	}

	maxAllowed := (len(s) + 1) / 2
	maxHeap := &charactersFrequencyHeap{}
	for ch, frequency := range charactersFrequency {
		// Check if there is any possible rearrangement.
		// If there is no characters whose adjacents are not the same,
		// The pattern that a single character can commonly use is as follows.
		// a*a*a...*a
		// Let n be the length of the string, the max frequency of a character is (n+1)/2
		if frequency > maxAllowed {
			return "", nil
		}
		pushCharFrequency(maxHeap, charFrequency{char: ch, frequency: frequency})
	}

	var res []byte
	var prev charFrequency
	for maxHeap.Len() > 0 {
		cur, err := popCharFrequency(maxHeap)
		if err != nil {
			return "", err
		}
		res = append(res, cur.char)
		cur.frequency--
		prev = cur

		// Push previous character back if it still has remaining frequency
		if prev.frequency > 0 {
			heap.Push(maxHeap, prev)
		}
	}

	return string(res), nil
}
