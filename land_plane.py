import math
import get_pos

# moves plane from its current position to the base of the runway, in a straight line
# inputs: r = radius of air traffic zone, v = plane speed, runLength = length of runway, runWidth = 
# width of runway
# outputs: none
# outputs: none
def flyToRunway(r, runWidth, runLength, v):
    #move airplane to runway start
    # start from generated point along perimeter or air traffic zone
    x_curr = get_pos.getPosition()[0]
    y_curr = get_pos.getPosition()[1]

    # destination is base of runway
    # in x direction, centre of runway = radius of zone - (width of runway / 2)
    x_dest = r - (runWidth / 2)
    #in y direction, base of runway = radius - (length of runway / 2)
    y_dest = r - (runLength / 2)

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

# moves plane along runway in a straight line, at speed v
# inputs: v = plane speed, runLength = length of runway
# outputs: none
def moveAlongRunway(runLength, v):
    # start from base of runway
    x_curr = get_pos.getPosition()[0]
    y_curr = get_pos.getPosition()[1]

    # destination is end of runway
    x_dest = x_curr
    y_dest = y_curr + runLength

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

# clears memory associated with planePoint which has reach the end of the runway
def endOfRunway(planePoint):
    del planePoint