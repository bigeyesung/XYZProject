#conda install pybind11 pybind11-abi pybind11-global
#pip install sophuspy

import numpy as np
import sophus as sp
import unittest
import pytest
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# quatNormal(quat)
# rotMat=rotation_from_quaternion(quat)
# rotMat2=quaternion_rotation_matrix(quat)
# rotMat3=from_quaternion(quat)
# 1. default constructor of SO3
# quatNormal(quat1)
# quatNormal(quat2)
# rotMat1=from_quaternion(quat1)
# rotMat2=from_quaternion(quat2)
# a=sp.SE3(rotMat1, trans1)
# b=sp.SE3(rotMat2, trans2)

class LGHandler():
    def SetSE3(self,trans,quat):
        self.quatNormal(quat)
        rotMat=self.from_quaternion(quat)
        lieGroup=sp.SE3(rotMat, trans)
        return lieGroup

    def quatNormal(self, quat):
        w,x,y,z= quat
        d=(w**2+x**2+y**2+z**2)**0.5
        for ind in range(len(quat)):
            quat[ind]=quat[ind]/d

    def Interpolate(self,a,b):
        #Ref: https://ethaneade.com/lie.pdf page 23
        newx=np.array([])
        newy=np.array([])
        newz=np.array([])
        time=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
        for t in time:
            a_inv=a.inverse()
            d=b * a_inv
            log_d=d.log()
            dt=t*log_d
            back=sp.SE3.exp(dt)
            mid=back*a
            newx=np.append(newx,mid.matrix()[0][3])
            newy=np.append(newy,mid.matrix()[1][3])
            newz=np.append(newz,mid.matrix()[2][3])
        return newx,newy,newz
    def from_quaternion(self, quat, ordering='wxyz'):
        #Ref: https://github.com/utiasSTARS/liegroups
        #Ref: https://github.com/AndreaCensi/geometry
        if not np.isclose(np.linalg.norm(quat), 1.):
            raise ValueError("Quaternion must be unit length")
        if ordering is 'xyzw':
            qx, qy, qz, qw = quat
        elif ordering is 'wxyz':
            qw, qx, qy, qz = quat
        else:
            raise ValueError(
                "Valid orderings are 'xyzw' and 'wxyz'. Got '{}'.".format(ordering))
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
    #set ori path
    aori = fig.gca(projection='3d')
    x=np.array([0.4183,  0.4180])
    y=np.array([-0.4920,-0.4917])
    z=np.array([1.6849,  1.6854])
    aori.plot(x, y, z, label='ori path')
    aori.legend()

    lgHandler=LGHandler()
    trans1=np.array([0.4183, -0.4920, 1.6849])
    trans2=np.array([0.4180, -0.4917, 1.6854])
    quat1=[0.5775, -0.8156, 0.0346, -0.0049]
    quat2=[0.5802,-0.8137, 0.0347, -0.0043]
    a=lgHandler.SetSE3(trans1,quat1)
    b=lgHandler.SetSE3(trans2,quat2)
    newx,newy,newz=lgHandler.Interpolate(a,b)
    ax = fig.gca(projection='3d')
    ax.plot(newx, newy, newz, label='SLAM curve')
    ax.legend()
    plt.show()
