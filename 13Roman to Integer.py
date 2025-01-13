class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        roman = {'I':1, 'V':5, "X":10, 'L':50, 'C':100, "D":500, "M":1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        for char in s :
            ans += roman[char]

        return ans
    


s = Solution.romanToInt('self','IXXXXXX')
print(s)