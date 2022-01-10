class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # IDEA: for each word, find its sorted string format, and store it in a hashtable with the sorted string as
        # key and the anagram group as the value. 
        
        # TIME: if K is the max length of string, O(NKlogK). N pass and K log K for sorting string
        # SPACE: O(NK)

        dic = {}
        res = []
        i = 0
        while i < len(strs):
            word = strs[i]
            sorted_word = "".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)
            
            i+=1
            
        for key, value in dic.items():
            res.append(value)
        
        return res
        
