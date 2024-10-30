from image_processor import PPMImage


def grayscale_filter(image):
    gray_pixels = []

    for r, g, b in image.pixels:
        gray = int((r + g + b) / 3)
        gray_pixels.append((gray, gray, gray))
    return PPMImage(image.width, image.height, image.max_color, gray_pixels)


def invert_filter(image):
    inverted_pixels = []
    max_pixel = image.max_color
    for r, g, b in image.pixels:
        inverted_pixels.append((
            max_pixel - r,
            max_pixel - g,
            max_pixel - b
        ))
    return PPMImage(image.width, image.height, image.max_color, inverted_pixels)


def adjust_brightness(image, factor):
    adjusted_brightness_pixels = []

    for r, g, b in image.pixels:
        adjusted_brightness_pixels.append((
            min(int(r * factor), 255),
            min(int(g * factor), 255),
            min(int(b * factor), 255),
        ))
    return PPMImage(image.width, image.height, image.max_color, adjusted_brightness_pixels)
