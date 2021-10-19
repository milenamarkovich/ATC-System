import math

# moves plane from its current position to the base of the runway, in a straight line
# inputs: r = radius of air traffic zone, v = plane speed, runLength = length of runway, runWidth = 
# width of runway
# outputs: none
def flyToRunway(self, r, runWidth, runLength, speed):
    #move airplane to runway start
    # start from generated point along perimeter or air traffic zone
    #self.currLocation = get_pos.getPosition()[0]
    #self.currLocation = get_pos.getPosition()[1]

    # destination is base of runway
    # in x direction, centre of runway = radius of zone - (width of runway / 2)
    dest_x = r - (runWidth / 2)
    #in y direction, base of runway = radius - (length of runway / 2)
    dest_y = r - (runLength / 2)

    delta_x = dest_x - self.currLocation[0]
    delta_y = dest_y - self.destination[1]
    distance = math.isqrt((delta_x * delta_x) + (delta_y * delta_y))

    if (distance > speed):
        ratio = speed / distance
        x_move = ratio * delta_x
        y_move = ratio * delta_y
        self.currLocation[0] = x_move + self.currLocation[0]
        self.currLocation[1] = y_move + self.currLocation[1]

    else:
        self.currLocation[0] = dest_x
        self.currLocation[1] = dest_y

# moves plane along runway in a straight line, at speed v
# inputs: v = plane speed, runLength = length of runway
# outputs: none

def moveAlongRunway(self, runLength, speed, numPlanes):

    # destination is end of runway
    dest_x = self.currLocation[0]
    dest_y = self.currLocation[1] + runLength

    delta_x = dest_x - self.currLocation[0]
    delta_y = dest_y - self.currLocation[1]
    distance = math.isqrt((delta_x * delta_x) + (delta_y * delta_y))

    if (distance > speed):
        ratio = speed / distance
        x_move = ratio * delta_x
        y_move = ratio * delta_y
        self.currLocation[0] = x_move + self.currLocation[0]
        self.currLocation[1] = y_move + self.currLocation[1]

    else:
        self.currLocation[0] = dest_x
        self.currLocation[1] = dest_y
        endOfRunway(self, numPlanes)
    

# clears memory associated with planePoint which has reach the end of the runway
def endOfRunway(self, numPlanes):
    numPlanes -= 1
    del self