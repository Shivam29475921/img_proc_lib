from image_processor import PPMImage
import math


def rotate_ppm(image, angle, clockwise=True):
    theta = math.radians(angle % 360)
    width, height = image.width, image.height
    x0 = width // 2
    y0 = height // 2
    rotated_pixels = [(0, 0, 0)] * (width * height)
    if clockwise:
        for y in range(height):
            for x in range(width):

                new_x = int(math.cos(theta) * (x - x0) - math.sin(theta) * (y - y0) + x0)
                new_y = int(math.sin(theta) * (x - x0) + math.cos(theta) * (y - y0) + y0)

                if 0 <= new_x < width and 0 <= new_y < height:
                    rotated_pixels[new_y * width + new_x] = image.pixels[y * width + x]

    else:
        for y in range(height):
            for x in range(width):

                new_x = int(math.cos(theta) * (x - x0) + math.sin(theta) * (y - y0) + x0)
                new_y = int(-math.sin(theta) * (x - x0) + math.cos(theta) * (y - y0) + y0)

                if 0 <= new_x < width and 0 <= new_y < height:
                    rotated_pixels[new_y * width + new_x] = image.pixels[y * width + x]
    return PPMImage(width=width, height=height, max_color=image.max_color, pixels=rotated_pixels)


def resize_ppm(image, new_width, new_height):
    pixels = image.pixels
    resized_pixels = []
    x_ratio = image.width / new_width
    y_ratio = image.height / new_height

    for i in range(new_height):
        for j in range(new_width):
            x = int(j * x_ratio)
            y = int(i * y_ratio)
            resized_pixels.append(pixels[y * image.width + x])

    return PPMImage(new_width, new_height, image.max_color, resized_pixels)


def flip_horizontally(image):
    pass

def flip_vertically(image):
    pass


