#assuming col size is the same?
#assuming entrace must be on either side?
from enum import Enum

class Space(Enum):
    EMPTY="O"
    BLOCK="X"

class Cross():
    def Start(self, cars):
        rows = len(cars)
        cols = sum(cars[0])+1
        paths = []
        minNum=float("inf")
        #create a path arr
        for rol in range(rows):
            tmp=[Space.BLOCK.value]*cols
            paths.append(tmp)
        #assign "empty space"
        for row in range(rows):
            for col in range(cols):
                #count "empty space index" for each row
                curRow = cars[row]
                curInd=0
                for ind in range(len(curRow)-1):
                    curInd+=curRow[ind]
                    paths[row][curInd]=Space.EMPTY.value
        
        #get min go through
        #check corner case if no entrance
        for row in range(1):
            for col in range(1,cols-1):
                #check either side(col head,col tail) is "empty"
                curNum=0
                if paths[0][col]==Space.EMPTY.value or paths[rows-1][col]==Space.EMPTY.value:
                    for ind in range(rows):
                        if paths[ind][col]==Space.BLOCK.value:
                            curNum+=1
                    # if curNum!=0:
                    minNum=min(minNum,curNum)
        return minNum

if __name__=="__main__":
    cars=[  [1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [1, 3, 1, 1]]
    cars1=[
        [1,4],
        [3,2],
        [2,2,1],
        [1,2,2]]
    cars2=[
        [1,3,1],
        [1,1,1,2],
        [1,1,2,1],
        [1,2,1,1]]
    cross=Cross()
    minNum=cross.Start(cars)
                