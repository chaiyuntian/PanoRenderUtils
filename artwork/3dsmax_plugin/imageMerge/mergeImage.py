# -*- coding:utf-8 -*-
import os
import sys
from PIL import Image
import time
class MergeImg:

    def __init__(self, imageFiles, mode='h'):
        self.border_size = 0
        self.images = []
        self.num = len(imageFiles)
        self.width = 0
        self.height = 0
        self.mode = mode
        if self.mode == 'v':
            for image in imageFiles:
                im = Image.open(image)
                if im.size[0] >= self.width:
                    self.width = im.size[0]
                    self.height = self.height + im.size[1]
                    self.images.append(im)
                    self.width += 2 * self.border_size
                    self.height += (self.num + 1) * self.border_size
                    print self.width, self.height

        if self.mode == 'h':
            for image in imageFiles:
                im = Image.open(image)
                if im.size[1] >= self.height:
                    self.height = im.size[0]
                    self.width = self.width + im.size[0]
                    self.images.append(im)
                    self.height += 2 * self.border_size
                    self.width += (self.num + 1) * self.border_size
                    print self.width, self.height


    def save(self, fileName):
        out_img = Image.new('RGBA', (self.width, self.height))
        out_img.paste(0xFFFFFF, (0, 0, self.width, self.height))

        offset = 0

        if self.mode == 'v':
            cur_height = self.border_size
            for image in self.images:
                tmp = image.copy()
                offset = (self.width - 2 * self.border_size - image.size[0]) / 2
                out_img.paste(tmp, (self.border_size + offset, cur_height))
                cur_height = cur_height + tmp.size[1] + self.border_size

        if self.mode == 'h':
            cur_width = self.border_size
            for image in self.images:
                tmp = image.copy()
                offset = (self.height - 2 * self.border_size - image.size[1]) / 2
                out_img.paste(tmp, (cur_width, self.border_size + offset))
                cur_width = cur_width + tmp.size[0] + self.border_size

        out_img.save(fileName)

if __name__ == "__main__":
    image_folder ='testImages'
    images = ['back', 'front', 'left', 'right', 'up', 'down']
    format1 = '.png'
    imageFiles = [image_folder + os.sep + img + format1 for img in images]
    print(imageFiles)
    m = MergeImg(imageFiles,'v')
    m.save(image_folder+os.sep+"merged_v.png")

    m = MergeImg(imageFiles,'h')
    m.save(image_folder+os.sep+"merged_h.png")
