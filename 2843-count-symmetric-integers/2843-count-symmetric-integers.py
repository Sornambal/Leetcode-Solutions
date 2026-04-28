class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high + 1):
            s = str(num)
            
            # skip odd length numbers
            if len(s) % 2 != 0:
                continue
            
            mid = len(s) // 2
            
            left = s[:mid]
            right = s[mid:]
            
            # sum of digits
            if sum(map(int, left)) == sum(map(int, right)):
                count += 1
        
        return count