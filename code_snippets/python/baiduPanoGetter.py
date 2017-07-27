import urllib
import os
saveFolderPath = os.path.join(os.getcwd(),"image")

if os.path.exists(saveFolderPath):
    pass
else:
    os.mkdir(saveFolderPath)


def BuildAddress(sid,i,j):
    return "http://pcsv1.map.bdimg.com/?qt=pdata&sid=%s&pos=%d_%d&z=5&udt=20170627"%(sid,i,j)


for i in range(8):
    for j in range(16):
        img_url = BuildAddress("09000300011606211447521121A",i,j)

        filepath = os.path.join(saveFolderPath,"%d_%d.jpg"%(i,j))

        print(filepath)
        
        urllib.urlretrieve(img_url,filepath)
