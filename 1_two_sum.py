##### optimal #######3


class Solution(object):
    
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [i,dic[nums[i]]]
            else:
                dic[target-nums[i]] = i            
        
#################   MY approach   ############
'''
import copy
class Solution(object):
    def bsearch(self,start,end,arr,ele):
        if(start>end):
            return -1
        else:
            mid = start+((end-start)//2)   #last included
            if arr[mid]==ele:
                return mid
            elif ele>arr[mid]:
                return self.bsearch(mid+1,end,arr,ele)
            else:
                return self.bsearch(start,mid-1,arr,ele)
        
    
    def twoSum(self, nums, target):
        a = copy.copy(nums)
        nums.sort()
        for i in range(len(nums)):
            array = nums[i+1:]
            #print(array)
            dest = target-nums[i]
            get = self.bsearch(0,len(array)-1,array,dest)
            if(get!=-1):
                if(a[a.index(nums[i])] == a[a.index(nums[get+1+i])]):
                    ans = [a.index(nums[i])]
                    a.remove(a[a.index(nums[i])])
                    ans.append(a.index(nums[get+1+i])+1)
                    return ans
                else:
                    return [a.index(nums[i]),a.index(nums[get+1+i])]
'''
            
            
        
