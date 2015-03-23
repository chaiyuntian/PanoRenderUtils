# -*- coding:utf-8 -*-
import os
from PIL import Image

'''
images better be same height and same width(at least in one row)
'''

# The function to merge a list of image into a big image matrix of row*col .
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

# The key funtion to merge image into three resolution levels(1920,1024,512).
# @param image_folder: The parent folder to put all the six-face images in.
# @param images: the images of six faces.
#    Warning: Do not change the image list orders unless you know and can modify the UV coordinates of the cube.
# @param format1: the images' file format.

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

def merge_to_one(image_folder = 'Rendering'+os.sep+"cam",tgFilename="",tgFolder="Production",
                             images = [ 'up','front','down','back', 'right','left'],
                             format1 = '.png'):
    #image_folder = 'Rendering'+os.sep+"cam"
    #images = ['back', 'front', 'left', 'right', 'up', 'down']
    #format1 = '.png'
    image_files = [image_folder + os.sep + img + format1 for img in images]
    print(image_files)
    tg2 = tgFolder + os.sep + tgFilename +".jpg"
    from time import clock
    t1=clock()
    merge_faces(image_files, tg2, 1920)
    print "Processing Time:",clock()-t1


if __name__ == "__main__":

    '''
    merge_to_one("GAP\\no_ps\\off_Ambient_spot","P1_NG_N_AS")
    merge_to_one("GAP\\no_ps\\off_Focus_track","P1_NG_N_FT")

    merge_to_one("GAP\\no_ps\\on_Ambient_spot","P1_NG_D_AS")
    merge_to_one("GAP\\no_ps\\on_Focus_track","P1_NG_D_FT")

    merge_to_one("GAP\\ps\\off_Ambient_spot","P1_G_N_AS")
    merge_to_one("GAP\\ps\\off_Focus_track","P1_G_N_FT")

    merge_to_one("GAP\\ps\\on_Ambient_spot","P1_G_D_AS")
    merge_to_one("GAP\\ps\\on_Focus_track","P1_G_D_FT")
    
    merge_to_one("GAP\\P2_Window\\all_off_model","P2_all_off_model")
    merge_to_one("GAP\\P2_Window\\all_off_poster","P2_all_off_poster")
    merge_to_one("GAP\\P2_Window\\off_model","P2_off_model")
    merge_to_one("GAP\\P2_Window\\off_poster","P2_off_poster")
    merge_to_one("GAP\\P2_Window\\on_model","P2_on_model")
    '''
    merge_to_one("GAP\\P2_Window\\on_poster","P2_on_poster")
    
        
