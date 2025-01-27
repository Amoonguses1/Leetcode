# Time: O(N)
# Space: O(1)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Function to calculate the product of two given
        numbers represented by strings

        Args:
            num1(str): a string consist of digits only
            do not contain any leading zero, except the number 0 itself
            num2(str): a string consist of digits only
            do not contain any leading zero, except the number 0 itself

        Returns:
            str: the string that is the product of two numbers in a string
        """
        return str(self.myatoi(num1)*self.myatoi(num2))

    def decode(self, st):
        res = 0
        for ch in st:
            res *= 10
            res += ord(ch) - ord("0")
        return res
