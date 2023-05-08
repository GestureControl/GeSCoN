import math
def distance1(duration):
    r = 3.4 * duration / 2
    dist1 = r / 100.00
    return dist1

def distance2(duration):
    r = 3.4 * duration / 2
    dist2 = r / 100.00
    return dist2

duration = 1000.0

Distance_1 = distance1(duration)
def test_distance1():
    assert int(Distance_1)==17    

Distance_2 = distance2(duration)
def test_distance2():
    assert int(Distance_2)==17

assert int(Distance_1) == int(Distance_2)
