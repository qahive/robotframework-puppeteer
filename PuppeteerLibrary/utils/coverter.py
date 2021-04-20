def str2bool(v):
    if v == True:
        return True
    elif v == False:
        return False
    return v.lower() in ("yes", "true", "1")

def str2str(s):
    if s is None:
        return None
    return str(s)

def str2int(s):
    if s is None:
        return 0
    return int(s)
