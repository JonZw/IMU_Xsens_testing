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


def moi_comp():
    # TODO:
    #   Check if Xsens and/or Qualisys gives output of the MoI (after postprocessing)
    #   If yes, then output in form a diagram or return it for comparison
    #   Note: This function might be unnecessary, if the MATLAB code or the software is already outputting it
    pass


def tbam_comp(): # needs as input the angular velocity of x,y,z and the number of datapoints
    # Angular Momentum = (moment of inertia)(angular velocity) angular velocity can be extracted out of Xsens and
    # Qualisys (Xsens has angular velocity, Qualisys can output 6 DOF)
    # TODO:
    #  1.) Implement the math to get the (total body) angular momentum for either (or all):
    #  - quaternions,
    #  - euler angles and
    #  - rotation matrix
    #  -> Both have Euler and rotation matrix! Try Euler first
    #  2.) Output it in a way of return for comparison (print/diagram + return) -> Is the angular momentum of CoM ok?
    #  Formula will be: L = Ic * w, Ic = - sum[i=1; N](m_i * (delta r_i)^2) and w = angular velocity (given from data),
    #  m_i = mass of i and r_i = denotes the trajectory of each particle i
    """
    I_c = 0
    for i in range(1,N):
        I_c += mass_i * (delta-r_i)^2
    I_c = - sum(1, N)

    L = I_c * w"""


if __name__ == '__main__':
    # mtdevice.main()
    pass
