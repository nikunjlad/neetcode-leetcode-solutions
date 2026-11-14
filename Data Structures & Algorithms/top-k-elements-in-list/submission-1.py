class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # initialize a counter to hold frequency of elements
        num_counter = Counter()

        # the counter holds the count of frequent elements
        for num in nums:
            num_counter[num] += 1

        # define a heapq
        heap = []
        for num in num_counter.keys():
            heapq.heappush(heap, (num_counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        

        
            
        return k_frequent
