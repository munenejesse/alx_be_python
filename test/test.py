class shape:
    def calculate_area(self):
        return 0
class rectange(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height
    
#usage
rect = rectange(4,5)
 print(rect)