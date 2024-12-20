class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Main program
def main():
    print("Choose a polygon to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rect = Rectangle(length, width)
        print(f"The area of the rectangle is: {rect.area()}")

    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        tri = Triangle(base, height)
        print(f"The area of the triangle is: {tri.area()}")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        circ = Circle(radius)
        print(f"The area of the circle is: {circ.area()}")

    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
