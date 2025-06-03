# Autora: M Luz Tappero
# Descripción del problema: Crear una clase llamada Punto que permita trabajar con coordenadas (x,y) para calcular la posición dentro de los cuadrantes, el vector entre dos puntos y la distancia entre ellos.
# Input: coordenadas (X, Y) de puntos.
# Output: impresión del punto, cuadrante al que pertenece, vector entre puntos y distancia entre ellos.

import math

# Definition of the class Point
class Point:
    """
    Class that represents a point in a 2D space with coordinates (x, y).
    It includes methods to determine the quadrant, calculate the vector to another point, and calculate the distance between two points.
    """
    # Constructor method of the class Point, which initializes the coordinates x and y. If no coordinates are provided, they default to 0.
    def __init__(self, x: float = 0, y: float = 0):
        "Initializes the Point object with coordinates x and y. If not provided, defaults to 0."
        if not self.is_valid(x) or not self.is_valid(y):
            raise ValueError("Invalid coordinates: Coordinates must be numbers and not NaN or infinite.")
        self.x = x
        self.y = y

    #Definition of the __str__ method to represent the point in a readable format.
    # This method is called when the object is printed, and it returns a string representation of the coordinates.
    def __str__(self):
        "Returns a string representation of the point in the format (x, y)."
        return f"({self.x}, {self.y})"
        
    # Definition of the Quadrant method that indicates which quadrant the point belongs to.
    def quadrant(self):
        " Returns the quadrant of the point based on its coordinates."
        if self.x > 0 and self.y > 0:
            return "Quadrant I"
        elif self.x < 0 and self.y > 0:
            return "Quadrant II"
        elif self.x < 0 and self.y < 0:
            return "Quadrant III"
        elif self.x > 0 and self.y < 0:
            return "Quadrant IV"
        elif self.x == 0 and self.y != 0:
            return "Y axis"
        elif self.y == 0 and self.x != 0:
            return "X axis"
        else:
            return "Origin"

    # Definition of the Vector method, whose parameters are another pair of coordinates (x2, y2) and which calculates the vector joining the two points.
    def vector_str(self, point2):
        "Returns a string representation of the vector from this point to another point."
        return f"({point2.x - self.x}, {point2.y - self.y})\n"

    # Definition of the method Distancia, whose parameters are another pair of coordinates (x2, y2) and which calculates the distance between the two points.
    def distancia(self, point2):
        " Calculates the distance between this point and another point."
        distance = math.sqrt((point2.x - self.x)**2 + (point2.y- self.y)**2)
        print(f"-The distance between {self} and {str(point2)} is: {distance:.2f}\n")

    # Definition of the is_valid method to check if the given value is a valid coordinate (neither NaN or infinite).
    @staticmethod
    def is_valid(value):
        """Checks if the given value is a valid coordinate (neither NaN nor infinite)."""
        return isinstance(value, (int, float)) and not (value != value or value == float('inf') or value == -float('inf'))


# Function to get a point from user 
def get_point(name):
    # Maximum number of attempts allowed for user input
    """
    Asks the user to input the coordinates of a point.
    Args:
        name (str): The name of the points to display.
    Returns:
        Point: A Point object with the entered coordinates.
    Raises:
        ValueError: If the user fails to provide valid input after the maximum retries.
    """
    max_retries = 5
    retries = 0
    while retries < max_retries:
        try:
            x = float(input(f"Enter the X coordinate of {name}: "))
            y = float(input(f"Enter the Y coordinate of {name}: "))
            if x==0 and y==0:
                print("Invalid entry. Coordinates cannot be both zero.")
                retries += 1
                continue
            return Point(x, y)
        except ValueError:
            retries += 1
            print(f"Invalid entry. Please enter valid numbers. Attempts left: {max_retries - retries}")
    print("Maximum retry limit reached. Unable to get valid input for the point.")
    return None


# Main program
def main():
    print("COORDINATE INPUT")
    p1 = get_point("Point 1")
    p2 = get_point("Point 2")

    print("\n**RESULTS**")
    # Show the coordinates and quadrants of the points
    if p1 is None or p2 is None:
        print("Error: One or both points have invalid input. No calculations will be performed.")
    else:
        for i, point in enumerate([p1, p2], start=1):
            print(f"\n-Point {i}: {point} - {point.quadrant()}")
        
        # Vector and distance calculations
        if p1.x != p2.x or p1.y != p2.y:
            print(f"\n-Vector from {p1} to {p2}: {p1.vector_str(p2)}")
            p1.distancia(p2)
        else:
            print("Points are identical. No vector or distance calculation performed.")


if __name__ == "__main__":
    main()
