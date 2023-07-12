class Solution(object):
    def removeElement(self, nums, val):
        """
        Removes all occurrences of `val` in the given `nums` list in-place.
        Returns the number of elements in `nums` which are not equal to `val`.
        
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # List comprehension to filter out elements equal to `val`
        nums[:] = [x for x in nums if x != val]

        return len(nums)
