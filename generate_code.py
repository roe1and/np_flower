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
'''
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
'''

def output(num, inp):
    # print(inp)
    led = 0
    # print(num, 'dammit')
    temp = []
    working = inp.copy()
    first = working.pop(0)
    # print(first)
    for a in working:
        temp.append(a)
    temp.append(first)
    # print(temp)

    '''
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
    '''
    num -= 1

    if num == 0:
        back =  {'a': 0, 'b': 4, 'c': 8, 'd': 12, 'num': 0}
        l3 =    {'a': 1, 'b': 5, 'c': 9, 'd': 13, 'num': 1}
        l2 =    {'a': 2, 'b': 6, 'c': 10, 'd': 14, 'num': 2}
        front = {'a': 3, 'b': 7, 'c': 11, 'd': 15, 'num': 3}

        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['a'], temp[back['a']][back['num']][0], temp[back['a']][back['num']][1], temp[back['a']][back['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['b'], temp[back['b']][back['num']][0], temp[back['b']][back['num']][1], temp[back['b']][back['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['c'], temp[back['c']][back['num']][0], temp[back['c']][back['num']][1], temp[back['c']][back['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['d'], temp[back['d']][back['num']][0], temp[back['d']][back['num']][1], temp[back['d']][back['num']][2])
        print(line)
        
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['a'], temp[l2['a']][l2['num']][0], temp[l2['a']][l2['num']][1], temp[l2['a']][l2['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['b'], temp[l2['b']][l2['num']][0], temp[l2['b']][l2['num']][1], temp[l2['b']][l2['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['c'], temp[l2['c']][l2['num']][0], temp[l2['c']][l2['num']][1], temp[l2['c']][l2['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['d'], temp[l2['d']][l2['num']][0], temp[l2['d']][l2['num']][1], temp[l2['d']][l2['num']][2])
        print(line)

        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['a'], temp[l3['a']][l3['num']][0], temp[l3['a']][l3['num']][1], temp[l3['a']][l3['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['b'], temp[l3['b']][l3['num']][0], temp[l3['b']][l3['num']][1], temp[l3['b']][l3['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['c'], temp[l3['c']][l3['num']][0], temp[l3['c']][l3['num']][1], temp[l3['c']][l3['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['d'], temp[l3['d']][l3['num']][0], temp[l3['d']][l3['num']][1], temp[l3['d']][l3['num']][2])
        print(line)

        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['a'], temp[front['a']][front['num']][0], temp[front['a']][front['num']][1], temp[front['a']][front['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['b'], temp[front['b']][front['num']][0], temp[front['b']][front['num']][1], temp[front['b']][front['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['c'], temp[front['c']][front['num']][0], temp[front['c']][front['num']][1], temp[front['c']][front['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['d'], temp[front['d']][front['num']][0], temp[front['d']][front['num']][1], temp[front['d']][front['num']][2])
        print(line)
        
        print('strip.show();')
        print('delay(111);')
        return 1
    else:
        back =  {'a': 0, 'b': 4, 'c': 8, 'd': 12, 'num': 0}
        l3 =    {'a': 1, 'b': 5, 'c': 9, 'd': 13, 'num': 1}
        l2 =    {'a': 2, 'b': 6, 'c': 10, 'd': 14, 'num': 2}
        front = {'a': 3, 'b': 7, 'c': 11, 'd': 15, 'num': 3}

        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['a'], temp[back['a']][back['num']][0], temp[back['a']][back['num']][1], temp[back['a']][back['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['b'], temp[back['b']][back['num']][0], temp[back['b']][back['num']][1], temp[back['b']][back['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['c'], temp[back['c']][back['num']][0], temp[back['c']][back['num']][1], temp[back['c']][back['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(back['d'], temp[back['d']][back['num']][0], temp[back['d']][back['num']][1], temp[back['d']][back['num']][2])
        print(line)
        
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['a'], temp[l2['a']][l2['num']][0], temp[l2['a']][l2['num']][1], temp[l2['a']][l2['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['b'], temp[l2['b']][l2['num']][0], temp[l2['b']][l2['num']][1], temp[l2['b']][l2['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['c'], temp[l2['c']][l2['num']][0], temp[l2['c']][l2['num']][1], temp[l2['c']][l2['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l2['d'], temp[l2['d']][l2['num']][0], temp[l2['d']][l2['num']][1], temp[l2['d']][l2['num']][2])
        print(line)

        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['a'], temp[l3['a']][l3['num']][0], temp[l3['a']][l3['num']][1], temp[l3['a']][l3['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['b'], temp[l3['b']][l3['num']][0], temp[l3['b']][l3['num']][1], temp[l3['b']][l3['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['c'], temp[l3['c']][l3['num']][0], temp[l3['c']][l3['num']][1], temp[l3['c']][l3['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(l3['d'], temp[l3['d']][l3['num']][0], temp[l3['d']][l3['num']][1], temp[l3['d']][l3['num']][2])
        print(line)

        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['a'], temp[front['a']][front['num']][0], temp[front['a']][front['num']][1], temp[front['a']][front['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['b'], temp[front['b']][front['num']][0], temp[front['b']][front['num']][1], temp[front['b']][front['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['c'], temp[front['c']][front['num']][0], temp[front['c']][front['num']][1], temp[front['c']][front['num']][2])
        print(line)
        line = 'strip.setPixelColor({}, {}, {}, {});'.format(front['d'], temp[front['d']][front['num']][0], temp[front['d']][front['num']][1], temp[front['d']][front['num']][2])
        print(line)

        print('strip.show();')
        print('delay(111);')
        #for f in temp:
        #    print(f)
        output(num, temp)
    # print(temp)

# print('before', chunk_list)
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