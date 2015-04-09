# -*- coding:utf-8 -*-
import os
from os.path import isdir
from PIL import Image
import re
import datetime
import shutil

fileformat = re.compile(r'c\d{1,}_LG\d{1,}_IES\d{1,}_[f,b,l,r,u,d].png$')
classify_folder = "classified"

# Message System
# warning, error and logs

def warn(msg,code=1000):
    if type(msg)==str:
        print ("[warning code:%d]:"%code)+msg

def error(msg,code=1000):
    if type(msg)==str:
        print ("[error code:%d]:"%code)+msg
        
def log(msg):
    now = datetime.datetime.now()
    data_str = "[log:"+now.strftime('@%Y-%m-%d %H:%M:%S')+']:'
    print data_str+msg

# usg regex to match filenames
# @param path - filepath root
def match_filename(path):
    lst = os.listdir(path)
    legal = []
    illegal = []
    for filename in lst:
        m = re.match(fileformat,filename)
        if m:
            legal.append(filename)
        else:
            illegal.append(filename)
    N = len(legal)
    M = len(illegal)
    log("legal filename count:%d, illegal filename count:%d"%(N,M))
    if N%6 != 0:
        warn("File missing prediction, some faces might be missing!")

    return legal


# Use the funciton under the condition:
# all the legal filenames are inputted in to the parameter
# put the files into different images according to their category
def file2Folder(rootpath,filename):
    lst = filename.split('_')
    targetfile = lst.pop()
    tgfolder = rootpath+os.sep+classify_folder
    for p in lst:
        tgfolder = os.path.join(tgfolder,p)
    
    if(isdir(tgfolder)):
        pass
    else:
        os.makedirs(tgfolder)
    source = os.path.join(rootpath,filename)
    target =  os.path.join(tgfolder,targetfile)
    shutil.copy(source, target)
    log("copied file from source:'%s' to target:'%s'" %(source,target))

# Classfy all the files into folders and report the illegal names.
def ToCategory(rootpath):
    lst = match_filename(rootpath)
    for f in lst:
        file2Folder(rootpath,f)



# images better be same height and same width(at least in one row)
# The function to merge a list of image into a big image matrix of row*col .
# @param image_files - files to merge
# @param tgfile - target filename
# @param tgwidth - taget image resolution
# @param row
# @param col
def merge_faces(image_files, tgfile, tgwidth=0, row=2, col=3):
    border_size = 0
    imgs = []
    num = len(image_files)
    width = 0
    height = 0

    if num != row * col:
        error('pattern is wrong, num != row * col')
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
    tg1 = image_folder + os.sep + "quality1_001.jpg"
    tg2 = image_folder + os.sep + "quality2_001.jpg"
    tg3 = image_folder + os.sep + "quality3_001.jpg"
    from time import clock
    t1=clock()
    merge_faces(image_files, tg1, 1920)
    merge_faces(image_files, tg2, 1024)
    merge_faces(image_files, tg3, 512)
    log("Processing Time:%f"%(clock()-t1))


# The key funtion to merge image into one resolution levels = 1920.
# @param image_folder: The parent folder to put all the six-face images in.
# @param images: the images of six faces.
#    Warning: Do not change the image list orders unless you know and can modify the UV coordinates of the cube.
# @param format1: the images' file format.
def merge_to_one(image_folder = 'Rendering'+os.sep+"cam",tgFilename="",tgFolder="Production",
                             images = [ 'u','f','d','b', 'r','l'],
                             format1 = '.png'):
    
    image_files = [image_folder + os.sep + img + format1 for img in images]
    if isdir(tgFolder):
        pass
    else:
        os.makedirs(tgFolder)
    
    tg2 = tgFolder + os.sep + tgFilename +".jpg"
    from time import clock
    t1=clock()
    merge_faces(image_files, tg2, 1920)
    log("finished:%s, processing Time:%f"%(tg2,clock()-t1))


# check if the input filenames match all the items in the face list
# @param filenames - input filename list
# @param facelist - six faces names
# @param format - image format
def matchFileList(filenames,facelist = [ 'u','f','d','b', 'r','l'],format = '.png'):
    flist = [face+ format for face in facelist]
    for f in filenames:
        try:
            flist.remove(f);
        except:
            pass
    return flist
        
# Merge the files under the folder. Using os.walk to go through all the folders and check if  [ 'u','f','d','b', 'r','l'] is all present.
# if yes then merge them all, name the target image with the hierach of the folder.
# @param rootFolder - which folder to work with.
def AutoMerge(rootFolder = os.getcwd()):
    finished = []
    unfinished = []
    for dirpath, dirnames, filenames in os.walk(rootFolder):
        lst = matchFileList(filenames)
        if len(lst)>=6:
            pass
        elif len(lst)==0:
            pathtemp = dirpath
            pathtemp = pathtemp.replace(rootFolder+os.sep,'');
            pathtemp = pathtemp.replace('\\','_')
            tgFilename = pathtemp
            merge_to_one(dirpath,tgFilename,rootFolder+os.sep+"Production")
            finished.append(tgFilename)
        else:
            unfinished.append((dirpath,lst))
            
    log("finished file list:")
    print finished
    log("unfinished file list:")
    print unfinished

# Category the files and Merge the images.
def AutoExec(rootpath):
    ToCategory(rootpath)
    AutoMerge(rootpath+os.sep+classify_folder)
    
if __name__ == "__main__":
    AutoExec(os.getcwd())


