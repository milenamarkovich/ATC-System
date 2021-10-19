import math

###################################################################################################
#AIRPLANE CLASS#

class PlaneNode(object) :
    # Plane Data Constructor
    def __init__(self, origin, currLocation, status, destRunway):
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

