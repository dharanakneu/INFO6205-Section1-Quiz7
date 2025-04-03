from typing import List

class MSDSortBasic:
    """
    Basic implementation of MSD (Most Significant Digit) sorting for strings.
    
    This implementation focuses on the key-indexed counting aspect of MSD sort
    by sorting strings based on a single character position.
    It's a simplified version that demonstrates the counting technique without recursion.
    """
    
    # ASCII range
    R = 256
    
    def __init__(self):
        """Initialize a new MSDSortBasic instance."""
        self.accesses = 0
    
    def _char_at(self, s: str, d: int) -> int:
        """
        Get the character at position d in string s, or -1 if d is past the end.
        
        Args:
            s: The string to examine
            d: The position to check
            
        Returns:
            The integer value of the character at position d, or -1 if d >= len(s)
        """
        self.accesses += 1
        if d < len(s):
            return ord(s[d])
        return -1
    
    def sort_by_position(self, arr: List[str], d: int) -> None:
        """
        Sort the array of strings based on the character at position d.
        
        Args:
            arr: The array of strings to sort
            d: The character position to sort by (0-indexed)
        """
        n = len(arr)
        if n <= 1:
            return

        # 1. Count frequency of each character at position d
        count = [0] * (self.R + 2)

        for s in arr:
            char_index = self._char_at(s, d) + 2
            count[char_index] += 1

        #2. Compute cumulative counts to determine positions
        for r in range(len(count) - 1):
                count[r + 1] += count[r]

        # 3. Distribute strings to auxiliary array
        aux = [None] * n
        for s in arr:
            char_index = self._char_at(s, d) + 1
            aux[count[char_index]] = s
            count[char_index] += 1
        
        # 4. Copy back to original array
        for i in range(n):
                arr[i] = aux[i]

    
    def is_sorted_by_position(self, arr: List[str], d: int) -> bool:
        """
        Check if the array is sorted by the character at position d.
        
        Args:
            arr: The array to check
            d: The position to check
            
        Returns:
            True if the array is sorted by position d, False otherwise
        """
        for i in range(1, len(arr)):
            if self._char_at(arr[i], d) < self._char_at(arr[i-1], d):
                return False
        return True