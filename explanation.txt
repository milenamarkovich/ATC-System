# ATC System Walkthrough

## Functionality

### Generating planes at random along the edge of the air traffic control zone
To do this, I used python's random module to generate a random value, k, between 0 and 1, and thus generate a random angle, at which the point would spawn, theta = 2 * pi * k.
I then converted from polar coordinates to get x = rZone * cos(theta) and y = rZone * sin(theta). This function, generatePlane, also places the generated plane into a queue, 
and adds it to the flights list.

### Generating arbitrary number of planes up to maximum limit
The generatePlane function only executes while the number of planes inside the traffic zone is less than the calculated maximum number of planes in the zone. 
To make sure that all planes could execute a holding flight pattern without being within 100m of eachother, I used a 'smaller circle' radius of 1000m + (100/2)m, since 
this will allow the planes to fly in a circle and always be 100m from eachother.

### Changing parameters without changing the code
In order to do this, I added a user selection where you can choose to input unique parameters - this way you can change the problem parameters without changing the code.

### Basic flight towards centre.
After spawning, the aircraft flies linearly towards the centre of the traffic zone. In order to choose an appropriate origin point for the circular holding pattern, I set
the planes to fly in this basic flight pattern only until they reach an appropriate distance from the zone perimeter - where they can start circling. In order not to crowd the
runways, I set the planes to circle as far away from the centre as possible.

### Circlular holding pattern
In order to execute the circular holding pattern, I followed a similar logic to the generatingPlanes function, but converting the airplane speed to angular velocity and using
this value to increment the angle, theta, corresponding to the polar coordinates (which are then converted to cartesian coordinates, per the above method).

### FIFO queue
I used a queue to store the generated planes in FIFO order, and used the queue.get() function to pop out the next plane to be signalled for landing.

### Deciding where to land
In order to choose an appropriate runway, I cycled through the available runways from left to right - this way there is more time for the landing plane to move down the runway
before the next plane approaches, thus avoiding collisions.

### Approaching for landing, and moving down the runway
I followed the same logic used for the basic flight pattern, however this time setting my destination to be the centre of the destination runway (width/2). Similarly,
I had the airplane move down the runway in a straight line (only incrementing y, holding x constant), until it reached the end of the runway.

### Airplane disappears at the end of the runway
In order to 'disappear' the airplane, I simply cleared the memory associated with its object.

### Avoiding collision
In order to check whether the airplane was within 100m of other planes, I checked the difference in x, y and diagonal directions. If the difference was less than 100m, I re-
adjusted the plane by 1 in the direction opposite of the 'threat' airplane. This could likely be made more accurate by having a circular zone, of radius = (100/2)m, around 
the airplane and detecting when another airplanes zone overlaps. 

## Follow-up Questions

### What is the best way to transmit messages between the airplanes and the ATC?
TCAS (Traffic Collision Avoidance Systems) work by continuosly querying the bearing, distance and altitude of nearby aircrafts. In order to not mix up signals, each aircraft
calls on a given frequency and ends their communication before receiving a response. This is the best way to ensure that the TCAS system communicates wwith the surrounding 
aircrafts accurately.

### What is the best way for the ATC to set holding patterns and paths for the planes such that they will not come too close to eachother?
The best way for the ATC to set holding patterns and paths for the planes is to map out a path for each newly spawned plane before spawning the next one.
