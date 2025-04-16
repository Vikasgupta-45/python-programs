
#performed by maviya 

import math


class Circle:
    def __init__(self):
        self.radius = 0
    
    def get_radius(self):
        self.radius = float(input("Enter the radius of the circle: "))


class Area(Circle):
    def __init__(self):
        super().__init__()
    
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        print(f"Area of the circle: {area:.2f}")


class Volume(Area):
    def __init__(self):
        super().__init__()

    def calculate_volume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        print(f"Volume of the sphere: {volume:.2f}")


if __name__ == "__main__":
  
    sphere = Volume()

    
    sphere.get_radius()

   
    sphere.calculate_area()

  
    sphere.calculate_volume()