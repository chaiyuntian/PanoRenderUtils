# -*- coding:utf-8 -*-
import os
from PIL import Image

'''
images better be same height and same width(at least in on row)
'''


def merge_faces(image_files, tgfile, tgwidth=0, row=2, col=3):
    border_size = 0
    imgs = []
    num = len(image_files)
    width = 0
    height = 0

    if num != row * col:
        print 'pattern error'
        return
    index = 0

    for r in range(row):
        row_width = 0
        cell_height = 0
        for c in range(col):
            im = Image.open(image_files[index])
            if tgwidth > 0:
                ratio = 1.0 * im.size[1] / im.size[0]
                new_height = int(tgwidth * ratio)
                new_size = (tgwidth, new_height)
                im = im.resize(new_size, Image.ANTIALIAS)
            imgs.append(im)
            row_width += im.size[0] + 2 * border_size
            if im.size[1] >= cell_height:
                cell_height = im.size[1]
            index += 1
        if row_width >= width:
            width = row_width
        height += cell_height + 2 * border_size

    out_img = Image.new('RGB', (width, height))
    out_img.paste(0xFFFFFF, (0, 0, width, height))

    index = 0

    for r in range(row):
        for c in range(col):
            tmp = imgs[index]
            offset_x = (width / col - 2 * border_size - tmp.size[0]) / 2
            offset_y = (height / row - 2 * border_size - tmp.size[1]) / 2
            cur_x = int(c * width / col)
            cur_y = int(r * height / row)
            out_img.paste(tmp, (cur_x + offset_x, cur_y + offset_y))
            index += 1
            out_img.save(tgfile)


def merge_to_three_qualities(image_folder = 'Rendering'+os.sep+"cam",
                             images = [ 'up','front','down','back', 'right','left'],
                             format1 = '.png'):

    #image_folder = 'Rendering'+os.sep+"cam"
    #images = ['back', 'front', 'left', 'right', 'up', 'down']
    #format1 = '.png'
    image_files = [image_folder + os.sep + img + format1 for img in images]
    print(image_files)
    tg1 = image_folder + os.sep + "quality1_001.jpg"
    tg2 = image_folder + os.sep + "quality2_001.jpg"
    tg3 = image_folder + os.sep + "quality3_001.jpg"
    from time import clock
    t1=clock()
    merge_faces(image_files, tg1, 1920)
    merge_faces(image_files, tg2, 1024)
    merge_faces(image_files, tg3, 512)
    print "Processing Time:",clock()-t1

if __name__ == "__main__":

    merge_to_three_qualities("GAP\\day\\Ambient_Spot")
    merge_to_three_qualities("GAP\\day\\Focus_Track")
