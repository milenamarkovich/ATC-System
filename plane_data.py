import math
import air_traffic_control

###################################################################################################
#INPUT PROBLEM PARAMETERS#

def chooseMode():

    select = input("Please select whether you would like to proceed with default parameters (D), or enter unique parameters (U): ")
    
    if select == "D":
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

    elif select == "U":
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

# determine the destination runway for given plane
def destRunway(self, runways):

    # check if there are runways to the right -> if yes, airplane lands at next available runway
    if self.destRunway >= runways:
        self.destRunway += 1
    
    # if we are at the rightmost runway, the next plane will land back at runway 1 (left-most)
    else:
        self.destRunway = 1

# update the position coordinates at given frequency (ie: 10Hz)
def getPosition(self):
    self.currLocation [0] = self.currLocation[0]
    self.currLocation[1] = self.currLocation[1]

# determine whether the airplane is being signaled to land (next up in queue)
# status = 1 corresponds to airplane being directed to land
# status = 2 corresponds to airplane entering holding pattern
def getStatus(self):
    
    # return and remove from queue the next airplane to be signalled for landing
    landQueue = air_traffic_control.getQueue()
    airplaneToLand = landQueue.get()
    
    # if the airplane to be signalled for landing is this airplane, set status = 1
    if (airplaneToLand == self):
        self.status = 1
    
    # if this airplane is not to be signalled for landing, set status = 2
    else:
        self.status = 2

###################################################################################################
#AIRPLANE CLASS#

class Airplane :
    # Plane Data Constructor
    def _init_(self, origin, currLocation, status, destRunway):
        # origin where plane is spawned; this will be used to identify the plane rather than assigning
        # arbitrary numbers/values to each plane -> this will require ensuring that no 2 planes which
        # have spawned at the same spot are in the traffic control zone at the same time!
        self.origin = origin
        
        # last recorded location:
        self.currLocation = currLocation
        
        # indicates whether airplane is landing or holding:
        self.status = status
        
        # destination runway to land on, once signalled to do so:
        self.destRunway = destRunway

param = getParameters()
numRunways = param["numRunways"]
radiusZ = param["radiusZ"]

origin = air_traffic_control.generatePlane(param["radiusZ"])
currLocation = getPosition()
status = getStatus()

destRunway = destRunway(numRunways)

myPlane = Airplane(origin, currLocation, status, destRunway)
