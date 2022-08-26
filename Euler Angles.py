import pybullet as pb
import numpy as np
import time
import transforms3d as tf

np.set_printoptions(precision=3, suppress=True)  # neat printing

#Variables
x=0
s=0
# p=0.0
# y=0.0

a=str(input('Type sequence. '))


if a == 'zyz':
    b=1
    print('funciona')


if a == 'zyx':
    b=0

# print(a)
# print(b)

#GUI
physicsClient = pb.connect(pb.GUI)
useFixedBase=True



#Ring 1 
Ring1=pb.loadURDF("3rd ring.urdf", useFixedBase= useFixedBase) # 3rd term / Outer ring

#Ring 2
Ring2=pb.loadURDF("1st ring.urdf", useFixedBase= useFixedBase) # Middle ring


#Ring 3
Ring3=pb.loadURDF("2nd ring.urdf", useFixedBase= useFixedBase) # 1st term/ Inner ring

#Parameters
Roll =pb.addUserDebugParameter("  Roll", -np.pi,np.pi,0) 
Pitch =pb.addUserDebugParameter("  Pitch", -np.pi,np.pi,0)
Yaw =pb.addUserDebugParameter("  Yaw", -np.pi,np.pi,0) 


while True:
    
    

    #Events
    keys = pb.getKeyboardEvents()
    qKey = ord('q')
    rKey = ord('r')

    #Ring RZYX

    #Ring Z / Slides 
    yz= pb.readUserDebugParameter(Yaw)
    

    #Ring Y / Slides
    yy= pb.readUserDebugParameter(Yaw)

    if rKey in keys and keys[rKey]&pb.KEY_WAS_TRIGGERED:
        py= pb.readUserDebugParameter(Pitch)
        py=np.pi/2
        s=1
        x=0
    if s==0:
        py= pb.readUserDebugParameter(Pitch)

    

    #Ring X / Slides
    px= pb.readUserDebugParameter(Pitch)
    yx= pb.readUserDebugParameter(Yaw)
    
    if qKey in keys and keys[qKey]&pb.KEY_WAS_TRIGGERED:
        rx=pb.readUserDebugParameter(Roll)
        rx=np.pi/2
        x=1
        s=0


    if x==0:
        rx= pb.readUserDebugParameter(Roll)

    if b==0:
        PosR2=tf.euler.euler2quat(0, np.pi+py, yy, 'rzyx') # Middle ring
        PosR1=tf.euler.euler2quat(0,np.pi/2,yz, 'rzyx') # 3rd term / Outer ring
        PosR3=tf.euler.euler2quat(np.pi/2+rx,np.pi+px,yx, 'rzyx') # 1st term/ Inner ring
    

    #ZYZ
    if b==1:
        PosR1=tf.euler.euler2quat(0,np.pi/2,yz, 'rzyz') # 3rd term / Outer ring
        PosR2=tf.euler.euler2quat(0, np.pi+py, yy, 'rzyz') # Middle ring
        PosR3=tf.euler.euler2quat(rx,np.pi/2+px,np.pi/2+yx, 'rzyz') # 1st term/ Inner ring


    pb.resetBasePositionAndOrientation(Ring1,[0,0,0], PosR1) 
    pb.resetBasePositionAndOrientation(Ring2,[0,0,0], PosR2)
    pb.resetBasePositionAndOrientation(Ring3,[0,0,0], PosR3)

    pb.stepSimulation()
    time.sleep(1./240.)
