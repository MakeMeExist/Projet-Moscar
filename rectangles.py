class Rectangle:

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def __repr__(self):  # Considérer que cette méthode est __str___
        return f"Rectangle - left : {self.left}, top : {self.top}, width : {self.width}, height : {self.height}"

    def __contains__(self, item):
        # item est un tuple composé des coordonnées d'un point (x,y)
        x, y = item
        '''
        x = item[0]
        y = item[1]
        '''
        return self.left <= x <= self.left + self.width and self.top <= y <= self.top + self.height

    def __add__(self, other):
        left = min(self.left, other.left)
        top = min(self.top, other.top)
        right = max(self.left + self.width, other.left + other.width)
        bottom = max(self.top + self.height, other.top + other.height)
        return Rectangle(left, top, right - left, bottom - top)

    def __mul__(self, other):
        left = max(self.left, other.left)
        top = max(self.top, other.top)
        right = min(self.left + self.width, other.left + other.width)
        bottom = min(self.top + self.height, other.top + self.height)
        if right < left or bottom < left:
            return None
        else:
            return Rectangle(left, top, right - left, bottom - top)

    def collision(self, other):
        left = max(self.left, other.left)
        top = max(self.top, other.top)
        right = min(self.left + self.width, other.left + other.width)
        bottom = min(self.top + self.height, other.top + self.height)
        if right < left or bottom < left:
            return False
        else:
            return True
