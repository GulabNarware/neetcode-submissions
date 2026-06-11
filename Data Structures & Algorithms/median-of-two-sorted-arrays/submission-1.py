class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left,right=0,len(nums1)-1
        left1,right1=0,len(nums2)-1

        num=nums1+nums2
        num1=sorted(num)
        l=0
        r=len(num1)-1

        if (l+r)%2== 0:
            return float(num1[(l+r)//2])
        else:
            a=(l+r)//2
            b=math.ceil((l+r)/2)
            return float((num1[a]+num1[b])/2)
