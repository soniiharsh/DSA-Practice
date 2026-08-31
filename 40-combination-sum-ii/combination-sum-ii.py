class Solution(object):
    
    def solve(self, i, candidates, target, ans, temp):
        
        if target == 0 and temp not in ans:
            if temp not in ans:

                 ans.append(temp[:])
                 return
        for j in range(i,len(candidates)):
            if j>i and candidates[j]==candidates[j-1]:
                continue
            if candidates[j]>target:
                break
            temp.append(candidates[j])
            self.solve(j+1,candidates,target-candidates[j],ans,temp)
            temp.pop()
            
    
    
    def combinationSum2(self, candidates, target):
        candidates=sorted(candidates)
        ans = []
        temp = []
        
        self.solve(0, candidates, target, ans, temp)
        
        return ans