import math
import queue
import generate_planes
import random

# create queue which will allow airplanes to land in FIFO (First In First Out) order
airplaneLandingWait = queue.Queue(maxsize = generate_planes.maxNumberOfPlanes(rZone, rHold))

# places item (in this case, list containing plane coordinates) into the above generated queue
def queueAirplane(item):
    airplaneLandingWait.put(item)

# remove and return airplane which is next up to land from queue
# inputs: numRunway = total number of runways available in the air traffic zone, runway = the runway
# at which the previous plane landed (number of runway determined by counting from 1 to numRunway, left
# to right)
# outputs: runway = this planes landing runway number will now inform the next planes landing,
# airplaneToLand = position of airplane which is directed to land
def getFromQueue(numRunway, runway):

    airplaneToLand = airplaneLandingWait.get()
    # if the previously plane landed at any runway which is not the last (ie: right-most runways), the 
    # next plane to land will land at the next runway over (ie: to the left)
    if (runway < numRunway):
        runway += 1

    # if we previously landed at the last runway (ie: left-most runway), the next plane will land at
    # the first runway (ie: right-most)
    else:
        runway = 1

    return runway

def readjust():
    #move away from nearest plane

def doNotCrash(safeDist):
    delta_x = #difference in x between all planes relative to eachother
    delta_y = #difference in y between all planes relative to eachother
    delta_r = #difference in r = math.isqrt((delta_x*delta_x)+(delta_y*delta_y)) between all planes relative to eachother

    if (delta_x and delta_y and delta_r > safeDist):
        #continue

    else:
        readjust()

