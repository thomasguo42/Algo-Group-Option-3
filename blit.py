# I am more comfortable with python so I use python to implement this process.

# Define a function called blit to perform the process
def blit(src_pixels, src_width, src_height, dest_pixels, dest_width, dest_height, offsetX, offsetY, color_keys):
    # Iterate through the source image to locate and retrieve the color value of every pixel
    for x in range (src_width):
        for y in range (src_height):
            # Adjust the location in the destination buffer by the origin (offsetX and offsetY)
            dest_x = x + offsetX
            dest_y = y + offsetY

            # Assume starting at 0 (as this is what OpenCV does). If we want to start at 1, change y to (y-1) and dest_y to (dest_y-1)
            src_location = y * src_width + x
            dest_location = dest_y * dest_width + dest_x

            src_value = src_pixels[src_location]

            # Assume that color_keys is a list so we can skip multiple colors if we need
            if src_value not in color_keys:
                dest_pixels[dest_location] = src_value

    return dest_pixels
# test code

src_pixels = [0xFF000000, 0xFFFFFF00, 0xFFFF0000, 0xFF00FF00, 0xFFFFFFFF, 0xFF0000FF] # black, yellow, red, green, white, blue in a 2*3 source buffer
src_width = 2
src_height = 3

dest_pixels = [0xFF808080] * 25 # a grey 5*5 destination buffer
dest_width = 5
dest_height = 5

color_keys = {0xFF000000, 0xFFFF0000} # skip black and red

# Assume we starts at position (0, 0)
offsetX = 0
offsetY = 0

modified_dest_pixels = blit(src_pixels, src_width, src_height, dest_pixels, dest_width, dest_height, offsetX, offsetY, color_keys)

# print out the modified destination buffer for verification
for y in range(dest_height):
    row = modified_dest_pixels[y * dest_width:(y + 1) * dest_width]
    row_list = []
    for pixel in row:
        row_list.append(hex(pixel))
    print (row_list)

