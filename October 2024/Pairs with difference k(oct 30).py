from collections import Counter

class Solution:
    def countPairsWithDiffK(self, arr, k):
        # Frequency dictionary to count occurrences of each element
        freq = Counter(arr)
        count = 0

        # Traverse each unique element in the frequency dictionary
        for num in freq:
            
            if num + k in freq:
                count += freq[num] * freq[num + k]
            if num - k in freq and k != 0:
                count += freq[num] * freq[num - k]

        return count // 2
