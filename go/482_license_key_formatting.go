package main

import "strings"

// licenseKeyFormatting reformats the given string
// by grouping characters into k-sized sections, separated by dashes.
// The first group may be shorter but will contain at least one character.
func licenseKeyFormatting(s string, k int) string {
	// Remove dashes and convert to upper case
	inputStringWithoutDash := strings.Replace(s, "-", "", -1)
	upperString := strings.ToUpper(inputStringWithoutDash)

	// Return early if there is no need for formatting
	n := len(upperString)
	if n < k {
		return upperString
	}

	// Determine the size of the first group to ensure at least one character
	firstGroupSize := n % k
	if firstGroupSize == 0 {
		firstGroupSize = k
	}

	// Build the reformatted string adding dashes between groups
	var result strings.Builder
	result.WriteString(upperString[:firstGroupSize])
	for i := firstGroupSize; i < n; i += k {
		result.WriteString("-")
		result.WriteString(upperString[i : i+k])
	}

	return result.String()
}
