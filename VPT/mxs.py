from utils import *
import re
switchfunc = '''fn Turn lt state = (if lt == undefined then(print "light type undefined")else(if classof lt == Free_Light then (lt.on = state)if classof lt == VRayIES then (lt.enabled = state)if classof lt == VRayLight then (lt.on = state)if classof lt == Free_Area then (lt.on = state)))
fn TurnGroup gp state = (if gp == undefined then(print "light group undefined")if classof gp == Dummy then(for l in gp.children do(Turn l state))else(print "input parameter is not group"))
if Turn == undefined or TurnGroup == undefined then(false)else(true)
'''
Exec(switchfunc)


fn_expression = re.compile(r'^fn\s(\S{1,})(\s(\S{1,})){1,}\s{0,}\=\s{0,}\({1})')

def parseFn(fnstr):
    re.match

class Fn(object):
    """dfndeftring for Fn"""
    def __init__(self, fndef):
        super(Fn, self).__init__()
        Exec(funcDef)
        self.fname = ""

    def call(self,*args):
        execStr = "% "
        Exec(self.f in xrange(1,10):
            pass)
        


def mxFunction(funcDef):
    Exec(funcDef)


if __name__ == '__main__':
    a = Fn()