class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            digits = [0]
        val = digits[len(digits)-1]
        digits[len(digits)-1] += 1
        if val+1 == 10:
            digits.pop()
            new = self.plusOne(digits)
            new.append(0)
            return new
        return digits
        