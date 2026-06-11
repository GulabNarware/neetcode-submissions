class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        n=0
        for i in nums:
            n+=i
            self.prefix.append(n)

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.prefix[right]

        if left==0:
            return self.prefix[right]
        elif left >0:
            leftsum=self.prefix[left-1]
        else:
            leftsum=self.prefix[left]
        return rightsum-leftsum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)