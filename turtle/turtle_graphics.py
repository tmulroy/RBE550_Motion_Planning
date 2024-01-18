from turtle import *


# Diameter
# arc length
# turn angle
# Forward 1/2 diameter
# Turn Right by 120 degrees
# Forward second leg ( determine by arc length)
# Turn right by 120 degrees
# Forward by diameter
# Turn right by 120 degrees

color('black', 'white')
begin_fill()
while True:
    forward(200)
    right(120)
    forward(150)
    right(120)
    forward(100)
    # if abs(pos()) < 1:
    #     break
# end_fill()
# done()
# print('done')