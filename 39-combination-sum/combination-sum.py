class Solution(object):
    
    def solve(self, i, candidates, target, ans, temp):
        
        # base case
        if i == len(candidates):
            if target == 0:
                ans.append(temp[:])
            return
        
        
        # TAKE
        if candidates[i] <= target:
            temp.append(candidates[i])
            
            self.solve(
                i,candidates,target - candidates[i],ans,temp
            )
            temp.pop()
        
        
        # NOT TAKE
        self.solve(
            i + 1,
            candidates,
            target,
            ans,
            temp
        )
    
    
    def combinationSum(self, candidates, target):
        
        ans = []
        temp = []
        
        self.solve(0, candidates, target, ans, temp)
        
        return ans