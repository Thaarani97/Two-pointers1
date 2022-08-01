#TC :O(n)
#SC :O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        l =0
        r = len(height)-1
        while l<r:
            max_ = max(max_,(min(height[l],height[r])*(r-l)))
            if height[l]< height[r]:
                l=l+1
            else:
                r= r-1
        
        return max_