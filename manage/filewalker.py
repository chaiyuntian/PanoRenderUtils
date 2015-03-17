# -*- coding: utf-8 -*-
import os
from os.path import basename, isdir
from os import listdir
 
def traverse(path, f,depth=0):
    print>>f,depth* '| ' + '|_', basename(path)
    if(isdir(path)):
        for item in listdir(path):
            traverse(path+'/'+item, f, depth+1)
 
if __name__ == '__main__':
    f = open('DIRECTORY.txt', 'w')
    traverse(os.getcwd(),f)
    f.close()
