# libraries needed
from datetime import date, datetime
from PIL import Image

# function definitions
def getDate():
    # getting today's date
    today   = date.today()

    # extracting day/month/weekday
    d = int(today.strftime("%d"))
    m = int(today.strftime("%m"))

    return [d, m]

def create_points():
    # giving the coordinates X for the cross position
    start   = 5
    spacing = 7
    stop    = 1031
    coordinatesX_cross = [int ( start + x/(spacing-1)*(stop-start) ) for x in range(spacing)]

    # giving the coordinates y for the cross position
    start   = 820
    spacing = 6
    stop    = 1631
    coordinatesY_cross = [int ( start + x/(spacing-1)*(stop-start) ) for x in range(spacing)]

    # creating tuple-meshgrid coordinates
    meshgrid = [tuple((x,y)) for y in coordinatesY_cross for x in coordinatesX_cross]

    return meshgrid

def newWeekday(weekday):
    weekdays = [1 , 2, 3, 4, 5, 6, 0]
    return weekdays[weekday]

# extension of the imgs
ext     = ".png"

# extracting day/month/weekday
day, month = getDate()

# points to place the cross
points = create_points()

# opening cross image
cross   = Image.open("calendar/cross"+ext)

# resizing cross to the size of date day box
cross   = cross.resize((162, 162))

# opening calendar month
c_month = Image.open("calendar/"+str(month)+ext)

# get the first weekday of the month
first   = newWeekday(datetime(2022,month,1).weekday())

# overlay crosses in coordinate positions
for i in range(day-1):
    c_month.paste(cross, points[i+first], cross)

# resizing for README.md adjust
w, h = c_month.width, c_month.height
c_month = c_month.resize((w//5,h//5))

# saving to print
c_month.save("this_month.png")