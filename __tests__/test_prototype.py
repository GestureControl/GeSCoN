import math
pointX1 = 10
pointX2 = 7
pointY1 = 16
pointY2 = 12
def get_dist(pointX1,pointX2,pointY1,pointY2):
    sign = -1
    if(pointY1<pointY2):
        sign = 1
    dist = (pointX1 - pointX2)**2 + (pointY1 - pointY2)**2
    dist = math.sqrt(dist)
    return dist*sign

distance = get_dist(pointX1,pointX2,pointY1,pointY2)
def test_get_dist():
    assert int(distance)==5
