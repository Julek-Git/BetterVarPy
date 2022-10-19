def string(x):
    return str(x)
def intnum(x):
    try:
        return int(x)
    except:
        return "  Give me a integer  "
def floatnum(x):
    try:
        return float(x)
    except:
        return "  Give me a float number  "
def boolean(x):
    if x == 1 or x == 0 or x == True or x == False:
        return bool(x)
    else:
        return "  Give me a boolean variable  "
def table(lenght, *args):
    if lenght == len(args):
        x = [args]
        return x
    else:
        return("  Give me a true lenght of the table  ")