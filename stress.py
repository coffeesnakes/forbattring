class Solution(object):
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
                sum -= values[s[i]]
            else:
                sum += values[s[i]]
                i += 1
        
        return sum
        