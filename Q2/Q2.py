class Trans():
    def __init__(self, mat):
        self.mat=mat

    def Run(self):
        if len(self.mat)!=0 :
            if len(self.mat)==len(self.mat[0]):
                self.RotateSquare()
            else:
                self.Rotate()
        print("ok")

    def GetMat(self):
        return self.mat
    # def Rotate(self, mat):
    #     #get rol,col
    #     #create transformed mat,
    #     #for each row, reverse it
    #     rols = len(mat)
    #     cols = len(mat[0])
    #     newMat=[]
    #     for row in range(cols):
    #         tmp=[0]*rols
    #         newMat.append(tmp)
        
    #     for row in range(len(newMat)):
    #         for col in range(len(newMat[0])):
    #             newMat[row][col]=mat[col][row]

    #     for row in range(len(newMat)):
    #         newMat[row].reverse()

    #     return newMat
    def Rotate(self):
        #given M means rol size and N means column size
        #Time complexity: O(M*N)
        #Space complexity: O(M*N)
        oriRols = len(self.mat)
        oriCols = len(self.mat[0])
        revRols = oriRols-1 #reversed rols

        #create transposed matrix
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

    def RotateSquare(self):
        #given M means rol size and N means column size
        #Time complexity: O(M*N/4)
        #Space complexity: O(1)
        #need more explain !!!!!!!!!!!!!
        n = len(self.mat)
        rows = n//2
        cols = (n+1)//2
        for i in range(rows):
            for j in range(cols):
                tmp0=self.mat[i][j]
                print("~i: ",~i)
                print("~j: ",~j)
                tmp1=self.mat[j][~i]
                tmp2=self.mat[~i][~j]
                tmp3=self.mat[~j][i]
                print("mat[i][j]",self.mat[i][j])
                print("mat[j][~i]",self.mat[j][~i])
                print("mat[~i][~j]",self.mat[~i][~j])
                print("mat[~j][i]",self.mat[~j][i])
                self.mat[i][j], self.mat[j][~i], self.mat[~i][~j], self.mat[~j][i] = self.mat[~j][i], self.mat[i][j], self.mat[j][~i], self.mat[~i][~j]
if __name__ == "__main__":
    
    mat = [ [1, 2, 3, 4, 5, 6, 7],
            [3, 4, 2, 1, 8, 1, 5],
            [2, 1, 6, 3, 2, 2, 1],
            [7, 3, 3, 7, 0, 2, 2]]
    mat1 = [ [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    trans = Trans(mat)
    trans1 = Trans(mat1)
    trans.Run()
    trans1.Run()
    print(trans.GetMat())
    print(trans1.GetMat())

