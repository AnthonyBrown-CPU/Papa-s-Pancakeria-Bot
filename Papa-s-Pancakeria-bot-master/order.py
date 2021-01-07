from enum import Enum

ORDER_PHASE = Enum('ORDER_PHASE', 'WAITING COOKING COOKED BUILT')

class Order():
    
    def __init__(self, ingredients, grillsNeeded, ironsNeeded, drink = None):
        self.ingredients = ingredients
        self.num_of_grills = grillsNeeded
        self.num_of_irons = ironsNeeded
        self.drink = drink
        self.drink_made = False
        
        self.phase = ORDER_PHASE.WAITING
        self.flipped = False
        self.id = -1
        
        self.cook_start_time = 0
    
    
        self.allocated_grills = []
        self.allocated_irons = []
    
    def has_drink(self):
        return self.drink != None
    
    def ready(self):
        is_built = self.phase is ORDER_PHASE.BUILT
        drink_ready = self.drink == None or self.drink_made is True
    
        return is_built and drink_ready
    

def get_order_by_id(orders, id):
    for order in orders:
        if order.id == id:
            return order
    
    return None