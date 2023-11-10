def area_triangle(base, height):
    try:
        if base >= 0 and height >= 0:
            area_tri = 0.5 * base * height
            return area_tri
        else:
            raise ValueError("Height and base must be non-negative numbers.")
        
    except ValueError as s:
        return str(s)