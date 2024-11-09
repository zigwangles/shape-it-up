import random

def generate_triangle():
    size = random.randint(3, 8)
    triangle = ""
    for i in range(1, size + 1):
        triangle += " " * (size - i) + "*" * (2 * i - 1) + "\n"
    return triangle

def generate_rectangle():
    width = random.randint(4, 8)
    height = random.randint(2, 5)
    rectangle = ""
    for _ in range(height):
        rectangle += "*" * width + "\n"
    return rectangle

def generate_diamond():
    size = random.randint(3, 5)
    diamond = ""
    for i in range(size):
        spaces = " " * (size - i)
        stars = "*" * (2 * i + 1)
        diamond += spaces + stars + "\n"
    for i in range(size - 2, -1, -1):
        spaces = " " * (size - i)
        stars = "*" * (2 * i + 1)
        diamond += spaces + stars + "\n"
    return diamond

def generate_hexagon():
    base = random.randint(3, 5)
    hexagon = ""
    for i in range(base):
        spaces = " " * (base - i)
        stars = "*" * (base + 2 * i)
        hexagon += spaces + stars + "\n"
    for i in range(base - 2, -1, -1):
        spaces = " " * (base - i)
        stars = "*" * (base + 2 * i)
        hexagon += spaces + stars + "\n"
    return hexagon

def generate_shape(shape_type):
    if shape_type == "triangle":
        return generate_triangle()
    elif shape_type == "rectangle":
        return generate_rectangle()
    elif shape_type == "diamond":
        return generate_diamond()
    elif shape_type == "hexagon":
        return generate_hexagon()
    else:
        return "Unknown shape!"

def main():
    while True:
        shape_type = input("Enter the shape you want to generate (triangle/rectangle/diamond/hexagon) or 'exit' to stop: ").strip().lower()
        if shape_type == "exit":
            break
        shape_art = generate_shape(shape_type)
        print("\nGenerated ASCII Art:")
        print(shape_art)

if __name__ == "__main__":
    main()