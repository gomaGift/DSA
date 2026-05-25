class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanInts = {
            'I': 1,
            'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'M': 1000
        }
        sum = 0

        for i in range(len(s) - 1):
            if romanInts.get(s[i]) < romanInts.get(s[i+1]):
                sum -= romanInts.get(s[i])

            else:
                sum += romanInts.get(s[i])
        
        sum += romanInts.get(s[-1])
        return sum 