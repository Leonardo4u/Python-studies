

def calculate_diameter_circle(radius):
    userinput_radius = float(input("Enter the radius of the circle: "))
    if userinput_radius < 0:
        return "Radius cannot be negative." 
    else:
        diameter = 2 * userinput_radius
        return f"The diameter of the circle with radius {userinput_radius} is {diameter}."
    
print(calculate_diameter_circle(0))