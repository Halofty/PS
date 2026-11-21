class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Create a set to store unique digits
        unique_digits = set(digits)
        
        # Calculate the total number of unique digits
        total_unique_digits = len(unique_digits)
        
        # If there are no unique digits, return 0
        if total_unique_digits == 0:
            return 0
        
        # Calculate the total numbers that can be formed with the unique digits
        # For each digit, we can choose to include it or not, hence 2 choices (include or exclude)
        # Total combinations = 2^total_unique_digits - 1 (subtracting 1 to exclude the empty set)
        total_numbers = (2 ** total_unique_digits) - 1
        
        return total_numbers