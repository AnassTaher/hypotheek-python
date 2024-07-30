from PIL import Image, ImageDraw
from pdf2image import convert_from_path

pages = convert_from_path('doc1.pdf', 500)

for count, page in enumerate(pages):
    if count == 1:
        page.save(f'out1.jpg', 'JPEG')
        
im = Image.open("out1.jpg")


# print the width and height of the image
# (4134, 5847)
# (1241, 1754)

print(im.size)


# crop_rectangle = (810, 405, 1180, 650)
crop_rectangle = (2690, 1350, 3880, 2170)
cropped_im = im.crop(crop_rectangle)

rows = 9
columns = 6

print(cropped_im.size)
cell_width = cropped_im.size[0] // (columns)
cell_height = cropped_im.size[1] // (rows)

print(cell_width, cell_height)


# draw a grid




grid = [ [0]*columns for _ in range(rows) ]

# # Loop through each cell, check for each pixel if there is a color value < 100, if so mark it as 1
#
for i in range(rows):
    for j in range(columns):
        count = 0
        for x in range(cell_width):
            for y in range(cell_height):
                pixel = cropped_im.getpixel((j*cell_width + x, i*cell_height + y))
                # pixel returns a RGB tuple (r, g, b)
                is_black = True
                for p in pixel:
                    if p > 0:
                        is_black = False
                        break
                if is_black:
                    count = 1
        grid[i][j] = count

dict_info = {
    "data" : grid
}

import json
with open('data.json', 'w') as outfile:
    json.dump(dict_info, outfile)



cropped_im.show()
