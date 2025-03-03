import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageDraw


def draw_circle():
    """Draws a circle using matplotlib."""
    fig, ax = plt.subplots()
    circle = plt.Circle((0.5, 0.5), 0.4, color='blue', fill=True)
    ax.add_patch(circle)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    plt.show()


def draw_rectangle():
    """Draws a rectangle using PIL."""
    img = Image.new('RGB', (200, 200), 'white')
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, 50, 150, 150], outline='red', width=5)
    img.show()


def draw_line():
    """Draws a line using OpenCV."""
    img = np.ones((200, 200, 3), dtype=np.uint8) * 255  # White image
    cv2.line(img, (50, 50), (150, 150), (0, 255, 0), 3)  # Green line
    cv2.imshow('Line', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
