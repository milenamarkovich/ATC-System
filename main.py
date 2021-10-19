import math
from time import time, sleep
from plane_data import param, Airplane
import plane_data
import hold_plane
import land_plane

plane_data.chooseMode()

##################################################################################################
#SUPPORTING FUNCTIONS:

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

maxPlanes = maxNumberOfPlanes(param["radiusZ"], param["radiusH"], param["safeDistance"])

###################################################################################################
#MAIN FUNCTION:

planesInZone = 0

# create int variables for ease of use throughout main function:
radiusZ = int(param["radiusZ"])
radiusH = int(param["radiusH"])
width = int(param["width"])
length = int(param["length"])
seperation = int(param["seperation"])
numRunways = int(param["numRunways"])
speed = int(param["speed"])
freq = int(param["freq"])
safeDistance = int(param["safeDistance"])

def main(self, other):

    while True:

        # if there is space in the traffic control zone, spawn an airplane and increment the
        # number of airplanes inside the traffic control zone:
        if (planesInZone < maxPlanes):
            self.origin
            planesInZone = planesInZone + 1

        if (self.status == 1):
            # airplane follows initial flight pattern (straight towards centre)
            hold_plane.basicFlight(self, radiusZ, radiusH, speed)
            
        if (self.status == 0):
            #plane in holding mode
            hold_plane.flyInCircle(self, speed, radiusH, radiusZ, safeDistance, other)

        if (self.status == 1):
            #plane directed to land
            land_plane.flyToRunway(self, radiusZ, width, length, speed)           
            
            # if the plane has reached the runway, move along in straight line
            if (self.currLocation[0] == radiusZ - (width / 2)):
                land_plane.moveAlongRunway(self, length, speed, planesInZone)

        # get current position
        self.currLocation

        # account for frequency of position readings
        updateT = 1 / freq
        sleep(updateT - time() % updateT)
    
main(Airplane.self, Airplane.other)