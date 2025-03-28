/*
This is an answer for
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

Time: O(3^n)
Space: O(n)
*/
package main

// Return the kth string of this list or return an empty string
// if there are less than k happy strings of length n.
func getHappyString(n int, k int) string {
	candi := []string{"a", "b", "c"}
	kthHappyString := []byte{}
	return findKthHappyString(n, &k, "", candi, &kthHappyString)
}

// This function is a helper function to construct happy string in in lexicographical order
// and returns the kth happy string if exist.
func findKthHappyString(length int, count *int, lastChar string, candi []string, buf *[]byte) string {
	if len(*buf) == length {
		(*count)--
		if *count > 0 {
			return ""
		}
		return string(*buf)
	}

	for _, ch := range candi {
		if ch != lastChar {
			*buf = append(*buf, ch[0])
			happyString := findKthHappyString(length, count, ch, candi, buf)
			if happyString != "" {
				return happyString
			}
			*buf = (*buf)[:len(*buf)-1]
		}
	}

	return ""
}
