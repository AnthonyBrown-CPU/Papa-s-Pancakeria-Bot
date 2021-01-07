import time, math

from constants import *
from win_control import *
from sum_area import *
from order import *
from station_changer import *

class BuildStation():
    
    def __init__(self, station_chngr):
        self.order_ready = False
        self.active_order = None
        self.drink_queue = []
        self.station = station_chngr
    
    
    def build_pancake(self, order):
        if self.order_ready:
            print("Cannot make pancake, another is ready to serve")
            return
        
        print("Building Pancake for order %s" % order.id)
        print(order.ingredients)
        
        #Go to build station
        self.station.change(STATION.BUILD)

        #build pancake
        for ingredient in order.ingredients:
            
            item_name = ingredient[0]
            item_type = IngredientTypes[item_name][0]
            
            if item_type in ('bread', 'waffle'):
                self.add_base()
            elif item_type == 'piece':
                item_count = ingredient[1]
                self.spread_pieces(item_name, item_count)
            else:
                self.spread_sprinkle_or_sauce(item_name)
        
        #Wait for animations to finish
        time.sleep(.5)
        order.phase = ORDER_PHASE.BUILT
        self.order_ready = True
        self.active_order = order
        
    
    def serve_pancake(self):        
        
        order_id = self.active_order.id
        
        self.station.change(STATION.BUILD)

        # Finish
        clickPos(Coor.build_finish)
        time.sleep(.2)
        
        # Place drink
        if self.active_order.has_drink() and self.active_order.drink_made:
            drink_i = self.drink_queue.index(order_id)
            BuildStation.place_drink(drink_i)
            self.drink_queue.remove(order_id)

        # Give to customer
        BuildStation.move_ticket_to_tray(order_id)
        
        self.active_order = None
        self.order_ready = False
        
        return order_id
 
    def add_drink(self, order):
        self.drink_queue.append(order.id)
 
    @staticmethod
    def place_drink(drink_i):
        drink_coor = Coor.drink_rack[drink_i]
        time.sleep(1)
        mousePos(drink_coor)
        leftDown()
        mousePos(Coor.build_tray)
        leftUp()
    
    @staticmethod
    def move_ticket_to_tray(order_id):
        mousePos((Coor.line_first_slot[0] + (Coor.line_spacing * order_id), Coor.line_first_slot[1]))
        leftDown()
        mousePos(Coor.build_tray)
        leftUp()
        
    
    @staticmethod
    def get_point_in_ellipse(x, y, theta):
        xPos = x * math.cos(math.radians(theta))
        yPos = y * math.sin(math.radians(theta))
        return int(math.floor(xPos)), int(math.floor(yPos))
        
    @staticmethod
    def get_point_in_flower(r_max, theta):
        r = r_max * math.cos((5/3) * math.radians(theta))
        x = r * math.cos(math.radians(theta))
        y = r * math.sin(math.radians(theta))
        
        return int(x), int(y)
    
    
    @staticmethod
    def add_base():
        mousePos(Coor.build_base)
        leftDown()
        mousePos((Coor.build_center[0] - 20, Coor.build_center[1]))
        leftUp()
        time.sleep(.3)
            
    @staticmethod
    def spread_pieces(ingred_name, toppings_num):
        
        ingred_type = IngredientTypes[ingred_name][0]
        ingred_pos = IngredientTypes[ingred_name][1]
        
        if(ingred_type != 'piece'):
            raise Exception("spread_pieces: ingredient not a piece")
        
        if toppings_num == 1:
            # Place in the center
            mousePos(ingred_pos)
            leftDown()
            mousePos(Coor.build_center)
            time.sleep(.2)
            leftUp()
            time.sleep(.2)
        else:
            #Step 1: Divide 360 degrees by number of toppings
            increment = 360 / toppings_num
            #Step 2: Hope.
            for x in range(0, toppings_num):
                offset = 45
            
                mousePos(ingred_pos)
                leftDown()
                time.sleep(.1)
                x, y = BuildStation.get_point_in_ellipse(45, 45, (x*increment)+offset)
                #print ('Placing topping at '+str(x)+', '+str(y)+' from pancake center')
                mousePos((Coor.build_center[0]+x, Coor.build_center[1]+y))
                time.sleep(.1)
                leftUp()
                
            time.sleep(.2)
    
    @staticmethod
    def spread_sprinkle_or_sauce(ingred_name):
        # Sprinkle or Sauce, flower pattern
        ingred_type = IngredientTypes[ingred_name][0]
        ingred_pos = IngredientTypes[ingred_name][1]
        duration = IngredientTypes[ingred_name][2]
        
        if(ingred_type not in ('sauce', 'sprinkle')):
            raise Exception("spread_sprinkle_or_sauce: invalid ingredient", ingred_name)
        
        degrees = 560
        points = 100
        
        increment = degrees / points
        delay = duration / points
        
        mousePos(ingred_pos)
        leftDown()
        for i in range(0, points):
            time.sleep(delay)
            x, y = BuildStation.get_point_in_flower(60, i*increment)
            #print ('Placing sprinkle/sauce at '+str(x)+', '+str(y)+' from pancake center')
            mousePos((Coor.build_center[0] + x, Coor.build_center[1] + y))
            leftUp(delay=0) # Move to first position and start placing
            
        #Buffer
        time.sleep(.2)
            
            
            
if __name__ == "__main__":
    import sys
    BuildStation.spread_topping(sys.argv[1])