import pybullet as pb
import numpy as np
import time
import transforms3d as tf
import plotly.graph_objects as go


np.set_printoptions(precision=3, suppress=True)  # neat printing

#Variables
x=0
s=0
r=0
p=0
y=0

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
    
    rKey = ord('r')
    pKey = ord('q')

    #Ring RZYX

    #Ring Z / Slides 
    yz= pb.readUserDebugParameter(Yaw)
    
    #Ring Y / Slides
    yy= pb.readUserDebugParameter(Yaw)
    py= pb.readUserDebugParameter(Pitch)

    #Ring X / Slides
    px= pb.readUserDebugParameter(Pitch)
    yx= pb.readUserDebugParameter(Yaw)
    rx=pb.readUserDebugParameter(Roll)

    #Trigger Gimbal Lock

    if rKey in keys and keys[rKey]&pb.KEY_WAS_TRIGGERED:
        r=0
        p=0
        y=0

        r=np.pi/2
    
    if pKey in keys and keys[pKey]&pb.KEY_WAS_TRIGGERED:
        r=0
        p=0
        y=0

        p=np.pi/2

    PosR1=tf.euler.euler2quat(0,(np.pi/2),yz+y, 'rzyx') # 3rd term / Outer ring

    PosR2=tf.euler.euler2quat(0, np.pi+py+p, yy+y, 'rzyx') # Middle ring
    
    PosR3=tf.euler.euler2quat(np.pi/2+rx+r,(np.pi+px),yx+y, 'rzyx') # 1st term/ Inner ring


    pb.resetBasePositionAndOrientation(Ring1,[0,0,0], PosR1) 
    pb.resetBasePositionAndOrientation(Ring2,[0,0,0], PosR2)
    pb.resetBasePositionAndOrientation(Ring3,[0,0,0], PosR3)

    time.sleep(1./240.)







    # if x==0:
    #     PosR1=tf.euler.euler2quat(0,np.pi/2,0, 'rzyx')
    #     p.resetBasePositionAndOrientation(Ring1,[0,0,0], PosR1) 
    #     time.sleep(3)
    #     x=x+1
    
    # if x==1:
    #     PosR1=tf.euler.euler2quat(0,np.pi,0, 'rzyx')
    #     p.resetBasePositionAndOrientation(Ring1,[0,0,0], PosR1) 
    #     time.sleep(3)
    #     x=x+1
    
    # if x==2:
    #     PosR1=tf.euler.euler2quat(np.pi/2,np.pi,0, 'rzyx')
    #     p.resetBasePositionAndOrientation(Ring1,[0,0,0], PosR1) 
    #     time.sleep(3)
    #     x=0











    
    





