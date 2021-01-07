import time
from enum import Enum

from win_control import *

STATION = Enum('STATION', 'ORDER GRILL BUILD DRINK')

class StationChanger():

    def __init__(self):
        self.current = STATION.ORDER

    def change(self, station):        
        # No need to change station if we are already there
        if station == self.current:
            return
        
        if station == STATION.ORDER:
            clickPos(Coor.s_order)
        elif station == STATION.GRILL:
            clickPos(Coor.s_grill)
        elif station == STATION.BUILD:
            clickPos(Coor.s_build)
        elif station == STATION.DRINK:
            clickPos(Coor.s_drink)
        else:
            raise Exception("Tried to switch to non-existent station with ID:", station)
            
        self.current = station
            
        print("Changing to station ", STATION(station).name)
        
        #Time it takes to transition between stations
        time.sleep(.5)