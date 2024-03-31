class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Convert the integer to a string
        num_str = str(x)
        reversed_string = num_str[::-1]
        if (num_str==reversed_string):
            return True
        else:
            return False
#my first algorithm solved by myself only googling syntax for [::-1] 