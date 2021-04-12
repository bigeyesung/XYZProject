#assuming we have the same car lengths for each row
#assuming entrace(empty space) must be on either side of our going path
#we can't go in front or back of the cars

#Input: 2D array
#Output: integer
#Corner case: empty 2D array
#Corner case: we have only 1 car in each row
from enum import Enum

class Space(Enum):
    EMPTY="O"
    BLOCK="X"

class Cross():
    def Start(self, cars):
        #if not cars
        if not cars:
            return 0

        pathRows = len(cars)
        pathCols = sum(cars[0])+1
        # For each row, at least we need 2 cars to go through
        if len(cars[0])<2:
            return 0
        
        paths = []
        minNum=float("inf")


        #create a path array
        for rol in range(pathRows):
            tmp=[Space.BLOCK.value]*pathCols
            paths.append(tmp)

        #assign "empty space"
        for row in range(pathRows):
            for col in range(pathCols):
                #count "empty space index" for each row
                curRow = cars[row]
                curInd=0
                for ind in range(len(curRow)-1):
                    curInd+=curRow[ind]
                    paths[row][curInd]=Space.EMPTY.value
        
        #get "going through cars" min numbers
        #check corner case if no entrance
        for row in range(1):
            for col in range(1,pathCols-1):
                #check either side(col head,col tail) is "empty"
                curNum=0
                if paths[0][col]==Space.EMPTY.value or paths[pathRows-1][col]==Space.EMPTY.value:
                    for ind in range(pathRows):
                        if paths[ind][col]==Space.BLOCK.value:
                            curNum+=1
                    minNum=min(minNum,curNum)
        return minNum

if __name__=="__main__":
    test1=[ [1, 2, 2, 1],
            [3, 1, 2],
            [1, 3, 2],
            [2, 4],
            [1, 3, 1, 1]]
    test2=[
            [1,4],
            [3,2],
            [2,2,1],
            [1,2,2]]
    test3=[
            [1,3,1],
            [1,1,1,2],
            [1,1,2,1],
            [1,2,1,1]]
    test4=[
            []]
    test5=[
            [1]]
    test6=[
            [1],
            [1]]
    test7=[
            [1,1],
            [2]
    ]
    cross=Cross()
    testCases=[test1,test2,test3,test4,test5,test6,test7]
    for test in testCases:
        minNum=cross.Start(test)
        print(minNum)
                