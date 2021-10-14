import math
import get_pos

def flyInCircle(v, r, f):
    angle = 0
    N = 100

    omega = v / r

    originX = get_pos.getPosition(f)[0] - r
    originY = get_pos.getPosition(f)[1] - r
    
    while airplaneLand == False :
        angle += omega
        x = originX + math.acos(angle + (math.pi/2)) * r * omega
        y = originX + math.asin(angle + (math.pi/2)) * r * omega

    position = [x,y]

    return position