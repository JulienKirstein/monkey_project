from PIL import Image
import numpy as np
import time
import json
import os

before = time.time()
pathRight = "scanRight"
pathLeft = "scanLeft"
directoryRight = os.listdir(pathRight)
directoryLeft = os.listdir(pathLeft)

laser_y_tot = []
laser_z_tot = []
for i in range(0, len(directoryRight)):
    laser_x = []
    laser_y = []
    laser_z = []

    imRight = Image.open(pathRight + "\\" + directoryRight[i])
    imRight = np.array(imRight)

    imLeft = Image.open(pathLeft + "\\" + directoryLeft[i])
    imLeft = np.array(imLeft)

    right = np.sum(imRight, axis=2)

    red = np.where((255 + 80 <= right) & (right <= 255 + 300))

    for j in red[0]:
        if not i <= len(directoryRight) / 2 - 1:
            laser_y += [int(j)]

    for j in red[1]:
        if not i <= len(directoryRight) / 2 - 1:
            laser_z += [int(j)]

    left = np.sum(imLeft, axis=2)
    red = np.where((255 + 80 <= left) & (left <= 255 + 300))
    for j in red[0]:
        if i <= len(directoryRight) / 2 - 1:
            laser_y += [int(j)]
    for j in red[1]:
        if i <= len(directoryRight) / 2 - 1:
            laser_z += [1920 - int(j)]

    laser_y_tot += [laser_y]
    laser_z_tot += [laser_z]


lasers = {"laser_y_tot": laser_y_tot, "laser_z_tot": laser_z_tot}
open("lasers.txt", "w").write(json.dumps(lasers))
print(time.time()-before)
