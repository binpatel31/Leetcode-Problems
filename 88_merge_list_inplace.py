class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i=m+n-1
        j=n-1
        cur=m-1
        while(cur>=0 and j>=0):
            if nums2[j] >= nums1[cur]:
                nums1[i] = nums2[j]
                j-=1
                i-=1
            else:
                nums1[i] = nums1[cur]
                cur-=1
                i-=1
        if(cur<0):
            while(j>=0):
                nums1[i] = nums2[j]
                i-=1
                j-=1
        else:
            while(cur>=0):
                nums1[i] = nums1[cur]
                i-=1
                cur-=1
        print(nums1)
            
                
            
            
            
            
            
        
