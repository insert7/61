#Bresenham's line drawing algorithm
import matplotlib.pyplot as plt

def draw_line(x0, y0, x1, y1):
    # Calculate differences
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    # Determine the direction of the line
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    # Initialize error term
    error = dx - dy
    # Starting point
    x, y = x0, y0
    # List to store the points of the line
    line = []

    # Bresenham's line algorithm
    while True:
        line.append((x, y))  # Add current point to the line
        if x == x1 and y == y1:  # If end point is reached, break
            break
        e2 = 2 * error
        if e2 > -dy:  # Adjust error term and position for x direction
            error -= dy
            x += sx
        if e2 < dx:  # Adjust error term and position for y direction
            error += dx
            y += sy

    return line

# Example usage: Drawing a line from (1, 1) to (7, 7)
x0, y0, x1, y1 = 1, 1, 7, 7
line = draw_line(x0, y0, x1, y1)

# Extract x and y values from the line points
x_values, y_values = zip(*line)

# Plot the line using matplotlib
plt.plot(x_values, y_values, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line Drawing')
plt.grid(True)
plt.show()