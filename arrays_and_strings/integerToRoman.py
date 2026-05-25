class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 5, 4, 1]
        romans = ["M", "CM", "D",  "CD", "C", "XC", "L", "XL", "X", "V", "IV", "I"]
        romanaNumeral = ""
        i = 0
        while num > 0:
            if num > integers[i]:
                romanaNumeral += romans[i]
                num -= integers[i]
            else:
                i += 1
        return romanaNumeral

