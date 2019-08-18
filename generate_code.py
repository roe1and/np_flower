import os
from PIL import Image

image = 'test.jpg'
im = Image.open(image)
pic = im.load()
print(range(im.size[1]))
image_rgb_values = []
print(im.size[0], im.size[1])

for x in range(im.size[0]):
    pixels = []
    #print(im.size[0])
    for y in range(im.size[1]):
        #print(im.size[1])
        pixels.append(pic[x, y])
        image_rgb_values.append(pic[x, y])
print(image_rgb_values)
print(len(image_rgb_values))
chunk_list = [image_rgb_values[i:i+16] for i in range(0, len(image_rgb_values), 16)]
with open('out.txt', 'w') as outfile:
    for i, rgb in enumerate(chunk_list):
        for j, pixel in enumerate(rgb):
            #strip.setPixelColor(1, 0, 111, 111);
            out_line = 'strip.setPixelColor({}, {}, {}, {});'.format(j, pixel[0], pixel[1], pixel[2])
            #print(j, pixel)
            outfile.write(out_line)
            outfile.write("\n")
        outfile.write('strip.show();')
        outfile.write("\n")
