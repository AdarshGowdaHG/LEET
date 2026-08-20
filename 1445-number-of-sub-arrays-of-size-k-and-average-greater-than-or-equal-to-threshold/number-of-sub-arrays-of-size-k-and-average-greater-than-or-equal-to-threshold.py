class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        target_sum = threshold * k
        count = 1 if current_sum >= target_sum else 0
        
        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum >= target_sum:
                count += 1
                
        return count