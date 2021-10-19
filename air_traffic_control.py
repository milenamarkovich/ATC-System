import math
import queue
import generate_planes
import random

# create queue which will allow airplanes to land in FIFO (First In First Out) order
airplaneLandingWait = queue.Queue()

def getQueue():
    return airplaneLandingWait

# this function generates a random point along the perimeter of the air traffic control zone
# inputs: zRad = zone radius
# outputs: list, [x,y] of spawn location
def generatePlane(self, zRad):

    # initialize plane point at (0,0) - note this is not the origin/centre (random point at upper RH corner)
    [x,y] = [0,0]

    # generate random angle theta, to place plane along air traffic zone circumference
    # use theta = 2*pi*k for 0<=k<=1 to generate random angle
    k = random.randint(0,1)
    theta = 2 * math.pi * k

    # use circle equation to determine (x,y) point along circle using x=r*cos(theta) and y=r*sin(theta)
    # r is the radius of the air traffic zone, as inputted by the user (10km per the given problem)
    x = zRad * math.acos(theta)
    y = zRad * math.asin(theta)

    # put plane in queue to land
    airplaneLandingWait.put(self)

    return [x,y]

def adjust(self, other):

    # if the threat is to the left, move plane to the right:
    if (self.currLocation[0] > other.currLocation[0]):
        self.currLocation[0] = self.currLocation[0] + 1

    # if the threat is to the right, move plane to the left:
    else:
        self.currLocation[0] = self.currLocation[0] + 1

    # if the threat is 'above' (along y-axis), move the plane 'down'
    if (self.currLocation[1] > other.currLocation[1]):
        self.currLocation[1] = self.currLocation[1] + 1

    # if the threat is 'below' (along y-axis), move the plane 'up'
    else:
        self.currLocation[1] = self.currLocation[1] - 1

def checkIfCrash(self, other, distSafe):

    # check if plane is to the left or right of 'crash threat' plane and define the horizontal distance
    # between the two accordingly:
    if (self.currLocation[0] > other.currLocation[0]):
        delta_x = self.currLocation[0] - other.currLocation[0]
    else:
        delta_x = other.currLocation[0] - self.currLocation[0]

    # check if plane is 'above' or 'below' (in the y-axis) of 'crash threat' plane and define the 
    # vertical (y) distance between the two accordingly:
    if (self.currLocation[1] > other.currLocation[1]):
        delta_y = self.currLocation[1] - other.currLocation[1]
    else:
        delta_y = other.currLocation[1] - self.currLocation[1]

    # define the diagonal distance between the two planes:
    delta_diag = math.isqrt((delta_x * delta_x) + (delta_y * delta_y))

    # if the planes are at or less than the defined safe distance (ie: 100m) between planes re-adjust 
    # the plane flight pattern to distance itself from the 'crash threat'
    if (delta_x <= distSafe) or (delta_y <= distSafe) or (delta_diag <= distSafe) :
        adjust(self, other)
        return True

    else:
        return False
