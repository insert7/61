import matplotlib.pyplot as plt

def bresenham(x1, y1, x2, y2):
    points = []
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx, sy = (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points

def draw_line(x1, y1, x2, y2):
    line_points = bresenham(x1, y1, x2, y2)
    x_coords, y_coords = zip(*line_points)
    
    plt.plot(x_coords, y_coords, marker='o', color='blue')
    plt.title("Bresenham's Line Drawing Algorithm")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

# Define the endpoints
x1, y1 = 1, 1
x2, y2 = 5, 5

# Draw the line
draw_line(x1, y1, x2, y2)
