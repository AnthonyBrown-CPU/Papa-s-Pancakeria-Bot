class Rect:
    
    def __init__(self, *args, **kwargs):
        if (len(args) == 1) and type(args[0]) == tuple:
            arg = args[0]
            self._x = arg[0]
            self._y = arg[1]
            self._width = arg[2]
            self._height = arg[3]
        elif (len(args) == 4) and all(isinstance(x, int) for x in args):
            self._x = args[0]
            self._y = args[1]
            self._width = args[2]
            self._height = args[3]
        elif (len(args) == 1) and type(args[0]) == Rect:
            self._x = args[0].x()
            self._y = args[0].y()
            self._width = args[0].width()
            self._height = args[0].height()
        else:
            # Invalid input arguments
            types = " ".join([type(x).__name__ for x in args])
            raise Exception("Rect initalized with invalid type(s):", types)
    
    def __repr__(self):
        return "<Rect (%s, %s, %s, %s)>" % (self._x, self._y, self._width, self._height)
    
    def __str__(self):
        return "<Rect (%s, %s, %s, %s)>" % (self._x, self._y, self._width, self._height)
    
    def left(self):
        return self._x
    
    def right(self):
        return self._x + self._width
        
    def top(self):
        return self._y
    
    def bottom(self):
        return self._y + self._height
    
    def width(self):
        return self._width
    
    def height(self):
        return self._height
    
    def x(self):
        return self._x
    
    def y(self):
        return self._y
    
    def setCoords(self, x1: int, y1: int, x2: int, y2: int):
        self._x = x1
        self._y = y1
        self._width = x2 - x1
        self._height = y2 - y1
        return self
    
    def setHeight(self, height: int):
        self._height = height
        return self
    
    def setRect(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        return self
        
    def setWidth(self, width: int):
        self._width = width
        return self
    
    def setX(self, x: int):
        self._x = x
        return self
    
    def setY(self, y: int):
        self._y = y
        return self
    
    def moveLeft(self, x: int):
        self._x = x
        return self
    
    def moveRight(self, x: int):
        self._x = x - self._width
        return self
    
    def moveTop(self, y: int):
        self._y = y
        return self
    
    def moveBottom(self, y: int):
        self._y = y - self._height
        return self
        
    def translate(self, dx: int, dy: int):
        self._x += dx
        self._y += dy
        return self