import matplotlib.pyplot as plt
import numpy as np
from typing import Final

#Author: Marco Balbontin-Ponce
#Version: 0.1.2

def generate_ideal_braking_curve():
    '''Generates a plot of the ideal braking curve based on vehicle values assigned to the variables.
       Utilises the numpy library via the use of numpy arrays, which allow calculations on whole arrays at once.
       Uses a numpy array of friction coefficients to calculate values of longitudinal weight transfer due to acceleration,
       which is then used to calculate the front and rear braking forces at which tyres begin to slip. 
       A graph of rear axle ideal braking force against front axle ideal braking force is then plotted via a matplotlib graph.'''
    
    #calculation values:
    ACCEL_DUE_TO_GRAV: Final = 9.81 #ms^-2
    WEIGHT: Final = 280 #Kg
    CENTRE_OF_GRAV_HEIGHT: Final = 0.25 #m
    WHEELBASE: Final = 1.59 #m
    FRONT_AXLE_WEIGHT_DIST: Final = 0.5

    #create array with coefficient of friction values (with a step of 0.1 from 0-1 inclusive):
    friction_coeff_arr = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    #calculates the longitudinal weight transfer due to acceleration, returning a new numpy array containing all values:
    long_weight_transfer_arr = calc_long_weight_transfer(friction_coeff_arr, ACCEL_DUE_TO_GRAV, WEIGHT, CENTRE_OF_GRAV_HEIGHT, WHEELBASE)
    #calculates the front & rear braking forces at which tyres begin to slip, returning a new numpy array for each containing all values:
    front_force_arr = calcForceAtFront(friction_coeff_arr, long_weight_transfer_arr, WEIGHT, ACCEL_DUE_TO_GRAV, FRONT_AXLE_WEIGHT_DIST) 
    rear_force_arr = calcForceAtRear(friction_coeff_arr, long_weight_transfer_arr, WEIGHT, ACCEL_DUE_TO_GRAV, FRONT_AXLE_WEIGHT_DIST)
    
    print('long weight transfer = ', long_weight_transfer_arr)
    print('front force = ', front_force_arr)
    print('rear force = ', rear_force_arr)

    #declare title of graph and plot the numpy arrays, x = front_force_arr & y = rear_force_arr.
    plt.title('Ideal Brake Curve')
    #plt.plot(x, y)
    plt.plot(front_force_arr, rear_force_arr, 'bo', linestyle = 'solid')
    #adjust the maximum and minimum values shown on the plot for the x & y axes
    plt.ylim(0, rear_force_arr.max()+100)
    plt.xlim(0, front_force_arr.max()+100)

    #add tyre friction coefficient annotations to the graph, with arrows pointing from points to related friction coefficient values.
    #for the first value the position of the first annotation will be adjusted so it is visible above the x axis.
    #all other annotations will follow the same positions relative to the points they're associated with.
    for i in range(friction_coeff_arr.size):
        annotation = f'μ = {friction_coeff_arr[i]}'
        if (i == 0):
            xytext_tuple = (22,6)
        else:
            xytext_tuple = (20,-8)
        plt.annotate(annotation, xy=(front_force_arr[i], rear_force_arr[i]), xytext=xytext_tuple, textcoords='offset points', arrowprops={"arrowstyle":"<-"})

    #add axis labels and show the graph.
    plt.xlabel('Front Axle Ideal Braking Force (N)')
    plt.ylabel('Rear Axle Ideal Braking Force (N)')
    plt.show()

    return

def calc_long_weight_transfer(friction_coeff_arr, accel_due_to_grav, weight, centre_of_grav_height, wheelbase):
    '''Calculates the longitudinal weight transfer due to acceleration. 
       The acceleration will be equal to the coefficient of friction multiplied by the acceleration due to gravity.
       A numpy array containing all values is returned (long_weight_transfer_arr)'''
    
    #longitudinal weight transfer due to acceleration calculation:
    accel_of_car_arr = (friction_coeff_arr * accel_due_to_grav)
    long_weight_transfer_arr = (accel_of_car_arr * weight)*(centre_of_grav_height/wheelbase)

    return long_weight_transfer_arr

def calcForceAtFront(friction_coeff_arr, long_weight_transfer_arr, weight, accel_due_to_grav, front_axle_weight_dist):
    '''Returns a numpy array containing all values of front braking force (N) at the instance tyres begin to slip.'''

    #front slip braking force calculation:
    front_slip_braking_force_arr = (friction_coeff_arr*((weight * accel_due_to_grav * front_axle_weight_dist) + long_weight_transfer_arr))

    return front_slip_braking_force_arr

def calcForceAtRear(friction_coeff_arr, long_weight_transfer_arr, weight, accel_due_to_grav, front_axle_weight_dist):
    '''Returns a numpy array containing all values of rear braking force (N) at the instance tyres begin to slip.'''
    #rear slip braking force calculation:
    rear_slip_braking_force_arr = (friction_coeff_arr*((weight * accel_due_to_grav)*(1-front_axle_weight_dist) - long_weight_transfer_arr))

    return rear_slip_braking_force_arr

generate_ideal_braking_curve()