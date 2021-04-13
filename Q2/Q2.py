class Trans():
    def __init__(self):
        self.mat=[]

    def Run(self):
        if len(self.mat)!=0 :
            if len(self.mat)==len(self.mat[0]):
                self.RotSquare()
            else:
                self.RotRectangle()
        else:
            print("The matrix is empty")

    def SetMat(self,mat):
        self.mat=mat

    def GetMat(self):
        return self.mat

    def RotRectangle(self):
        #given M rols and N columns
        #Time complexity: O(M*N)
        #Space complexity: O(M*N)
        oriRols = len(self.mat)
        oriCols = len(self.mat[0])
        revRols = oriRols-1 #reversed rols

        #create a transposed matrix
        newMat=[]
        for row in range(oriCols):
            newMat.append([0]*oriRols)
            
        #start from the last row, and do reversed column-direction iteration
        #if original mat is 2 x 3, so we start from 
        #[1,0]->[0,0]
        #[1,1]->[0,1]
        #[1,2]->[0,2]
        for ind in range(oriCols):
            newCol=0
            for revInd in range(revRols,-1,-1):
                newMat[ind][newCol]=self.mat[revInd][ind]
                newCol+=1
        self.mat=newMat

    def RotSquare(self):
        #Ref: https://leetcode.com/problems/rotate-image/discuss/209450/Python-solution
        #given M rols and N columns
        #Time complexity: O(M*N/4)
        #Space complexity: O(1)
        #I found the above solution is more efficient in terms of time and space complexity.
        # the "~" operator takes the reversed index. So for integers, ~x is equivalent to (-x) - 1.
        # E.g. if index = 0, ~index = -1. If index =1 , ~index= -2. 
        # For instance if we have a 3X3 matrix, each time using "~" to find four coresponding locations and swap them.
        #->(0,0),(0,2),(2,2),(2,0)
        #->(0,1),(1,2),(2,1),(1,0)
        n = len(self.mat)
        rows = n//2
        cols = (n+1)//2
        for i in range(rows):
            for j in range(cols):
                self.mat[i][j], self.mat[j][~i], self.mat[~i][~j], self.mat[~j][i] = self.mat[~j][i], self.mat[i][j], self.mat[j][~i], self.mat[~i][~j]

if __name__ == "__main__":
    
    mat = [ [1, 2, 3, 4, 5, 6, 7],
            [3, 4, 2, 1, 8, 1, 5],
            [2, 1, 6, 3, 2, 2, 1],
            [7, 3, 3, 7, 0, 2, 2]]

    mat1 = [ [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    mat2 = [ [1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10,11,12],
             [13,14,15,16]] 
    mat3 = []
    testCases=[mat,mat1,mat2,mat3]
    trans=Trans()
    for mat in testCases:
        print("ori mat:",mat)
        trans.SetMat(mat)
        trans.Run()
        print(trans.GetMat())


