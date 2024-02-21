"""
Author: William OAtes
Class: CS021
Date: 1/25/2022
Description: Calculate speed given dist and time
"""
# [Input]
# Get Values for distance and time from user
distance = int(input("Enter distance: "))
time = int(input("Enter Time: "))
#Processing
#Calculate speed by the formula s = d / t
speed = distance / time

#[Output]
#Display calculated speed to user
print("The speed is", speed)
