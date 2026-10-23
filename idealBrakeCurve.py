import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from typing import Final

#Author: Marco Balbontin-Ponce
#Version: 0.0.7

#Generates a plot of the ideal braking curve based on values assigned to the final variables.
#Get an array with coefficients from 0-1 with a step of 0.1. Use this array to generate another array of long_weight_transfer
#values and then calculate rear and front slip forces, also being arrays and then plot values. Add interactivity (annotations).
def generate_ideal_braking_curve():
    #calculation values:
    ACCEL_DUE_TO_GRAV: Final = 9.81 #ms^-2
    WEIGHT: Final = 280 #Kg
    CENTRE_OF_GRAV_HEIGHT: Final = 0.25 #m
    WHEELBASE: Final = 1.59 #m
    FRONT_AXLE_WEIGHT_DIST: Final = 0.5

    #create array with coefficient of friction values and then calculate Front & Rear force, generating 2 more arrays to be plotted.
    friction_coeff_arr = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    
    long_weight_transfer_arr = calc_long_weight_transfer(friction_coeff_arr, ACCEL_DUE_TO_GRAV, WEIGHT, CENTRE_OF_GRAV_HEIGHT, WHEELBASE)
    front_force_arr = calcForceAtFront(friction_coeff_arr, long_weight_transfer_arr, WEIGHT, ACCEL_DUE_TO_GRAV, FRONT_AXLE_WEIGHT_DIST) 
    rear_force_arr = calcForceAtRear(friction_coeff_arr, long_weight_transfer_arr, WEIGHT, ACCEL_DUE_TO_GRAV, FRONT_AXLE_WEIGHT_DIST)
    
    #plt.plot(x, y)
    plt.title('Ideal Brake Curve')
    plt.plot(front_force_arr, rear_force_arr)
    plt.xlabel('Front Brake Force (N)')
    plt.ylabel('Rear Brake Force (N)')
    plt.show()
    return

#Calculates the longitudinal weight transfer due to acceleration. 
#The acceleration will be equal to the coefficient of friction multiplied by the acceleration due to gravity.
def calc_long_weight_transfer(friction_coeff_arr, accel_due_to_grav, weight, centre_of_grav_height, wheelbase):
    #longitudinal weight transfer due to acceleration calculation:
    accel_of_car_arr = (friction_coeff_arr * accel_due_to_grav)
    long_weight_transfer_arr = (accel_of_car_arr * weight)*(centre_of_grav_height/wheelbase)

    return long_weight_transfer_arr

#Returns the value of front braking force (N) at the instance tyres begin to slip.
def calcForceAtFront(friction_coeff_arr, long_weight_transfer_arr, weight, accel_due_to_grav, front_axle_weight_dist):
    #front slip braking force calculation:
    front_slip_braking_force_arr = (friction_coeff_arr*((weight * accel_due_to_grav * front_axle_weight_dist) + long_weight_transfer_arr))

    return front_slip_braking_force_arr

#Returns the value of rear braking force (N) at the instance tyres begin to slip.
def calcForceAtRear(friction_coeff_arr, long_weight_transfer_arr, weight, accel_due_to_grav, front_axle_weight_dist):
    #rear slip braking force calculation:
    rear_slip_braking_force_arr = (friction_coeff_arr*((weight * accel_due_to_grav)*(1-front_axle_weight_dist) - long_weight_transfer_arr))

    return rear_slip_braking_force_arr

generate_ideal_braking_curve()