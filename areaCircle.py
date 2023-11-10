import math

def area_circle(radius):
    try:
        if isinstance(radius, int) and radius > 0:
            area = math.pi * (radius ** 2)
            return area
        else:
            raise ValueError("Input radius must be positive integer.")
    except ValueError as s:
        return str(s)