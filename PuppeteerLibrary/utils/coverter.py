def str2bool(v):
    if v == True:
        return True
    return v.lower() in ("yes", "true", "1")
