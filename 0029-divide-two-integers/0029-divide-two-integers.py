class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            return float('inf')
        
        negative = False
        if (dividend < 0) != (divisor < 0):
            negative = True
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            
            result += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)
        
        if negative:
            result = -result
        
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        
        return result
