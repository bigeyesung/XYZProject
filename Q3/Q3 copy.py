import random
import heapq 
from enum import Enum
import numpy as np
x1 = np.array([[1,0,0,0],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]
               ])
x2 = np.array([[1,0,0,3],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]
               ])
x3 = np.array([[1,0,0,4],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]
               ])
xRot=np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])
yRot=np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])
#z turn 90 deg
zRot=np.array([[0,-1,0],
              [1,0,0],
              [0,0,1]])
tmp=np.matmul(yRot,xRot)
rotMat=np.matmul(zRot,tmp)
# x3 = np.array([[1,0,0,4],
#                [0,1,0,0],
#                [0,0,1,0],
#                [0,0,0,1]
#                ])
x4 = np.array([[rotMat[0][0],rotMat[0][1],rotMat[0][2],4],
               [rotMat[1][0],rotMat[1][1],rotMat[1][2],0],
               [rotMat[2][0],rotMat[2][1],rotMat[2][2],0],
               [0,0,0,1]
               ])


# x1 = np.array([[1, 1],
#               [0, 1]])
# x2 = np.array([[4, 1],
#               [2, 2]])
# tmp1=np.multiply(x2, x1)
trans2=np.matmul(x2,x1)
trans3=np.matmul(x3,trans2)
trans4=np.matmul(x4,trans2)
print(trans3)
print(trans4)

dataset=[
[1305031787.1206, 0.4183, -0.4920, 1.6849, -0.8156, 0.0346, -0.0049, 0.5775],
[1305031787.1306, 0.4180, -0.4917, 1.6854, -0.8137, 0.0347, -0.0043, 0.5802],
[1305031787.1406, 0.4176, -0.4922, 1.6860, -0.8133, 0.0353, -0.0049, 0.5807],
[1305031787.1506, 0.4174, -0.4920, 1.6866, -0.8113, 0.0350, -0.0055, 0.5836],
[1305031787.1607, 0.4170, -0.4921, 1.6872, -0.8106, 0.0349, -0.0061, 0.5845],
[1305031787.1707, 0.4166, -0.4920, 1.6878, -0.8082, 0.0353, -0.0068, 0.5878],
[1305031787.1806, 0.4163, -0.4920, 1.6887, -0.8070, 0.0348, -0.0074, 0.5895],
[1305031787.1906, 0.4160, -0.4921, 1.6892, -0.8055, 0.0348, -0.0084, 0.5915],
[1305031787.2006, 0.4156, -0.4920, 1.6900, -0.8032, 0.0350, -0.0094, 0.5946],
[1305031787.2106, 0.4153, -0.4922, 1.6908, -0.8015, 0.0353, -0.0106, 0.5969],
[1305031787.2206, 0.4149, -0.4922, 1.6916, -0.7994, 0.0356, -0.0117, 0.5996],
[1305031787.2306, 0.4145, -0.4921, 1.6923, -0.7975, 0.0360, -0.0128, 0.6021],
[1305031787.2406, 0.4142, -0.4922, 1.6931, -0.7961, 0.0370, -0.0145, 0.6039],
[1305031787.2506, 0.4138, -0.4921, 1.6937, -0.7949, 0.0374, -0.0157, 0.6054],
[1305031787.2606, 0.4136, -0.4921, 1.6945, -0.7937, 0.0377, -0.0174, 0.6069],
[1305031787.2707, 0.4131, -0.4921, 1.6951, -0.7925, 0.0385, -0.0189, 0.6084],
[1305031787.2806, 0.4127, -0.4921, 1.6958, -0.7916, 0.0390, -0.0203, 0.6095],
[1305031787.2907, 0.4124, -0.4919, 1.6965, -0.7901, 0.0393, -0.0218, 0.6114],
[1305031787.3007, 0.4121, -0.4917, 1.6973, -0.7886, 0.0400, -0.0231, 0.6132],
[1305031787.3106, 0.4116, -0.4916, 1.6982, -0.7870, 0.0410, -0.0245, 0.6151],
[1305031787.3206, 0.4113, -0.4914, 1.6989, -0.7848, 0.0417, -0.0256, 0.6178],
[1305031787.3306, 0.4110, -0.4911, 1.6998, -0.7827, 0.0428, -0.0268, 0.6203],
[1305031787.3406, 0.4107, -0.4910, 1.7007, -0.7814, 0.0438, -0.0280, 0.6219],
[1305031787.3506, 0.4105, -0.4906, 1.7015, -0.7796, 0.0455, -0.0293, 0.6240],
[1305031787.3606, 0.4103, -0.4902, 1.7022, -0.7779, 0.0469, -0.0303, 0.6258],
[1305031787.3706, 0.4101, -0.4897, 1.7030, -0.7763, 0.0489, -0.0316, 0.6276],
[1305031787.3807, 0.4099, -0.4893, 1.7036, -0.7754, 0.0511, -0.0327, 0.6286],
[1305031787.3906, 0.4097, -0.4887, 1.7041, -0.7743, 0.0533, -0.0339, 0.6297],
[1305031787.4006, 0.4095, -0.4881, 1.7047, -0.7732, 0.0556, -0.0348, 0.6308],
[1305031787.4106, 0.4093, -0.4875, 1.7051, -0.7721, 0.0577, -0.0356, 0.6319],
[1305031787.4206, 0.4091, -0.4868, 1.7055, -0.7711, 0.0600, -0.0367, 0.6328],
[1305031787.4306, 0.4088, -0.4862, 1.7058, -0.7701, 0.0622, -0.0376, 0.6338],
[1305031787.4406, 0.4086, -0.4854, 1.7060, -0.7690, 0.0643, -0.0383, 0.6349],
[1305031787.4506, 0.4084, -0.4848, 1.7060, -0.7689, 0.0665, -0.0388, 0.6347],
[1305031787.4606, 0.4081, -0.4839, 1.7058, -0.7685, 0.0688, -0.0387, 0.6349],
[1305031787.4706, 0.4079, -0.4833, 1.7055, -0.7697, 0.0706, -0.0390, 0.6333],
[1305031787.4806, 0.4075, -0.4825, 1.7052, -0.7701, 0.0719, -0.0390, 0.6327],
[1305031787.4906, 0.4072, -0.4817, 1.7048, -0.7704, 0.0731, -0.0394, 0.6321],
[1305031787.5006, 0.4068, -0.4809, 1.7042, -0.7707, 0.0741, -0.0395, 0.6316],
[1305031787.5106, 0.4064, -0.4801, 1.7035, -0.7715, 0.0747, -0.0397, 0.6306],
[1305031787.5206, 0.4060, -0.4791, 1.7027, -0.7717, 0.0753, -0.0401, 0.6302],
[1305031787.5306, 0.4056, -0.4783, 1.7018, -0.7726, 0.0755, -0.0402, 0.6291],
[1305031787.5406, 0.4051, -0.4774, 1.7006, -0.7743, 0.0758, -0.0403, 0.6270],
[1305031787.5506, 0.4045, -0.4766, 1.6993, -0.7762, 0.0761, -0.0405, 0.6245],
[1305031787.5607, 0.4042, -0.4753, 1.6978, -0.7772, 0.0762, -0.0406, 0.6233],
[1305031787.5707, 0.4037, -0.4742, 1.6962, -0.7788, 0.0760, -0.0407, 0.6213],
[1305031787.5806, 0.4032, -0.4731, 1.6944, -0.7816, 0.0761, -0.0409, 0.6177],
[1305031787.5906, 0.4028, -0.4720, 1.6923, -0.7844, 0.0767, -0.0415, 0.6142],
[1305031787.6006, 0.4024, -0.4707, 1.6902, -0.7870, 0.0766, -0.0416, 0.6107],
[1305031787.6107, 0.4020, -0.4695, 1.6879, -0.7901, 0.0773, -0.0418, 0.6066],
[1305031787.6206, 0.4016, -0.4683, 1.6853, -0.7945, 0.0776, -0.0415, 0.6008],
[1305031787.6305, 0.4013, -0.4670, 1.6826, -0.7986, 0.0780, -0.0410, 0.5954],
[1305031787.6406, 0.4011, -0.4659, 1.6798, -0.8021, 0.0787, -0.0408, 0.5906],
[1305031787.6505, 0.4007, -0.4644, 1.6769, -0.8053, 0.0789, -0.0398, 0.5862],
[1305031787.6606, 0.4004, -0.4631, 1.6739, -0.8090, 0.0793, -0.0386, 0.5812],
[1305031787.6706, 0.4000, -0.4617, 1.6709, -0.8119, 0.0801, -0.0375, 0.5770],
[1305031787.6806, 0.3996, -0.4603, 1.6677, -0.8153, 0.0805, -0.0361, 0.5723],
[1305031787.6906, 0.3993, -0.4590, 1.6642, -0.8189, 0.0813, -0.0344, 0.5670],
[1305031787.7006, 0.3989, -0.4577, 1.6607, -0.8230, 0.0819, -0.0325, 0.5611],
[1305031787.7106, 0.3987, -0.4564, 1.6569, -0.8274, 0.0825, -0.0309, 0.5547],
[1305031787.7206, 0.3983, -0.4551, 1.6529, -0.8315, 0.0833, -0.0291, 0.5484]]

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
    def GetData(self, sec):
        #trans(x,y,z)
        trans=[dataset[sec][CoordData.TIME.value],dataset[sec][CoordData.X.value],dataset[sec][CoordData.Y.value],dataset[sec][CoordData.Z.value]]
        #quar(w,x,y,z)
        quats = [dataset[sec][CoordData.QW.value],dataset[sec][CoordData.QX.value],dataset[sec][CoordData.QY.value],dataset[sec][CoordData.QZ.value]]
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
        #return traversed meters
        traversed=self.GetTraversed(tran)
        #average feature num
        aveFeatures=self.GetAveProperty(Property.FEATURE.value,featureNums)
        #average matches 
        aveMatches=self.GetAveProperty(Property.MATCH.value,matches)

        #warning signs
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
        # invoking the constructor of parent class  
        MetricSLAM.__init__(self)  
        self.accConfidence=[]

    def SetConfidence(self,aveFeatures, aveMatches):
        #assuming aveNum and aveMatch
        if aveFeatures>=PropData.AVEFEATURE.value and aveMatches>=PropData.AVEMATCH.value:
            self.accConfidence.append(random.uniform(0.5, 1))
        else:
            self.accConfidence.append(random.uniform(0.0, 0.499))

    # def Run(self,trans,quats,featureNum,matches):
    #     return super().Run(trans,quats,featureNum,matches)

    def GetMaxAccConfidence(self):
        # self.accConfidence=[0.5, 0.6, 0.1, 0.7, 0.6, 0.8, 0.9, 0.2, 0.6, 0.1]
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
        return headIdx, tailIdx

class LandmarkSLAM(MetricSLAM):
    def __init__(self):
        # invoking the constructor of parent class  
        MetricSLAM.__init__(self)
        self.module1=[]
        self.module2=[]
        self.module3=[]

    def GetOverlap(self):
        self.module1=[1,8,15,26]
        self.module2=[2,2,7,13]
        self.module3=[4,9,10]
        maxRange=float("inf")
        minNum=1
        maxNum=26
        for num1 in self.module1:
            for num2 in self.module2:
                for num3 in self.module3:
                    tmp=[num1,num2,num3]
                    curRange=max(tmp)-min(tmp)
                    curRange=min(curRange,maxRange)
                    if curRange<maxRange:
                        print("curRange:",curRange)
                        minNum=min(tmp)
                        maxNum=max(tmp)
                        maxRange=curRange
        return minNum,maxNum
    
    def GetOverlap2(self):
        #assuming each module has unique numbers.
        self.module1=[1,8,15,26]
        self.module2=[2,2,7,13]
        self.module3=[4,9,10]
        module1=tuple(self.module1)
        module2=tuple(self.module2)
        module3=tuple(self.module3)

        #while loop(ind:0~):
        # for current index, find out which module has smallest, second smallest and largest number.Save result in "arr"
        # for current arr:
        #   update current range(maxNum-minNum)
        #   if: check 1st smallest module, if the adjacent(next index) number < current largest, index++
        #   elif: check 2nd smallest module,if the adjacent(next index) number < current largest, index++
        #   elif: if the above modules fail, current largest module index++
        #   else:
        moduleIndex = {module1:0,module2:0,module3:0}
        ranges=[]
        minRange=float("inf")
        while(moduleIndex[module1]<len(module1) and moduleIndex[module2]<len(module2) and moduleIndex[module3]<len(module3)):
            heap=[]
            minNum, midNum, maxNum = 0 , 0, 0
            num1=module1[moduleIndex[module1]]
            num2=module2[moduleIndex[module2]]
            num3=module3[moduleIndex[module3]]
            modTable = {num1:module1, num2:module2, num3:module3}
            heapq.heapify(heap)
            heapq.heappush(heap,num1)
            heapq.heappush(heap,num2)
            heapq.heappush(heap,num3)
            print("cur arr",heap)
            minNum=heapq.heappop(heap)
            midNum=heapq.heappop(heap)
            maxNum=heapq.heappop(heap)
            tmp = [minNum,midNum,maxNum]
            ranges.append([maxNum-minNum,tmp])
            smallMod=modTable[minNum]
            largeMod=modTable[maxNum]
            midMod  =modTable[midNum]
            if (moduleIndex[smallMod]+1<len(smallMod) and smallMod[moduleIndex[smallMod]+1]<=maxNum):
                moduleIndex[smallMod]+=1
            elif (moduleIndex[midMod]+1<len(midMod) and midMod[moduleIndex[midMod]+1]<=maxNum):
                moduleIndex[midMod]+=1
            else:
                moduleIndex[largeMod]+=1
        ranges.sort()
        print(ranges[0])

    

if __name__=="__main__":
    simulate = Simulate()
    slam = MetricSLAM()
    toposlam = TopologicalSLAM()
    landslam = LandmarkSLAM()
    sec=0
    while(sec<=20):
        #send data every frame/sec
        tran,quat,featureNums,matches=simulate.GetData(sec)

        #parent slam
        slam.Run(tran,quat,featureNums,matches)
        
        #child slam
        traversed, aveFeatures, aveMatches = toposlam.Run(tran,quat,featureNums,matches)
        toposlam.SetConfidence(aveFeatures, aveMatches)
        toposlam.GetMaxAccConfidence()

        #child slam
        traversed, aveFeatures, aveMatches = landslam.Run(tran,quat,featureNums,matches)
        landslam.GetOverlap()
        landslam.GetOverlap2()
        sec+=1

