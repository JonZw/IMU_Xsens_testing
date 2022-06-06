import mtdevice


# TODO:
#  Implement the following
#  1.) Postprocessed Dataset reading
#  2.) Computation of CoM
#  3.) Computation of Moment of Inertia
#  4.) Computation of Total Body Angular Momentum (2 functions: one for linear(?), one for angular momentum)
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


def tbam_comp():
    # Angular Momentum = (moment of inertia)(angular velocity) angular velocity can be extracted out of Xsens and
    # Qualisys (Xsens has angular velocity, Qualisys can output 6 DOF)
    # TODO:
    #  1.) Implement the math to get the (total body) angular momentum for either (or all):
    #  - quaternions,
    #  - euler angles and
    #  - rotation matrix
    #  2.) Output it in a way of return for comparison (print/diagram + return)
    pass


if __name__ == '__main__':
    # mtdevice.main()
    pass
