class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        t1,t2=self.shape(grid)
        #print(self.shape(grid))
        p=0
        for k in range(t1):
        	for t in range(t2):
        		if grid[k][t] == 1:
        			a=self.calaround(grid,k,t)
        			p=p+a
        return p
    def shape(self,grid):
    	return len(grid),len(grid[0])
    def calaround(self,grid,x,y):
    	q=0
    	if x>0:
    		if grid[x-1][y]==1:
    			q=q+1
    	if x<self.shape(grid)[0]-1:
    		if grid[x+1][y]==1:
    			q=q+1
    	if y>0:
    		if grid[x][y-1]==1:
    			q=q+1
    	if y<self.shape(grid)[1]-1:
    		if grid[x][y+1]==1:
    			q=q+1
    	return 4-q
# s=Solution()
# t=s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
# print(t)