import matplotlib.pyplot as plt
import numpy as np
from typing import Final

#Author: Marco Balbontin-Ponce
#Version: 0.0.2

#Will generate the ideal braking curve based on values which are inputted.
def generate_ideal_braking_curve():
    return

#Calculates the longitudinal weight transfer due to acceleration. 
#The acceleration will be equal to the coefficient of friction multiplied by the acceleration due to gravity.
def calc_long_weight_transfer(friction_coeff):
    ACCEL_DUE_TO_GRAV: Final = 9.81 #ms^-2
    WEIGHT: Final = 280 #Kg
    CENTRE_OF_GRAV_HEIGHT: Final = 0.25 #m
    WHEELBASE: Final = 1.59 #m

    #Longitudinal weight transfer due to acceleration calculation:
    accel_of_car = (friction_coeff * ACCEL_DUE_TO_GRAV)

    long_weight_transfer = (accel_of_car * WEIGHT)*(CENTRE_OF_GRAV_HEIGHT/WHEELBASE)

    return long_weight_transfer

#Returns an array containing all Front Brake Force values to be plotted.
def calcForceAtFront(friction_coeff, long_weight_transfer):
    WEIGHT: Final = 280 #Kg
    ACCEL_DUE_TO_GRAV: Final = 9.81 #ms^-2
    FRONT_AXLE_WEIGHT_DIST: Final = 0.5

    front_slip_braking_force = (friction_coeff*((WEIGHT * ACCEL_DUE_TO_GRAV * FRONT_AXLE_WEIGHT_DIST) + long_weight_transfer))

    return front_slip_braking_force