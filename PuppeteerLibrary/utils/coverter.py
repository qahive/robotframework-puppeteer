def str2bool(v):
    if v == True:
        return True
    elif v == False:
        return False
    return v.lower() in ("yes", "true", "1")
