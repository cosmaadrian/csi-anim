import cv2

class Shape:
    def __init__(self, **kwargs):
        pass

    def draw(self, frame):
        raise Exception('Not implemented.')

    def set(self, attribute, value):
        self.__dict__[attribute] = value

class Circle(Shape):
    def __init__(self, position, radius, color = (255, 255, 255), thickness = 2, **kwargs):
        super().__init__(**kwargs)
        self.position = position
        self.radius = radius
        self.color = color
        self.thickness = thickness

    def draw(self, frame):
        return cv2.circle(frame, self.position, self.radius, self.color, self.thickness)
