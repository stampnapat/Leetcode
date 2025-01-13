class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_list = []
        for num in nums :
            if num != val :
                new_list.append(num)

        while len(new_list) < len(nums):
            new_list.append("_")
        
        
        return new_list
    

nums = [0,1,2,2,3,0,4,2]
val = 2
x = Solution.removeElement("nums",nums,val)
print(x)
