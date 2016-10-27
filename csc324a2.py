

def PE(x, z):
    return ((x+z)/20) + 55

def TE(y, z):
    return ((y+z)/20) + 65

def PT(x, y, z, t):
    return ((x+z)/20) + ((y+z)/20) + t

if __name__ == '__main__':

    #print(PT(0, 0, 1000, 0))
    t = 120
    x = 0
    y = 0
    z = 1000
    for i in range(t):
        print("PE: {}, TE: {}, PT: {}, t: {}".format(PE(x, z), TE(y, z), PT(x, y, z, i), i))