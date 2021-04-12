import random
import heapq 
import collections
from enum import Enum
import numpy as np

class CoordData(Enum):
    TIME=0
    X=1
    Y=2
    Z=3
    QX=4
    QY=5
    QZ=6
    QW=7

class Property(Enum):
    FEATURE=0
    MATCH=1

class PropData(Enum):
    AVEFEATURE=5.48
    AVEMATCH=51.2
    ACCRANGE=5

class Simulate():
    def __init__(self):
        self.dataset=[]
        
    def ReadFile(self, input):
        try:
            with open(input) as f:
                lines = f.readlines()
                for ind in range(3,len(lines)):
                    line=lines[ind].strip().split(" ")
                    for ind in range(len(line)):
                        line[ind]=float(line[ind])
                    self.dataset.append(line)
                f.close()
            return True
        except:
            print("file can't be opened")
            return False
    def GetData(self, sec):
        #trans(x,y,z)
        trans=[self.dataset[sec][CoordData.TIME.value],self.dataset[sec][CoordData.X.value],self.dataset[sec][CoordData.Y.value],self.dataset[sec][CoordData.Z.value]]
        #quar(w,x,y,z)
        quats = [self.dataset[sec][CoordData.QW.value],self.dataset[sec][CoordData.QX.value],self.dataset[sec][CoordData.QY.value],self.dataset[sec][CoordData.QZ.value]]
        #feature
        featureNum = random.randint(0, 10)
        #match
        matches = random.randint(0, 100)
        return trans,quats,featureNum,matches

class MetricSLAM():
    def __init__(self):
        # self.camera = np.array([[1,0,0,0],
        #                         [0,1,0,0],
        #                         [0,0,1,0],
        #                         [0,0,0,1]
        #                         ])
        self.curPos=[0,0,0]
        self.traversed=0
        self.maxSizeMem=5
        self.minFeature=5
        self.maxFeature=10
        self.features=[]
        # self.featuresTotal=0
        self.matches=[]
        self.totals=[0,0]
        # self.matchesTotal=0
        #limit memory-> using queue

    def Run(self,tran,quat,featureNums,matches):
        traversed=self.GetTraversed(tran)
        aveFeatures=self.GetAveProperty(Property.FEATURE.value,featureNums)
        aveMatches=self.GetAveProperty(Property.MATCH.value,matches)

        #Print data
        print("traversed:",traversed)
        print("aveFeatures:",aveFeatures)
        print("aveMatches:",aveMatches)
        self.GetWarning(aveFeatures)
        print("===end=====")
        return traversed, aveFeatures, aveMatches

    def GetWarning(self, aveFeatures):
        if aveFeatures<=self.minFeature:
            print("suggesting poor lighting conditions")
        elif aveFeatures>=self.maxFeature:
            print("suggesting over exposure")

    def GetTraversed(self, trans):
        x=self.curPos[0]-trans[CoordData.X.value]
        y=self.curPos[1]-trans[CoordData.Y.value]
        z=self.curPos[2]-trans[CoordData.Z.value]
        self.traversed+=(x**2+y**2+z**2)**0.5
        self.curPos=trans[1:]
        return self.traversed

    # def GetCurPos2(self, trans):
    #     deltaX=trans[CoordData.X.value]-self.camera[0][3]
    #     deltaY=trans[CoordData.Y.value]-self.camera[1][3]
    #     deltaZ=trans[CoordData.Z.value]-self.camera[2][3]
    #     transMat = np.array([[1,0,0,deltaX],
    #                          [0,1,0,deltaY],
    #                          [0,0,1,deltaZ],
    #                          [0,0,0,1]
    #                         ])
    #     self.camera=np.matmul(transMat,self.camera)

    def GetAveProperty(self, property, newData):
        container=self.features
        # totalVal=self.totals[Property.FEATURE.value]

        if property==Property.MATCH.value:
            container=self.matches
            self.totals[property]=self.totals[Property.MATCH.value]

        if len(container)<self.maxSizeMem:
            container.append(newData)
            self.totals[property]+=newData
            return self.totals[property]/len(container)
        #if size == max mem -> remoeve the head, recalculate 
        else:
            self.totals[property]=self.totals[property]-container[0]+newData
            container.pop(0)
            container.append(newData)
            return self.totals[property]/self.maxSizeMem


    # def GetAveFeatures(self, featureNums):
    #     if len(self.features)<self.maxSizeMem:
    #         self.features.append(featureNums)
    #         self.featuresTotal+=featureNums
    #         return self.featuresTotal/len(self.features)
    #     #if size == max mem -> remoeve the head, recalculate 
    #     else:
    #         self.featuresTotal=self.featuresTotal-self.features[0]+featureNums
    #         self.features.pop(0)
    #         self.features.append(featureNums)
    #         return self.featuresTotal/self.maxSizeMem

    # def GetAveMatches(self, matches):
    #     if len(self.matches)<self.maxSizeMem:
    #         self.matches.append(matches)
    #         self.matchesTotal+=self.matches
    #         return self.featuresTotal//len(self.matches)
    #     #if size == max mem -> remoeve the head, recalculate 
    #     else:
    #         self.matchesTotal=self.matchesTotal-self.matches[0]+matches
    #         self.matches.pop(0)
    #         self.matches.append(matches)
    #         return self.matchesTotal//self.maxSizeMem

class TopologicalSLAM(MetricSLAM):
    def __init__(self):
        MetricSLAM.__init__(self)  
        self.accConfidence=[]

    def SetConfidence(self,aveFeatures, aveMatches):
        #assuming aveNum and aveMatch
        if aveFeatures>=PropData.AVEFEATURE.value and aveMatches>=PropData.AVEMATCH.value:
            self.accConfidence.append(random.uniform(0.5, 1))
        else:
            self.accConfidence.append(random.uniform(0.0, 0.499))

    def GetMaxAccConfidence(self):
        headIdx=0
        curRange=PropData.ACCRANGE.value-1

        curConf = sum(self.accConfidence[headIdx:PropData.ACCRANGE.value])
        maxConf = curConf
        for ind in range(1,len(self.accConfidence)-curRange):
            curConf=curConf-self.accConfidence[ind-1]+self.accConfidence[ind+curRange]
            if curConf>maxConf:
                print("curConf:",curConf)
                headIdx=ind
                maxConf=curConf
        # print(headIdx)
        # print(headIdx+curRange)
        if len(self.accConfidence)<PropData.ACCRANGE.value:
            tailIdx=len(self.accConfidence)-1
        else:
            tailIdx=headIdx+curRange
        print("Current confidence:",curConf)
        print("Max confidence:",maxConf)
        print("Max confidence start frame:  %s end frame: %s" % (headIdx, tailIdx))
        return headIdx, tailIdx

class LandmarkSLAM(MetricSLAM):
    def __init__(self):

        MetricSLAM.__init__(self)
        self.module1=[]
        self.module2=[]
        self.module3=[]
        self.maxNum=0
        self.minNum=0

    def GetOverlap(self):
        minNum=0
        maxNum=0
        print("module1:",self.module1)
        print("module2:",self.module2)
        print("module3:",self.module3)
        if self.module1 and self.module2 and self.module3:
            minRange=self.maxNum-self.minNum
            for land1 in self.module1:
                for land2 in self.module2:
                    for land3 in self.module3:
                        visited=[land1,land2,land3]
                        curRange=max(visited)-min(visited)
                        # curRange=min(curRange,minRange)
                        if curRange<minRange:
                            # print("curRange:",curRange)
                            # print("minRange",minRange)
                            minNum=min(visited)
                            maxNum=max(visited)
                            minRange=curRange
            print("minRange:",minRange)
            print("minRange start:  %d end: %d" % (minNum, maxNum))
            return minNum, maxNum
        else:
            print("not enough visited landmarks")
    
    def GetOverlap_v2(self):
        if self.module1 and self.module2 and self.module3:
            #while loop:
                # for current index, find out which module has smallest, second smallest and largest number.Save result in "arr"
                # for current arr:
                #   update current range(maxNum-minNum)
                #   if: check 1st smallest module, if the adjacent(next index) number < current largest, index++
                #   elif: check 2nd smallest module,if the adjacent(next index) number < current largest, index++
                #   elif: if the above modules fail, current largest module index++
            module1=tuple(self.module1)
            module2=tuple(self.module2)
            module3=tuple(self.module3)
            moduleIndex = {module1:0,module2:0,module3:0}
            ranges=collections.defaultdict(list)
            minRange=self.maxNum-self.minNum
            while(moduleIndex[module1]<len(module1) and moduleIndex[module2]<len(module2) and moduleIndex[module3]<len(module3)):
                heap=[]
                minNum, midNum, maxNum = 0, 0, 0

                #get numbers(visited landmarks) from each module
                num1=module1[moduleIndex[module1]]
                num2=module2[moduleIndex[module2]]
                num3=module3[moduleIndex[module3]]
                modTable = {num1:module1, num2:module2, num3:module3}

                #Sort the current vistied landmarks. 
                #Using heap to avoid computation when data is too large(future)
                heapq.heapify(heap)
                heapq.heappush(heap,num1)
                heapq.heappush(heap,num2)
                heapq.heappush(heap,num3)
                minNum=heapq.heappop(heap)
                midNum=heapq.heappop(heap)
                maxNum=heapq.heappop(heap)
                visited = [minNum,midNum,maxNum]
                curRange=maxNum-minNum
                # Check if two or more ranges have the same size-> choose smaller integers
                if ranges.get(curRange)!=None:
                    curNum=ranges[curRange][0]
                    if minNum<curNum:
                        ranges[curRange]=visited
                else:
                    ranges[curRange].extend(visited)
                # ranges.append([curRange,visited])
                if curRange<minRange:
                    minRange=curRange
                smallMod=modTable[minNum]
                largeMod=modTable[maxNum]
                midMod  =modTable[midNum]
                if (moduleIndex[smallMod]+1<len(smallMod) and smallMod[moduleIndex[smallMod]+1]<=maxNum):
                    moduleIndex[smallMod]+=1
                elif (moduleIndex[midMod]+1<len(midMod) and midMod[moduleIndex[midMod]+1]<=maxNum):
                    moduleIndex[midMod]+=1
                else:
                    moduleIndex[largeMod]+=1
            print("minRange:",minRange)
            print("minRange start:  %d end: %d" % (ranges[minRange][0], ranges[minRange][2]))
        else:
            print("not enough visited landmarks")

    def SetLandmarks(self):
        #remove cache
        self.module1.clear()
        self.module2.clear()
        self.module3.clear()

        #given a random number
        marksSet=set(np.random.randint(100, size=(10)))
        marksArr=list(marksSet)
        marksArr.sort()
        if len(marksArr)!=0:
            self.maxNum=marksArr[-1]
            self.minNum=marksArr[0]
            while marksArr:
                self.module1.append(marksArr.pop(0))
                if marksArr:
                    self.module2.append(marksArr.pop(0))
                if marksArr:
                    self.module3.append(marksArr.pop(0))

        # self.module1= [1, 11, 67, 88]
        # self.module2= [6, 55, 70]
        # self.module3= [9, 58, 74]
        # self.maxNum=88
        # self.minNum=1


if __name__=="__main__":

    simulate = Simulate()
    slam = MetricSLAM()
    toposlam = TopologicalSLAM()
    landslam = LandmarkSLAM()
    if (simulate.ReadFile("Input/groundtruth.txt")):
        sec=0
        while(sec<=20):
            #send data every sec
            tran,quat,featureNums,matches=simulate.GetData(sec)

            print("SLAM")
            slam.Run(tran,quat,featureNums,matches)
            
            print("Topological SLAM")
            traversed, aveFeatures, aveMatches = toposlam.Run(tran,quat,featureNums,matches)
            toposlam.SetConfidence(aveFeatures, aveMatches)
            toposlam.GetMaxAccConfidence()

            print("Landmarks SLAM")
            traversed, aveFeatures, aveMatches = landslam.Run(tran,quat,featureNums,matches)
            landslam.SetLandmarks()
            landslam.GetOverlap()
            #test function
            landslam.GetOverlap_v2()
            sec+=1

