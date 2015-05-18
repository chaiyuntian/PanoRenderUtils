import MaxPlus
import sys
import os
from merge import AutoExec
from xlsx import read_xls
from PySide import QtGui
import MaxPlus
from light import *


class _GCProtector(object):
    widgets = []

# QTGui Creation
app = QtGui.QApplication.instance()
if not app:
    app = QtGui.QApplication([])

def openDir(rootpath = 'F:\\imgs'):
    if(os.path.isdir(rootpath)):
        pass
    else:
        rootpath = ""
    
    dirname =  QtGui.QFileDialog.getExistingDirectory(dir=rootpath)
    print "Chosen Folder:" + dirname
    return dirname

def openFile(rootpath = 'F:\\imgs'):
    
    if(os.path.isdir(rootpath)):
        pass
    else:
        rootpath = ""

    filename = "nothing"
    try:
        filename,s = QtGui.QFileDialog.getOpenFileName(dir=rootpath, filter="Excel(*.xls *.xlsx)")
        print "Chosen File:" + filename
        return filename
    except:
        print "Error occurred"

def MergeImg():
    path = openDir()
    try:
        AutoExec(path)
    except:
        print "Error occurred during image merging."

def outputNode(n,indent = ''):
    print indent, n.Name
    for c in n.Children:
        outputNode(c, indent + '--')

def CheckScene():
    f = openFile()
    print f



    print "ok"

def createSphere():
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
    obj.ParameterBlock.Radius.Value = 5.0
    return MaxPlus.Factory.CreateNode(obj)

def createVPT(name):
    print "Checking has previously registered menus"
    if MaxPlus.MenuManager.MenuExists(name):
        MaxPlus.MenuManager.UnregisterMenu(name)
    else:
        pass
    action1 = MaxPlus.ActionFactory.Create('Check Scene','Check Scene2', CheckScene)
    action2 = MaxPlus.ActionFactory.Create('Merge Pictures','Merge', MergeImg)

    mb = MaxPlus.MenuBuilder(name)
    mb.AddItem(action1)
    mb.AddSeparator()
    mb.AddItem(action2)
    mb.AddSeparator()
    menu = mb.Create(MaxPlus.MenuManager.GetMainMenu())

    #menu = mb.Create(MaxPlus.MenuManager.GetMainMenu())

if __name__ == "__main__":
    createVPT("VPT")

    #outputNode(MaxPlus.Core.GetRootNode())