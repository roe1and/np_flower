import os
from PIL import Image

image = 'test.jpg'
im = Image.open(image)
pic = im.load()
# print(range(im.size[1]))
image_rgb_values = []
# print(im.size[0], im.size[1])

for x in range(im.size[0]):
    pixels = []
    #print(im.size[0])
    for y in range(im.size[1]):
        #print(im.size[1])
        pixels.append(pic[x, y])
        image_rgb_values.append(pic[x, y])
chunk_list = [image_rgb_values[i:i+4] for i in range(0, len(image_rgb_values), 4)]
image_rgb_values_copy1 = image_rgb_values.copy()

image_rgb_values1 = []
o = image_rgb_values_copy1.pop(0)

for v in image_rgb_values_copy1:
    image_rgb_values1.append(v)
image_rgb_values1.append(o)

#chunk_list = [image_rgb_values[i:i+4] for i in range(0, len(image_rgb_values), 4)]
#print(chunk_list)
#for i, rgb in enumerate(chunk_list):
#    print(rgb)

def move_over(l):
    return_list_copy = l.copy()
    return_list = []
    first = return_list_copy.pop()
    return_list.append(return_list_copy)
    return_list.append(first)
    return return_list

outfile = open('out.txt', 'w')

def output(num, inp):
    # print(inp)
    led = 0
    print(num, 'dammit')
    temp = []
    working = inp.copy()
    first = working.pop(0)
    # print(first)
    for a in working:
        temp.append(a)
    temp.append(first)
    for frame in working:
        # print(frame)
        for i in frame:
            line = 'setPixelColor({}, {});'.format(led, i)
            print(line)
            led += 1
    for j in first:        
        line = 'setPixelColor({});'.format(i)
        print(line)
    print('delay(100)')
    num -= 1

    if num == 14:
        return 1
    else:
        output(num, temp)
        #for f in frame:
        #    print(f)
    # print(temp)

print('before', chunk_list)
output(im.size[0], chunk_list)

'''
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
'''