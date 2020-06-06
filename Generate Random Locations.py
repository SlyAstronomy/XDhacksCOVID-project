import random

startinglat = 49.185996
startinglng = -122.846

rangex = 0.00001
rangey = 0.00001
entries = 92
x = 1

while x<entries:
    variation = random.choice([-1,1])*rangex*random.random()
    newlat = startinglat+variation
    variation = random.choice([-1, 1]) * rangey * random.random()
    newlng = startinglng+variation
    print(newlat, newlng)
    #print("new google.maps.LatLng("+str(newlat)+","+" "+str(newlng)+"),")
    x+=1

