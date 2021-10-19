import math
import queue
import generate_planes
import random
import flights
import hold_plane
import land_plane
from time import time, sleep

from plane_data import PlaneNode

###################################################################################################
#INPUT PROBLEM PARAMETERS#

def chooseMode():

    selectMode = input('Please select whether you would like to proceed with default parameters (D), or enter unique parameters (U): ')
    
    if selectMode == "D":
        parameters = {
            "radiusZ" : 10000,
            "radiusH" : 1000,
            "width" : 100,
            "length" : 500,
            "seperation" : 500,
            "numRunways" : 2,
            "speed" : 140,
            "freq" : 10,
            "safeDistance" : 100 
            }
        return parameters

    elif selectMode == "U":
        getParameters()

    else:
        print("Error, please type 'D' for default or 'U' for unique parameters")
        chooseMode()

def getParameters():
    # get user inputted parameters -> this way we can change parameters such as traffic control zone
    # radius and runway dimensions, without changing the code:

    # zone radius:
    radiusZ = int(input("Enter the Air Traffic Zone radius (m): ")) 

    # hold pattern radius:
    radiusH = int(input("Enter the holding pattern flight radius (m): ")) 

    # runway dimensions:
    width = int(input ("Enter the runway width (m): ")) 
    length = int(input ("Enter the runway length (m): ")) 
    seperation = int(input ("Enter seperation between runways (m): ")) 
    numRunways = int(input ("Enter number of runways: ")) 

    # speed of plane
    speed = int(input("Enter the speed of the aircraft (m/s): ")) 

    # frequency of transmission
    freq = int(input("Enter frequency of position readings (Hz): ")) 

    # safe distance between planes
    safeDistance = int(input("Enter a safe distance between planes to avoid crashing (m): ")) 

    parameters = {
            "radiusZ" : radiusZ,
            "radiusH" : radiusZ,
            "width" : width,
            "length" : length,
            "seperation" : seperation,
            "numRunways" : numRunways,
            "speed" : speed,
            "freq" : freq,
            "safeDistance" : safeDistance 
            }
    
    # logical test to ensure that all parameters fit inside the provided traffic control zone radius:
    if (radiusZ>radiusH) and (radiusZ>safeDistance) and (length<radiusZ) and (((width*numRunways) + ((numRunways-1)*seperation))<radiusZ):
        return parameters
    else:
        print("The parameters you entered are not physically possible; please try again")
        getParameters()

###################################################################################################
#SUPPORTING FUNCTIONS FOR AIRPLANE DATA#

# determine whether the airplane is being signaled to land (next up in queue)
# status = 1 corresponds to airplane being directed to land
# status = 2 corresponds to airplane entering holding pattern
def getStatus(identPoint):
    
    # return and remove from queue the next airplane to be signalled for landing
    landQueue = getQueue()
    airplaneToLand = landQueue.get()
    
    # if the airplane to be signalled for landing is this airplane, set status = 1
    if (airplaneToLand == identPoint):
        status = 1
    
    # if this airplane is not to be signalled for landing, set status = 2
    else:
        status = 2
    
    return status

# this function determines the maximum number of planes which can circle in a holding pattern
# within the air traffic control zone
# inputs: zoneRad = radius of air traffic control zone, holdRad = radius of holding flight pattern,
# dist = the allowable safe distance between planes
# outputs: maxHoldPattern = (int) maximum number of planes which can circle within the zone
def maxNumberOfPlanes(zoneRad, holdRad, dist):

    # to ensure that even with a maximum number of planes in the air traffic control zone, no
    # 2 airplanes will come within 100m (safeDistance) of eachother, we add safeDistance/2 to 
    # the holding pattern radius as a 'padding'
    holdRad = holdRad + (dist/2)

	# catch-case: if user inputs smaller air traffic zone than holding pattern radius
    if (holdRad > zoneRad):
	    return 0

    #angle made by holding pattern radius
    angleHold = 0
    # ratio of holding pattern radius : difference between air traffic zone and holding pattern radii
    ratio = 0
    # maximum holding pattern circles that can be made inside the air traffic zone (this translates to max number of planes)
    maxNumPlanes = 0
	# Stores the ratio
    ratio = holdRad / (zoneRad - holdRad)

    # if hold pattern diameter > air traffic zone, we can only have one plane flying this pattern inside the zone
    if (zoneRad < 2 * holdRad):
	    maxNumPlanes = 1
	
    else:

		# find angle of holding pattern circle
	    angleHold = (abs(math.asin(ratio) * 180) / 3.14159265)		
		# use this to find the maximum number of holding pattern circle flights which can be made in the air traffic zone
	    maxNumPlanes = (360 / (2 * math.floor(angleHold)))
	
	# Return the final result
    return maxNumPlanes

# determine the destination runway for given plane
# inputs: runways = number of runways
def whichRunway(self, runways):

    # check if there are runways to the right -> if yes, airplane lands at next available runway
    if self.destRunway >= runways:
        self.destRunway = self.destRunway + 1
        return self.destRunway
    
    # if we are at the rightmost runway, the next plane will land back at runway 1 (left-most)
    else:
        self.destRunway = 1
        return self.destRunway

param = chooseMode()

# create int variables for ease of use throughout main function:
radiusZ = param["radiusZ"]
radiusH = param["radiusH"]
width = param["width"]
length = param["length"]
seperation = param["seperation"]
numRunways = param["numRunways"]
speed = param["speed"]
freq = param["freq"]
safeDistance = param["safeDistance"]

maxPlanes = maxNumberOfPlanes(radiusZ, radiusH, safeDistance)

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
    x, self.origin[0] = zRad * math.acos(theta)
    y, self.origin[1] = zRad * math.asin(theta)

    # put plane in queue to land
    airplaneLandingWait.put(self)

    flights.Flights().append(self)

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

class TrafficController:

    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
        pass
     
    def control(self):

        planesInZone = 0

        while True:

            # if there is space in the traffic control zone, spawn an airplane and increment the
            # number of airplanes inside the traffic control zone:
            if (planesInZone < maxPlanes):
                cur_plane = self.tail
                cur_plane.origin = generatePlane(self, radiusZ)
                planesInZone = planesInZone + 1

            next_plane = self.next 

            cur_plane.status = next_plane.status

            if (cur_plane.status == 2):
                # airplane follows initial flight pattern (straight towards centre)
                pattern = hold_plane.basicFlight(self, radiusZ, radiusH, speed)
                    
                if (hold_plane.basicFlight(self, radiusZ, radiusH, speed) == "done"):
                    #plane in holding mode
                    pattern = hold_plane.flyInCircle(self, speed, radiusH, radiusZ)

            if (cur_plane.status == 1):
                cur_plane.destRunway = whichRunway(self, numRunways)
                #plane directed to land
                land_plane.flyToRunway(self, radiusZ, width, length, speed)           
                    
                # if the plane has reached the runway, move along in straight line
                if (cur_plane.currLocation[0] == radiusZ - (width / 2)):
                    land_plane.moveAlongRunway(self, length, speed, planesInZone)

            # get current position
            cur_plane.currLocation = self

            #checkIfCrash(self, other, safeDistance)

            # account for frequency of position readings
            updateT = 1 / freq
            sleep(updateT - time() % updateT)