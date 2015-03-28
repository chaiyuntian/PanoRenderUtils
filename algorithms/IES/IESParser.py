'''
# This is an IES parser module
# Author: Yuntina Chai
'''
import re

class IESParser(object):
    '''
    # members:
        vtx: The result of ies parsing to a in terpolated poinst in 3d space
        info: The basic information dictionary of an IES file
        format: The format type of current ies file.
    # methods:
        parseFile
        @param fn: input the filepath of the ies file.
    '''
    RE_IESNA = r'^IESNA:.'
    
    def init(self,**kwargs):
        super(IESParser,**kwargs).__init__(**kwargs)
        self._vtx = []
        self._info = {}
        self.iesna = ''
    
    def parseFile(self,fn):
        f = open(fn);
        flines = [];
        for line in open(fn):
            line = f.readline()  
            print line  
            flines.append(line)
        if not self.checkIESNA(flines[0]):
            print "Invalid IES file"
        else:
            
            self.iesna = self.iesna.replace(self.RE_IESNA,"")
        print self.iesna
        
        f.close()

    def checkIESNA(self,line):
        return re.match(self.RE_IESNA,line);
        
    
    
    def getVtx(self):
        return self._vtx

    def getInfo(self):
        return self.info
    


if __name__=="__main__":
    k = IESParser()
    k.parseFile("test.ies")
    print 
    
