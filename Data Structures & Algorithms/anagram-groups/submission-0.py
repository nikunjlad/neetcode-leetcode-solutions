class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # we create a hashmap which is a dictionary of lists
        hashmap = defaultdict(list)

        # loop over each string in the array and create a dictionary
        for string in strs:
            count = [0] * 26        # a count array which holds 26 characters
            for char in string:
                count[ord(char) - ord('a')] += 1
            
            hashmap[tuple(count)].append(string)

        return list(hashmap.values())
