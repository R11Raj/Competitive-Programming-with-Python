class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count=0
        
        self.seen=set()
        
        def dfs(student):
            for i in range(len(M)):
                if M[student][i] and i not in self.seen:
                    self.seen.add(i)
                    dfs(i)
            
            
        
        for i in range(len(M)):
            if i not in self.seen:
                count+=1
                self.seen.add(i)
                dfs(i)
        
        return count
