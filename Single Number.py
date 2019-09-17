class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti = {}
        for i in nums:
            if i in dicti.keys():
                dicti[i]+=1
            else:
                dicti[i]=1
        for (k,v) in dicti.items():
            if v==1:
                return k
        
        return 0
                
        