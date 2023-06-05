class Solution:
    def ContainsDuplicate(self,nums: list[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
            
        return False    
    
    
    
    
    //use hash fuction to solve in O(n) time complexity but space complexity becomes O(n) as well.
         