import numpy as np
import sophus as sp
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from enum import Enum
import matplotlib.pyplot as plt

class LGroup(Enum):
    SO3=2
    SE3=3

class LGHandler():
    def SetSE3(self,trans,quat):
        self.quatNormal(quat)
        rotMat=self.from_quaternion(quat)
        lieGroup=sp.SE3(rotMat, trans)
        return lieGroup

    def SetSO3(self,quat):
        self.quatNormal(quat)
        rotMat=self.from_quaternion(quat)
        lieGroup=sp.SO3(rotMat)
        return lieGroup

    def quatNormal(self, quat):
        w,x,y,z= quat
        d=(w**2+x**2+y**2+z**2)**0.5
        for ind in range(len(quat)):
            quat[ind]=quat[ind]/d

    def Interpolate(self, a, b, group):
        #Ref: https://ethaneade.com/lie.pdf page 23
        newx=np.array([])
        newy=np.array([])
        newz=np.array([])
        time=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        for t in time:
            # First consider the group element that takes a to b: b=da
            d= b * a.inverse()
            # find the corresponding lie algebra
            log_d=d.log()
            # Give it a scaler t
            dt=t*log_d
            # Map back to lie group
            if group == LGroup.SE3:
                back=sp.SE3.exp(dt)
            elif group == LGroup.SO3:
                back=sp.SO3.exp(dt)
            #find the interpolated element    
            element=back*a
            newx=np.append(newx,element.matrix()[0][group.value])
            newy=np.append(newy,element.matrix()[1][group.value])
            newz=np.append(newz,element.matrix()[2][group.value])
        return newx,newy,newz

    def from_quaternion(self, quat):
        #Ref: https://github.com/utiasSTARS/liegroups
        #Ref: https://github.com/AndreaCensi/geometry
        qw, qx, qy, qz = quat
        # Form the matrix
        qw2 = qw * qw
        qx2 = qx * qx
        qy2 = qy * qy
        qz2 = qz * qz

        R00 = 1. - 2. * (qy2 + qz2)
        R01 = 2. * (qx * qy - qw * qz)
        R02 = 2. * (qw * qy + qx * qz)
        R10 = 2. * (qw * qz + qx * qy)
        R11 = 1. - 2. * (qx2 + qz2)
        R12 = 2. * (qy * qz - qw * qx)
        R20 = 2. * (qx * qz - qw * qy)
        R21 = 2. * (qw * qx + qy * qz)
        R22 = 1. - 2. * (qx2 + qy2)
        return          (np.array([[R00, R01, R02],
                                [R10, R11, R12],
                                [R20, R21, R22]]))

if __name__=="__main__":
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    # fig2 = plt.figure()

    #set ori path
    ori = fig.gca(projection='3d')
    x=np.array([0.4183,  0.4180])
    y=np.array([-0.4920,-0.4917])
    z=np.array([1.6849,  1.6854])
    ori.plot(x, y, z, label='ori path')
    ori.legend()

    lgHandler=LGHandler()
    #Given providing ranges between a and b
    trans1=np.array([0.4183, -0.4920, 1.6849])
    trans2=np.array([0.4180, -0.4917, 1.6854])
    quat1=[0.5775, -0.8156, 0.0346, -0.0049]
    quat2=[0.5802,-0.8137, 0.0347, -0.0043]
    a=lgHandler.SetSE3(trans1,quat1)
    b=lgHandler.SetSE3(trans2,quat2)

    newx,newy,newz=lgHandler.Interpolate(a,b,LGroup.SE3)
    se3Curve = fig.gca(projection='3d')
    se3Curve.plot(newx, newy, newz, label='SLAM SE3 curve')
    se3Curve.legend()


    # c=lgHandler.SetSO3(quat1)
    # d=lgHandler.SetSO3(quat2)
    # newx,newy,newz=lgHandler.Interpolate(c,d,LGroup.SO3)
    # so3Curve = fig2.gca(projection='3d')
    # so3Curve.plot(newx, newy, newz, label='SLAM SO3 curve')
    # so3Curve.legend()
    plt.show()
