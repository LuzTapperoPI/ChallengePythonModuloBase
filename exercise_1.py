# Autora: M Luz Tappero
# Descripción del problema: calcular distancia, base y altura de un rectángulo a partir de dos puntos de coordenadas (x,y) que forman la diagnonal del rectángulo.
# Input: coordenadas (X, Y) de puntos.
# Output: impresión del resultado de distancia entre ambos puntos, base y altura del rectángulo.

import math

# Function to get points from the user.
def get_point(prompt):
    """
    Get pair of points from the user.
    """
    while True:
        try:
            point = input(prompt)
            x, y= map(float, point.split(','))
            return x, y
        except ValueError:
            print("Invalid input. Please enter a point in the format 'x,y'.\n")

# Function to calculate the distance between two points.
def calculate_distance(point1, point2):
    """
    Calculate the distance between two points in a 2D space.
    """
    # Equation: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    message = f"The diagonal distance between points {point1} and {point2} is: {distance:.2f}\n"
    print(message)
    return distance

# Function to calculate the height of the rectangle formed by two points.
def calculate_rectangle_height(point1, point2):
    """
    Calculate the height of the rectangle formed by two points.
    """
    # Equation: abs(y2 - y1)
    height = abs(point2[1] - point1[1])
    print(f"The height of the rectangle, calculated from points {point1} and {point2}, is: {height}\n")
    return height

# Function to calculate the base of the rectangle formed by two points.
def calculate_rectangle_base(point1, point2):
    """
    Calculate the base of the rectangle formed by two points.
    """
    # Equation: abs(x2 - x1)
    base = abs(point2[0] - point1[0])
    print(f"The base of the rectangle, calculated from points {point1} and {point2}, is: {base}\n")
    return base

# Function to calculate the area of the rectangle using base and height.
def calculate_rectangle_area(base, height):
    """
    Calculate the area of the rectangle using base and height.
    """
    # Equation: base * height
    area = base * height
    print(f"The area of the rectangle formed by points is: {area}\n")
    return area

# Main function to execute the program.
def main():
    point1= get_point("Enter the first point in format x,y: ")
    point2= get_point("Enter the second point in format x,y: ")

    calculate_distance(point1, point2)
    height = calculate_rectangle_height(point1, point2)
    base = calculate_rectangle_base(point1, point2)
    calculate_rectangle_area(base, height)

if __name__ == "__main__":
    main()
