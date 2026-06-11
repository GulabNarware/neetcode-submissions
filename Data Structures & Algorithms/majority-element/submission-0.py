class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}

        for i in nums:
            if i not in count:
                count[i]=1

            else:
                count[i]+=1

        max_ele=count[i]
        element=i

        for j in count:
            if max_ele<count[j]:
                max_ele=count[j]
                element=j

        return element
