
def warn(msg,code=1000,fpath = default_log_path):
    if type(msg)!=str:
        msg = str(msg)
    now = datetime.datetime.now()
    msg = ("[warning code:%d]:"%code)+now.strftime('@%Y-%m-%d %H:%M:%S')+']:'+msg
    print msg
    #print2file(msg,fpath)
        

def error(msg,code=1000,fpath = default_log_path):
    if type(msg)!=str:
        msg = str(msg)
    now = datetime.datetime.now()
    msg =  ("[error code:%d "%code)+now.strftime('@%Y-%m-%d %H:%M:%S')+']:'+msg
    print msg
    #print2file(msg,fpath)
        
def log(msg,fpath = default_log_path):
    if type(msg)!=str:
        msg = str(msg)
    now = datetime.datetime.now()
    data_str = "[log:"+now.strftime('@%Y-%m-%d %H:%M:%S')+']:'
    msg = data_str+msg
    print msg
    print2file(msg,fpath)
