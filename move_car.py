# codeReviewFun
# Author:
# Purpose:
# Python version:

# Variable setup
directions = ['N','E','S','W']
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split()) ### Explain unintuitive code

first_vehicle_x = None ### Not needed
first_vehicle_y = None

class Vehicle():
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face ### 'dir' is reserved

    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)] ### Separate out into multiple lines

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)] ### Separate out into multiple lines

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        if new_x != first_vehicle_x or new_y != first_vehicle_y: ### Compare new position to each vehicle, not just first
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y

# test_turn_left

# test_turn_right

# test_move

# Request inputs
vehicle_one_pos = raw_input().split()
vehicle_one_commands = raw_input()

vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command])) ### Try to avoid eval() for readability

first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y


vehicle_two_pos = raw_input().split() ### Define function rather than duplicating code
vehicle_two_commands = raw_input()

vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2]) ### Typo 'vehicle_two_ps' -> 'vehicle_two_pos'
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

print vehicle_one.x, vehicle_one.y, vehicle_one.dir ### Create main function and return variables ### Create output function that prints returns from main
print vehicle_two.x, vehicle_two.y, vehicle_two.dir
