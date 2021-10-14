import math
import random

def generatePlane(r):

    # initialize plane point at (0,0) - note this is not the origin/centre (random point at upper RH corner)
    x, y = 0
    planePoint = [x,y]

    # generate random angle theta, to place plane along air traffic zone circumference
    # use theta = 2*pi*k for 0<=k<=1 to generate random angle
    k = random.randint(0,1)
    theta = 2 * math.pi * k

    # use circle equation to determine (x,y) point along circle using x=r*cos(theta) and y=r*sin(theta)
    # r is the radius of the air traffic zone, as inputted by the user (10km per the given problem)
    x = r * math.acos(theta)
    y = r * math.asin(theta)

    return planePoint

def basicFlightPattern(f, r, new_pos, v):

    # start from generated point along perimeter or air traffic zone
    x_curr = generatePlane(r)[0]
    y_curr = generatePlane(r)[1]

    # destination is centre of circle, which is located at point (radius, radius)
    x_dest, y_dest = r

    # constant speed plane is moving at
    speed = v

    delta_x = x_dest - x_curr
    delta_y = y_dest - y_curr
    distance = math.isqrt((delta_x * delta_x) + (delta_y * delta_y))

    if (distance > speed):
        ratio = speed / distance
        x_move = ratio * delta_x
        y_move = ratio * delta_y
        new_x_pos = x_move + x_curr
        new_y_pos = y_move + y_curr

    else:
        new_x_pos = x_dest
        new_y_pos = y_dest

    new_pos = [new_x_pos, new_y_pos]
    
    return new_pos


def maxNumberOfPlanes(radiusZone, radiusHold):
	
	# catch-case: if user inputs smaller air traffic zone than holding pattern radius
	if (radiusHold > radiusZone):
		return 0

    #angle made by holding pattern radius
	angleHold = 0

    # ratio of holding pattern radius : difference between air traffic zone and holding pattern radii
	ratio = 0

    # maximum holding pattern circles that can be made inside the air traffic zone (this translates to max number of planes)
	maxHoldPattern = 0

	# Stores the ratio
	ratio = radiusHold / (radiusZone - radiusHold)

    # if hold pattern diameter > air traffic zone, we can only have one plane flying this pattern inside the zone
	if (radiusZone < 2 * radiusHold):
		number_of_circles = 1
	
	else:

		# find angle of holding pattern circle
		angleHold = (abs(math.asin(ratio) * 180) / 3.14159265)
		
		# use this to find the maximum number of holding pattern circle flights which can be made in the air traffic zone
		maxHoldPattern = (360 / (2 * math.floor(angleHold)))
	
	# Return the final result
	return maxHoldPattern
