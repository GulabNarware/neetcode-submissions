class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(nums):

            if len(nums)<=1:
                return nums

            mid=len(nums)//2

            left_arr=nums[:mid]
            right_arr=nums[mid:]

            left=merge_sort(left_arr)
            right=merge_sort(right_arr)

            return merging(left,right)


        def merging(left,right):

            l=0
            r=0
            result=[]

            while l<len(left) and r<len(right):

                if left[l]<=right[r]:
                    result.append(left[l])
                    l+=1

                else:
                    result.append(right[r])
                    r+=1


            if l<len(left):
                result.extend(left[l:])

            if r<len(right):
                result.extend(right[r:])

            return result
        return merge_sort(nums)
