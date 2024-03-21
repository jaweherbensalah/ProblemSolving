"""
Description
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.
"""


class NestedInteger(object):
    def __init__(self, value=None, nested_list=None):
        self.value = value
        self.nested_list = nested_list
        
    def isInteger(self):
        """ returns true if this NestedInteger holds a single integer 
        rather than a nested list
        :rtype boolean"""

        return self.value is not None
    
    def getInteger(self):
        """ returns the single integer that this NestedInteger holds,
         if it holds a single integer
          
        returns None if this nestedInteger holds a nested list 
        
        :rtype int"""

        return self.value if self.isInteger() else None
    
    def getList(self):
        """ returns the nested list that this NestedInteger holds,
         if it holds a nested list

        returns None if this nestedInteger holds a single integer
        
        :rtype List[NestedInteger]"""

        return self.nested_list if not self.isInteger() else None


class Solution():
    def depthSum(self,nestedList ):
        """
        :type nestedList: List[NestedInteger]
        :rtype int
        """

        return self.depthSum_helper(nestedList,1)
    

    def depthSum_helper(self, nested_list,depth):
        if len(nested_list)==0 or nested_list==None:
            return 0
        else:
            sum=0
            for e in nested_list:
                if e.isInteger():
                    sum+=e.getInteger()*depth
                else:
                    sum+=self.depthSum_helper(e.getList(),depth+1)
        return sum


        

nl=[NestedInteger([[1,1],2,[1,1]])]
s=Solution()
res=s.depthSum(nl)
print(res)

#***************************************************************************************
            #Second approach
#***************************************************************************************
def depthSum(nestedList):
    def dfs(nested_list, depth):
        total_sum = 0
        for element in nested_list:
            if isinstance(element, int):
                total_sum += element * depth
            else:
                total_sum += dfs(element, depth + 1)
        return total_sum

    return dfs(nestedList, 1)


nl = [1, [2, 3], [4, [5, 6]]]
# nl=[[1,1],2,[1,1]]

result = depthSum(nl)
print(result)
