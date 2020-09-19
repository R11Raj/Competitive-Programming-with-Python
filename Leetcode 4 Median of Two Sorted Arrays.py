class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        
        n=n1+n2
        
        mid = n//2 + 1
        
        i=0
        j=0
        
        merged=[]
        
        while mid>0:
            
            if i>=n1:
                merged.append(nums2[j])
                j+=1
            elif j>=n2:
                merged.append(nums1[i])
                i+=1
            elif nums1[i]<=nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
            mid-=1
        
        if n%2==0:
            return (merged[-1]+merged[-2])/2
        
        return float(merged[-1])
