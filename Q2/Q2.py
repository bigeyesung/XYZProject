
class Trans():
    def Rotate(self, mat):
        #get rol,col
        #create transformed mat,
        #for each row, reverse it
        rols = len(mat)
        cols = len(mat[0])
        newMat=[]
        for row in range(cols):
            tmp=[0]*rols
            newMat.append(tmp)
        
        for row in range(len(newMat)):
            for col in range(len(newMat[0])):
                newMat[row][col]=mat[col][row]

        for row in range(len(newMat)):
            newMat[row].reverse()

        return newMat
if __name__ == "__main__":
    trans = Trans()
    mat = [ [1, 2, 3, 4, 5, 6, 7],
        [3, 4, 2, 1, 8, 1, 5],
        [2, 1, 6, 3, 2, 2, 1],
        [7, 3, 3, 7, 0, 2, 2]]
    newMat=trans.Rotate(mat)
    print(newMat)
