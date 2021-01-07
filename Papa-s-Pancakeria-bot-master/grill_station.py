import time

from constants import *
from win_control import *
from sum_area import *
from order import *
from station_changer import *

FIRST_DAY_COOK_TIME = 16
DEFAULT_COOK_TIME = 34

class GrillStation():
    
    grills = [True, True, True, True, True, True, True, True]
    irons = [True, True, True, True]
    finished_queue = []
    
    IRON = 0
    GRILL = 1
    
    def __init__(self, station_chngr, cook_time = DEFAULT_COOK_TIME):
        self.cook_time = cook_time
        self.station = station_chngr
        
    def can_do_order(self, order):
        #if the number of grills and irons available is greater than the required from order info, return true
        if self.grills.count(True) >= order.num_of_grills and self.irons.count(True) >= order.num_of_irons:
            return True
        return False
        
    def do_order(self, order):
        self.station.change(STATION.GRILL)
        #place batters on grill, and the extras        
        
        self.allocate_grills(order)
        self.allocate_irons(order)
        
        print(order.allocated_grills)
        print(order.allocated_irons)
        
        grill_it = 0
        iron_it  = 0
        
        for ingredient in order.ingredients:
            
            ingredient_name = ingredient[0]
            if ingredient_name not in ('pancake', 'french', 'waffle'):
                continue
                
            if len(ingredient) == 2:
                topping = ingredient[1]
            else:
                topping = None
            
            if ingredient_name in ('pancake', 'french'):
                grill_slot = order.allocated_grills[grill_it]
                grill_it += 1
                self.place_ingredient(self.GRILL, ingredient_name, grill_slot)
                if topping is not None:
                    self.place_ingredient(self.GRILL, topping, grill_slot)
            
            if ingredient_name in ('waffle'):
                iron_slot = order.allocated_irons[iron_it]
                iron_it += 1
                self.place_ingredient(self.IRON, ingredient_name, iron_slot)
                if topping is not None:
                    self.place_ingredient(self.IRON, topping, iron_slot)
        
        order.cook_start_time = time.time()
        order.phase = ORDER_PHASE.COOKING
        print("Order %s has started cooking" % order.id)
        
    def check_orders(self, orders):
        for order in orders:
            if order.phase != ORDER_PHASE.COOKING:
                continue
        
            if order.cook_start_time + self.cook_time <= time.time():
                #Go to grill
                self.station.change(STATION.GRILL)
                
                if order.flipped == False:
                #Flip Pancakes
                    print ('Flipping order '+str(order.id))
                    for slot in order.allocated_grills:
                        self.flip(self.GRILL, slot)
                    for slot in order.allocated_irons:
                        self.flip(self.IRON, slot)
                    order.cook_start_time = time.time()
                    order.flipped = True

                elif order.flipped == True:
                #Pancakes are cooked
                    print("Order", str(order.id), "has finished cooking")
                    for item in order.ingredients:
                        if item[0] in ('pancake', 'french'):
                            slot = order.allocated_grills.pop()
                            self.finish_cooking(self.GRILL, slot)
                            self.grills[slot] = True
                        
                        if item[0] in ('waffle'):
                            slot = order.allocated_irons.pop()
                            self.finish_cooking(self.IRON, slot)
                            self.irons[slot] = True
                        
                    order.phase = ORDER_PHASE.COOKED
                    self.finished_queue.append(order.id)
                    time.sleep(.4)
                
    def flip(self, type, slot):
        if(type == self.GRILL):
            clickPos(Coor.grill[slot], delay=0.1)
            print("Flipping grill", slot+1)
        elif(type == self.IRON):
            clickPos(Coor.iron[slot], delay=0.1)
            print("Flipping iron", slot+1)
    
    def allocate_grills(self, order):
        allocated_grills = []
        
        for i in range(0, 8):
            if len(allocated_grills) == order.num_of_grills:
                break
            if self.grills[i] == True:
                allocated_grills.append(i)
                self.grills[i] = False
            
                
        order.allocated_grills = allocated_grills

    def allocate_irons(self, order):
        allocated_irons = []
        
        for i in range(0, 4):
            if len(allocated_irons) == order.num_of_irons:
                break
            if self.irons[i] == True:
                allocated_irons.append(i)
                self.irons[i] = False
            
                
        order.allocated_irons = allocated_irons
    
    def place_ingredient(self, type, ingredient, slot):
        print ('Placing %s at slot %s' % (ingredient, slot))
        mousePos(IngredientTypes[ingredient][1])
        time.sleep(.4)
        leftDown()
        if type == self.GRILL:
            mousePos(Coor.grill[slot])
        elif type == self.IRON:
            mousePos(Coor.iron[slot])
        time.sleep(.1)
        leftUp()    
    
    def finish_cooking(self, type, slot):
        if type == self.GRILL:
            mousePos(Coor.grill[slot])
        elif type == self.IRON:
            mousePos(Coor.iron[slot])
        time.sleep(.1)
        leftDown()
        mousePos(Coor.gril_confirm)
        time.sleep(.1)
        leftUp()

    def pancakes_ready(self):
        #print("%s pancake orders ready" % len(self.finished_queue))
        return len(self.finished_queue) != 0