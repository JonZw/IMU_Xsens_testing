import mtdevice
import math

# TODO:
#  Implement the following
#  1.) Postprocessed Dataset reading
#  2.) Computation of CoM
#  3.) Computation of Moment of Inertia
#  4.) Computation of Total Body Angular Momentum (one for angular momentum of CoM enough?)
#  5.) Functions which compare the output of 2 CoM, MoI and TBAM
#  Split the function in more scripts, if more readable
#  Note: Apparently a lot of code needed, maybe I should just implement the computation and not the whole thing

# Following function might not be necessary
def input_data():
    # TODO:
    #   If data has to be cleared or modified in some way, do it here or export to another script if it is too much
    pass


def com_comp():
    # TODO:
    #   Check if Xsens and/or Qualisys gives output of the CoM (after postprocessing)
    #   If yes, then output in form a diagram or return it for comparison
    #   Note: This function might be unnecessary, if the MATLAB code or the software is already outputting it
    pass


def moi_comp(): # Need body weight as input
    # TODO:
    #   Check if Xsens and/or Qualisys gives output of the MoI (after postprocessing)
    #   If yes, then output in form a diagram or return it for comparison
    #   Note: This function might be unnecessary, if the MATLAB code or the software is already outputting it
    #   Ic = - sum[i=1; N](m_i * (delta r_i)^2) and w = angular velocity (given from data),
    #   m_i = mass of i and r_i = denotes the trajectory of each particle i
    #   -> Is the parallel axis theorem maybe more accurate and easier to do?
    """
    With the help of a paper I found average percentage, which is widely accepted (according to the paper)
    The following percentages are the segment weighs according to the body mass and might be very helpful for Inertia
    computation of rigid body with complex shape, which may get the most exact Center of mass result
    Head&Neck = 8,2%
    Torso = 46,84%
    Upper arm = 3,25 %
    Lower arm = 1,8%
    Hand = 0,65%
    Thigh = 10,5%
    Calf = 4,75%
    Foot = 1,43%

    Segment lenghts as percentage of body height
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

    I_c = 0
    for i in range(1,N):
        I_c += mass_i * (delta-r_i)^2
    I_c = - sum(1, N)
    return I_c

    Pseudocode for Parallel Axis Theorem
    -> Easier than the first approach, because I don't need the indvidual mass.
    I will just assume the mass and the distance from the arm (and the range of the arm)


    I_pa = I_CoM + mass * (distance)^2
    return I_pa

    """
    pass


def tbam_comp():
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
    """
    I_C = moi_comp()
    L = I_c * w, w = euler angles. NOTE: I possibly have to individually calculate the different axis angles.

    return L
    """


if __name__ == '__main__':
    # mtdevice.main()
    pass
