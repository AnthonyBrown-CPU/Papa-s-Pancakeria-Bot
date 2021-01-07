import time

from constants import *
from win_control import *
from sum_area import *
from order import *
from station_changer import *

class Drink():
    def __init__(self, flavour, size, additional):
        self.flavour = flavour
        self.size = size
        self.additional = additional
    
    def __repr__(self):
        return "<Drink %s %s %s>" % (self.flavour, self.size, self.additional)
        
    def __str__(self):
        return "<Drink %s %s %s>" % (self.flavour, self.size, self.additional)
    
class DrinksStation():

    def __init__(self, station_chngr):
        self.station = station_chngr

    def make_drink(self, order):
        is_tutorial = False
        
        if order.drink is None:
            print("Order has no drink!")
            return
    
        drink = order.drink
        self.station.change(STATION.DRINK)
        time.sleep(1)
        
        if sumArea(Area.drink_check) == GUISum.drinks_tutorial:
            print("TUTORIAL_DETECT")
            is_tutorial = True
        
        # Flavour
        print("FLAVOUR")
        clickPos(Coor.d_flav[drink.flavour]) 
        time.sleep(.3)
        
        # Cup size
        print("CUP SIZE")
        clickPos(Coor.d_size[drink.size])
        time.sleep(.7)
        
        # Timing click
        print("POUR")
        clickPos(Coor.d_pour_btn)
        time.sleep(.2)
        clickPos(Coor.d_pour_btn)
        time.sleep(3)
        
        # Milk
        print("ADDITIONAL")
        clickPos(Coor.d_add[drink.additional])
        time.sleep(.55)
        
        # Timing click
        print("POUR")
        clickPos(Coor.d_pour_btn)
        
        if is_tutorial:
            time.sleep(2)
            clickPos(Coor.d_my_drinks)
            time.sleep(.5)
            clickPos(Coor.d_my_drinks)
        
        order.drink_made = True