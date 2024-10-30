from image_processor import *

# image = PPMImage.read_ppm('sample_images/sample.ppm')
# image.draw_ppm()
#
#
# rotated_image2 = rotate_image(image, 270)
# rotated_image2.write_ppm('sample_images/rotated2.ppm')
#

# image = PPMImage.generate_random_ppm(width=100, height=100)
# image.write_ppm('sample_images/sample_white.ppm')
#
# rotated_image1 = rotate_ppm(image, 30, clockwise=False)
# rotated_image1.write_ppm('sample_images/rotated1.ppm')
#
# image_cropped = resize_ppm(image, new_width=1500, new_height=150)
# image_cropped.write_ppm('sample_images/sample_resized.ppm')
# #
# image = invert_filter(image)
# image.write_ppm('sample_images/sample_invert.ppm')

# grayscale_image = grayscale_filter(image)
# grayscale_image.write_ppm('sample_images/grayscale.ppm')

# bright_image = adjust_brightness(image, 1.5)
# bright_image.write_ppm("sample_images/sample3.ppm")

PPMImage.jpg_to_ppm('sample_images/download.jpeg', 'sample_images/download2.ppm')
image = PPMImage.read_ppm('sample_images/download2.ppm')
invert_filter(image).write_ppm('sample_images/inverted.ppm')
