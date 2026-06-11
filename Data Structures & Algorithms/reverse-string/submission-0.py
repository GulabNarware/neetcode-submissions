class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_pointer=0
        second_pointer=len(s)-1

        while first_pointer<=second_pointer:
            temp=s[first_pointer]
            s[first_pointer]=s[second_pointer]
            s[second_pointer]=temp

            second_pointer-=1
            first_pointer+=1

            
