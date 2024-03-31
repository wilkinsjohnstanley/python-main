class Solution(object):
    def romanToInt(self, s):
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        # total = 0
        # prev_value = 0

        # for char in reversed(s): 
        #     current_value = roman_values[char] 
        #     print(f"roman_values[char] returns {roman_values[char]}")
        #     if current_value < prev_value:
        #         total -= current_value
        #     else:
        #         total += current_value
        #     prev_value = current_value

        # return total
        '''Here's the NeedCode solution'''
        res = 0
        for i in range(len(s)):
            if i+1<len(s) and roman_values[s[i]]<roman_values[s[i+1]]:
                res -= roman_values[s[i]]
            else:
                res += roman_values[s[i]]
        return res

# Test the class method
solution = Solution()
print(solution.romanToInt("III"))    # Output: 3
print(solution.romanToInt("IV"))     # Output: 4
print(solution.romanToInt("VI"))     # Output: 6
print(solution.romanToInt("IX"))     # Output: 9
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))# Output: 1994
