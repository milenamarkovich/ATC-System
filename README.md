# ATC-System
2D Air Traffic Control System

### The ATC system has the following features:
* Keeps track of all airplanes’ positions (latitude, longitude) within the traffic control zone.
The traffic control zone is a circle of radius 10km.
* Queues airplanes for landing based on time of arrival into the traffic control zone.
* Commands airplanes to go for landing (when it is their turn) to one of two runways.
* Otherwise commands airplanes to fly in a circular “holding pattern” which is a circle with
a radius of 1km around a suitable point.
* The ATC must never allow for planes to come within 100m of each other, whether
flying or landing.

### An airplane has the following characteristics:
* Assume each plane is a point.
* When an airplane appears/’spawns’ in the world, it does so at a random point on the
edge of the traffic control zone, and it travels towards the center of the zone.
* Airplanes travel at a speed of 140 m/s while flying. Assume that they instantaneously
stop and disappear when they reach the end of the landing strip.
* Airplanes automatically transmit their position (latitude, longitude) at a rate of 10 Hz to
the ATC system while flying. They stop transmitting their position once landed.
* When given a command from ATC to land at a specific runway, an airplane travels to the
base of the runway in a straight line. Once it reaches the base, it turns/changes angle
instantaneously to follow the path of the runway till the runway’s end. Its speed is the
same (140 m/s) throughout.

The dimensions of the runways are:
* width: 100m 
* length: 500m 
* seperation: 500m, equidistant from the center as shown in the diagram.

