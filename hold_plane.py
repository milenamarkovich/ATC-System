import math
import air_traffic_control
from time import time, sleep

# direct airplane to enter basic flight pattern (fly straight towards center of zone) until it is
# able to fly in the holding pattern radius without exiting the traffic control zone
def basicFlight(self, radZ, radH, v):

    # define circle within which 'appropriate origin points' will exist (meaning they are far
    # enough from the edge of the traffic zone, to not leave the zone during circular, holding
    # pattern flight)

    # start by finding the angle the vector between traffic zone origin and the spawned airplane
    # point makes w/ the horizontal using theta = arctan (y_orig/x_orig)
    x = self.origin[0]
    y = self.origin[1]

    theta = math.atan(y/x)
    r = radZ - radH

    # destination is an appropriate point at which to begin circular holding pattern
    dest_x = r * math.acos(theta)
    dest_y = r * math.asin(theta)

    delta_x = dest_x - self.currLocation[0]
    delta_y = dest_y - self.currLocation[1]
    distance = math.isqrt((delta_x * delta_x) + (delta_y * delta_y))

    if (distance > v):
        ratio = v / distance
        x_move = ratio * delta_x
        y_move = ratio * delta_y
        self.currLocation[0] = x_move + self.currLocation[0]
        self.currLocation[1] = y_move + self.currLocation[1]

    else:
        self.currLocation[0] = dest_x
        self.currLocation[1] = dest_y

def flyInCircle(self, speed, r, rZ, safeDist, other):

    # define starting angle and angular speed (omega)
    angle = math.radians(45)
    omega = speed / r

    # define centre point around which the airplane will fly in a circular pattern
    # first we will choose a centre-point to the left of the plane:

    # if the plane is to the left of the zone origin, its holding pattern origin will be to the left,
    # this is because we want planes to be as far from the runway (centre) as possible, in order to
    # fit as many planes in the traffic zone as possible:
    if (self.currLocation[0] < rZ):
        originX = self.currLocation[0] - (r * math.sin(angle))
    # similarly, if the plane is to the right of the zone origin, its holding pattern origin will be to
    # the right
    else:
        originX = self.currLocation [0] + (r * math.sin(angle))

    # this logic is repeated to determine the origin in the y-axis:
    if (self.currLocation[1] < rZ):
        originY = self.currLocation[1] - (r * math.cos(angle))

    else:
        originY = self.currLocation[1] + (r * math.cos(angle))

    # if this centre point will set the plane on a collision course with another plane,
    # we will choose a centre-point to the left of the plane
    if (air_traffic_control.checkIfCrash(self, other, safeDist) == True):
        originX = self.currLocation[0] + r
    
    # while the plane is not yet signalled to land, it flies in a circle of the given holding pattern
    # radius (ie: 1km)
    while self.status == 2 :
        angle += omega
        self.currLocation[0] = originX + (math.acos(angle + (math.pi/2)) * r * omega)
        self.currLocation[1] = originY - (math.asin(angle + (math.pi/2)) * r * omega)