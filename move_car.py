### move_car.py
# Author: Caleb Strait
# Python 3.5.2
##

### Description
# Defines a grid and a class Vehicle, which will have starting point(X, Y on the grid) and direction(one of N,E,S,W)
# taken from user and there will be commands, L & R turns the vehicle 90 degrees around left and right respectively
# and M moves the vehicle one unit to faced direction. Vehicles are sent sequentially. If the second vehicle attempts
# to move to the occupied spot of the first vehicle, the command will be skipped. If any move command makes any of the
# vehicles move out of the grid, that command will be skipped as well.
##

### Expected Inputs
# The first line defines the limits of the grid; X and Y separated by space
# The second line defines the current position and facing direction for the first vehicle; X, Y, and facing are separated by space
# The third line defines the commands for the first vehicle, which is a line of string
# The fourth and fifth lines are the same as second and third but for the second vehicle
##

def main(input_list):

    ### Unit testing
    #*# TO DO #*# test_turn_left
    #*# TO DO #*# test_turn_right
    #*# TO DO #*# test_move
    ##

    ### Variable definitions
    directions = ['N','E','S','W']
    movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
    grid_max_X, grid_max_Y = map(int, input_list[1].split())
    commands_vehicle_1 = map(int, input_list[3].split())
    commands_vehicle_2 = map(int, input_list[5].split())
    ##

    ### Create vehicles 1 & 2
    vehicle_1 = initialize_vehicle(map(int, input_list[2].split()))
    vehicle_2 = initialize_vehicle(map(int, input_list[4].split()))
    ##

    ### Perform vehicle commands
    while len(commands_vehicle_1) > 0 && len(commands_vehicle_2) > 0:
        if len(commands_vehicle_1) > 0:
            command_vehicle(vehicle_1, commands_vehicle_1[0])
            commands_vehicle_1 = commands_vehicle_1[1:]
            print_to_console(vehicle_1, 1)
        if len(commands_vehicle_2) > 0:
            command_vehicle(vehicle_2, commands_vehicle_2[0])
            commands_vehicle_2 = commands_vehicle_2[1:]
            print_to_console(vehicle_2, 2)
    ##

def initialize_vehicle(x_pos, y_pos, facing):
    return Vehicle(x_pos, y_pos, facing)

def command_vehicle(vehicle, command):
    if command == 'L':
        vehicle.turn_left()
    elif command == 'R':
        vehicle.turn_right()
    elif command == 'M':
        vehicle.move()
    else:
        raise ValueError('Invalid Command')

def print_to_console(vehicle, vehicle_num):
    print(vehicle_num + ': x=' + str(vehicle.x) + ' y=' + str(vehicle.y) + ' facing=' + vehicle.facing)

class Vehicle():
    def __init__(self, x_pos, y_pos, face):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.face = face

    def turn_left(self):
        self.face = directions[(directions.index(self.face)-1)%len(directions)] #*# TO DO #*# Check

    def turn_right(self):
        self.face = directions[(directions.index(self.face)+1)%len(directions)] #*# TO DO #*# Check

    def move(self):
        new_x = self.x_pos + movement[self.face][0] #*# TO DO #*# Check
        new_y = self.y_pos + movement[self.face][1] #*# TO DO #*# Check
        #*# TO DO #*# Check for collison with other vehicles or walls
