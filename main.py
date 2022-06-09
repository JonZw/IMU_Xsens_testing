import mtdevice
import math
import json
import numpy as np

# TODO:
#  Implement the following
#  1.) Write functions, which handles, structures the data from the incoming dataset
#  2.) Postprocessed Dataset reading
#  3.) Computation of CoM
#  4.) Computation of Moment of Inertia
#  5.) Computation of Total Body Angular Momentum (one for angular momentum of CoM enough?)
#  6.) Functions which compare the output of 2 CoM, MoI and TBAM
#
#  Split the function in more scripts, if more readable
#  Note: Apparently a lot of code needed, maybe I should just implement the computation and not the whole thing


"""
With the help of a paper I found average percentage, which is widely accepted (Hall, according to the paper)
The following percentages are the segment weighs according to the body mass and might be very helpful for Inertia
computation of rigid body with complex shape, which may get the most exact Center of mass result.

Head & Neck = 8,2%
Torso = 46,84%
Upper arm = 3,25 %
Lower arm = 1,8%
Hand = 0,65%
Thigh = 10,5%
Calf = 4,75%
Foot = 1,43%

Segment lengths as percentage of body height
Head & Neck 10.75
Torso 30.00
Upper arm 17.20
Lower arm 15.70
Hand 5.75
Thigh 23.20
Calf 24.70
Foot 14.84

Distance of segment centre of gravity from proximal end as percentage of segment length.

Head & Neck = 56.7
Torso = 56.2
Upper arm = 43.6
Lower arm = 43.0
Hand = 46.8
Thigh = 43.3
Calf = 43.4
Foot = 50.0

Radius of gyration of body segments as a percentage of segment length.
-> Longitudinal axis is for now the most important (For standing/straight walking)

            Radius of gyration according to the axis
Segment        Sagittal    Frontal     Longitudinal
Head & Neck     30.3        31.5        26.1
Torso           48.2        38.3        46.8
Upper arm       32.8        31.0        18.2
Lower arm       29.5        28.4        13.0
Hand            28.5        23.3        18.2
Thigh           26.7        26.7        12.1
Calf            28.1        27.5        11.4
Foot            25.7        24.5        12.4

Pseudocode for Inertia with rigid bodies for complex shapes
-> Might be not realistic, because I most likely will not get the mass from the body segments (and the radius)
-> Edit: Body segment weight and delta r is solved with the information above
"""

# Variables are set global, because they don't need to be changed and are needed for more than one function
# Weight percentage
hn_w = 8.2
t_w = 46.84
ua_w = 3.25
la_w = 1.8
hand_w = 0.65
thigh_w = 10.5
c_w = 4.75
f_w = 1.43

# Longitudinal axis percentage
hn_lo = 26.1
t_lo = 46.8
ua_lo = 18.2
la_lo = 13.0
hand_lo = 18.2
thigh_lo = 12.1
c_lo = 11.4
f_lo = 12.4

position = []  # Will be used to store to all position, will be later changed to JSON, just for testing for now


# Following function(s) will be used to handle data. Change the functions later into a new script
def input_data():
    # TODO:
    #   If data has to be cleared or modified in some way, do it here or export to another script if it is too much
    pass


def weightsegment_comp(mass):
    sc_mass = mass * 0.01
    weight = [hn_w * sc_mass, t_w * sc_mass, ua_w * sc_mass, la_w * sc_mass, hand_w * sc_mass, thigh_w * sc_mass,
              c_w * sc_mass,
              f_w * sc_mass]
    return weight


def longitudinal_comp(mass):
    sc_mass = mass * 0.01
    longitudinal = [hn_lo * sc_mass, t_lo * sc_mass, ua_lo * sc_mass, la_lo * sc_mass, hand_lo * sc_mass, thigh_lo *
                    sc_mass, c_lo * sc_mass, f_lo * sc_mass]
    return longitudinal





def position_comp(mass, pos):  # NOT YET CORRECT!!!
    # TODO:
    #  Find a way to assign the percentage weight to the exact position. -> Maybe structure it in a way and
    #  make it analog to weightsegment_comp(mass)
    #  So write a preprocessing functions, which sorts the input according to its labels in the right order
    #  Figure out, how I can make the code below (especially the second variable I need to figure out on how to assign)

    """
    Following code could add a new json file with the content:
    A = {
    string: value
    }

    with open("data.json", "w") as fp:
        json.dump(A, fp)

    -> This might solve the problem with adding and computing all pos
    """

    position.append(pos)
    position[-1][0] = pos[0] * weightsegment_comp(mass)[0]  # SECOND VARIABLE IS ONLY EXAMPLE AND NOT RIGHT!!!
    position[-1][1] = pos[1] * weightsegment_comp(mass)[1]  # SECOND VARIABLE IS ONLY EXAMPLE AND NOT RIGHT!!!
    position[-1][2] = pos[2] * weightsegment_comp(mass)[2]  # SECOND VARIABLE IS ONLY EXAMPLE AND NOT RIGHT!!!
    # TODO: Find a way to map x,y,z to the right weight percentage and that it is called for every position


def com_comp(mass, pos):  # mass is the body weight, pos needs to be an array containing x,y,z coordinates
    # TODO:
    #   Check if Xsens and/or Qualisys gives output of the CoM (after postprocessing)
    #   If yes, then output in form a diagram or return it for comparison
    #   Note: This function might be unnecessary, if the MATLAB code or the software is already outputting it
    #   Also: It needs functions to work, which can map the right position to the right weight percentage
    #   Ask Lizeth if the dataset always gets processed in the same order!!!

    """
    Pseudocode:
    CoM.x = 0
    CoM.y = 0
    CoM.z = 0
    CoM = [CoM.x, CoM.y, CoM.z]

    for i in range(0,N):
        CoM.x += mass_i * pos.x_i
        CoM.y += mass_i * pos.y_i
        CoM.z += mass_i * pos.z_i

    return CoM
    """

    # Clearer Codesketch
    position_comp(mass, pos)
    # TODO: position_comp(mass, pos) is only called once for now, it needs to be called for every position in the end!!!
    """
    for i in range(0, len(position) -1):
        com_x += position[i][0]
        com_y += position[i][1]
        com_z += position[i][2]
    """

    return np.sum(position, axis=0) / mass  # already enough code, check if the output is right later


def moi_comp(mass):  # Need body weight as input
    # TODO:
    #   Check if Xsens and/or Qualisys gives output of the MoI (after postprocessing)
    #   If yes, then output in form a diagram or return it for comparison
    #   Note: This function might be unnecessary, if the MATLAB code or the software is already outputting it
    #   Ic = - sum[i=1; N](m_i * (delta r_i)^2) and w = angular velocity (given from data),
    #   m_i = mass of i and r_i = denotes the trajectory of each particle i
    #   -> Is the parallel axis theorem maybe more accurate and easier to do?

    weight = weightsegment_comp(mass)

    longitudinal = longitudinal_comp(mass)

    i_c = 0
    # TODO: check numpy if there is a more efficient way
    for i in range(0, len(weight)):
        i_c += weight[i] * pow((longitudinal[i]), 2)

    """
    Pseudocode for Parallel Axis Theorem (Alternative and/or maybe better way)
    -> Easier than the first approach, because I don't need the indvidual mass.
    I will just assume the mass and the distance from the arm (and the range of the arm)


    I_pa = I_CoM + mass * (distance)^2
    return I_pa

    """

    return i_c


def tbam_comp(mass, ang_vel):
    # needs as input the angular velocity of x,y,z and the number of datapoints
    # Angular Momentum = (moment of inertia)(angular velocity) angular velocity can be extracted out of Xsens and
    # Qualisys (Xsens has angular velocity, Qualisys can output 6 DOF)
    # TODO:
    #  1.) Implement the math to get the (total body) angular momentum for either (or all):
    #  - quaternions,
    #  - euler angles and
    #  - rotation matrix
    #  -> Both have Euler and rotation matrix! Try Euler first
    #  2.) Output it in a way of return for comparison (print/diagram + return) -> Is the angular momentum of CoM ok?
    #  Formula will be: L = Ic * w, Ic will be computed in moi_comp()
    #  NOTE: STILL HAVE TO COMPUTE THE TOTAL BODY ANGULAR MOMENTUM, FOR NOW IT IS ONLY FOR TEST: NEED TO WAIT FOR COM!

    i_c = moi_comp(mass)
    l = i_c * ang_vel  # ang_vel = euler angles.
    # TODO: I maybe have to individually calculate the different axis angles, if I need more than one axis to compute.

    return l


if __name__ == '__main__':
    m = 75
    ang_v = 0.3
    p = [2, 3, 4]
    print(com_comp(m, p))
    print(tbam_comp(m, ang_v))
    print(moi_comp(m))
