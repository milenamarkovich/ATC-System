import air_traffic_control
class Flights:
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def append(self, new_plane):
        if self.head == None:
            self.head = new_plane
            self.tail = new_plane
        else:
            self.tail.next = new_plane
            self.tail = new_plane
    
    def searchPlanes(self, key):
        pos = 0
        cur_plane = self.head
        while cur_plane != None:
            if cur_plane.data == key:
                cur_plane.node_pos = pos
                return cur_plane
            cur_plane = cur_plane.next
            pos+=1