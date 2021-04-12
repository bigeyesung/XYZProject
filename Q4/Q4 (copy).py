#conda install pybind11 pybind11-abi pybind11-global
#pip install sophuspy

import numpy as np
import sophus as sp
import unittest
import pytest
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
aori = fig.gca(projection='3d')


# timestamp tx ty tz qx qy qz qw
arr=[1305031787.1206, 0.4183, -0.4920, 1.6849 -0.8156, 0.0346, -0.0049, 0.5775]
quat=[0.5775, -0.8156, 0.0346, -0.0049]

x=np.array([
0.4183,
0.4180
])

y=np.array([
-0.4920,
-0.4917
])

z=np.array([
1.6849,
1.6854
])

aori.plot(x, y, z, label='ori path')
aori.legend()

# def rotation_from_quaternion(x):
#     """
#         Converts a quaternion to a rotation matrix.
#     """
#     # Documented in <http://en.wikipedia.org/w/index.php?title=
#     # Quaternions_and_spatial_rotation&oldid=402924915>
#     #w x y z
#     a, b, c, d = x

#     r1 = [a ** 2 + b ** 2 - c ** 2 - d ** 2, 2 * b * c - 2 * a * d, 2 * b * d + 2 * a * c]
#     r2 = [2 * b * c + 2 * a * d, a ** 2 - b ** 2 + c ** 2 - d ** 2, 2 * c * d - 2 * a * b]
#     r3 = [2 * b * d - 2 * a * c, 2 * c * d + 2 * a * b, a ** 2 - b ** 2 - c ** 2 + d ** 2]

#     return np.array([r1, r2, r3])

#Q: w,x,y,z
# def quaternion_rotation_matrix(Q):
#     """
#     Covert a quaternion into a full three-dimensional rotation matrix.
 
#     Input
#     :param Q: A 4 element array representing the quaternion (q0,q1,q2,q3) 
 
#     Output
#     :return: A 3x3 element matrix representing the full 3D rotation matrix. 
#              This rotation matrix converts a point in the local reference 
#              frame to a point in the global reference frame.
#     """
#     # Extract the values from Q
#     q0 = Q[0]
#     q1 = Q[1]
#     q2 = Q[2]
#     q3 = Q[3]
     
#     # First row of the rotation matrix
#     r00 = 2 * (q0 * q0 + q1 * q1) - 1
#     r01 = 2 * (q1 * q2 - q0 * q3)
#     r02 = 2 * (q1 * q3 + q0 * q2)
     
#     # Second row of the rotation matrix
#     r10 = 2 * (q1 * q2 + q0 * q3)
#     r11 = 2 * (q0 * q0 + q2 * q2) - 1
#     r12 = 2 * (q2 * q3 - q0 * q1)
     
#     # Third row of the rotation matrix
#     r20 = 2 * (q1 * q3 - q0 * q2)
#     r21 = 2 * (q2 * q3 + q0 * q1)
#     r22 = 2 * (q0 * q0 + q3 * q3) - 1
     
#     # 3x3 rotation matrix
#     rot_matrix = np.array([[r00, r01, r02],
#                            [r10, r11, r12],
#                            [r20, r21, r22]])
                            
#     return rot_matrix

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

ax = fig.gca(projection='3d')
ax.plot(newx, newy, newz, label='SLAM curve')
ax.legend()

plt.show()

class LGHandler():
    def SetSE3(self,trans,quat):
        self.quatNormal(quat)
        rotMat=from_quaternion(quat)
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
            b_mat = b.matrix()
            ainv_mat = a_inv.matrix()
            log_d=d.log()
            dt=t*log_d
            back=sp.SE3.exp(dt)
            mid=back*a
            newx=np.append(newx,mid.matrix()[0][3])
            newy=np.append(newy,mid.matrix()[1][3])
            newz=np.append(newz,mid.matrix()[2][3])

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
    lgHandler=LGHandler()
    trans1=np.array([0.4183, -0.4920, 1.6849])
    trans2=np.array([0.4180, -0.4917, 1.6854])
    quat1=[0.5775, -0.8156, 0.0346, -0.0049]
    quat2=[0.5802,-0.8137, 0.0347, -0.0043]
    a=lgHandler.SetSE3(trans1,quat1)
# R = sp.SO3([[0, 1, 0],
#             [0, 0, 1],
#             [1, 0, 0]])
# T = sp.SE3(R.matrix(), np.ones(3))
# pt = np.array([1, 2, 3])


# Rnp = np.array([[-0.02495988040066277, 0.01720436961811805,   0.9995404014027787],
#                 [ 0.06813350186490005,   0.997556284701166, -0.01546883243273596],
#                 [ -0.9973639407428014, 0.06771608759556018, -0.02607107950853105]])
# Rtest = sp.SO3([[-0.02495988040066277, 0.01720436961811805,   0.9995404014027787],
#                 [0.06813350186490005,   0.997556284701166, -0.01546883243273596],
#                 [-0.9973639407428014, 0.06771608759556018, -0.02607107950853105]])
# class TestSO3(unittest.TestCase):
#     def test_static_exp(self):
#         R = sp.SO3(Rnp)
#         R_prime = sp.SO3.exp(R.log())
#         self.assertTrue(np.allclose(R.matrix(), R_prime.matrix()))

# test=TestSO3()
# test.test_static_exp()


# tmp1=R * pt  # array([2., 3., 1.])
# tmp2=T * pt  # array([3., 4., 2.])
# test=R.log()
# print("ok")

