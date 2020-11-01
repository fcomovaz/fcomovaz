# Credits
"""
moonphase.py - Calculate Lunar Phase
Author: Sean B. Palmer, inamidst.com
Cf. http://en.wikipedia.org/wiki/Lunar_phase#Lunar_phase_calculation
"""

# libraries requiered
import math, decimal, datetime

dec = decimal.Decimal

#   getting the lunar position
def lunarPosition(now=None): 
    if  now is None: 
        now = datetime.datetime.now()

    diff = now - datetime.datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))

    return lunations % dec(1)

# setting the lunar phase
def phase(pos): 
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return {
        0: "New Moon :new_moon:", 
        1: "Waxing Crescent :waxing_crescent_moon:", 
        2: "First Quarter :first_quarter_moon:", 
        3: "Waxing Gibbous :waxing_gibbous_moon:", 
        4: "Full Moon :full_moon:", 
        5: "Waning Gibbous :waning_gibbous_moon:", 
        6: "Last Quarter :last_quarter_moon:", 
        7: "Waning Crescent :waning_crescent_moon:"
    }[int(index) & 7]

#   calculating the lunar phase and position
pos = lunarPosition()
phasename = phase(pos)

# file to be rewriten
moon_file = open("temp_moonphase.md","w+")

# join temperature info
moon_file.write("\n<details><summary>Moon Phase :full_moon_with_face::new_moon_with_face:</summary><br/>\n")

# set lunar phase
moon_file.write(f"Today it's {phasename}")

# close the details tag
moon_file.write("\n</details>\n\n")

# close file
moon_file.close()