import tkinter as tk
from random import randint, uniform, random
import math

banner = """    ________________  __  _______   _____ ______  _____  ____    ___  __________  ____ 
   / ____/ ____/ __ \/  |/  /  _/  / ___//  _/  |/  / / / / /   /   |/_  __/ __ \/ __ \\
  / /_  / __/ / /_/ / /|_/ // /    \__ \ / // /|_/ / / / / /   / /| | / / / / / / /_/ /
 / __/ / /___/ _, _/ /  / // /    ___/ // // /  / / /_/ / /___/ ___ |/ / / /_/ / _, _/ 
/_/   /_____/_/ |_/_/  /_/___/   /____/___/_/  /_/\____/_____/_/  |_/_/  \____/_/ |_|  """

print(banner)

#Set Scale ENTER 255 to see earths radio bubble
print("\nHelp: Enter 225 as the default for earths known radio bubble. \nOr if you prefer enter your own to get some fun results.")
SCALE = int(input("\nUniversal Scale in lightyears: "))
#Max number of advance civs
NUM_CIVS = int(input("How many civilizations in the universe: "))
#setup display canvas
root = tk.Tk()
root.title("Fermi Paradox Simulator")
c = tk.Canvas(root, width=1000, height=800, bg='black')
c.grid()
c.configure(scrollregion=(-500, -400, 500, 400))

#Actual Milky Way dimensions (light-years)
DISK_RADIUS = 50000
DISK_HEIGHT = 1000
DISK_VOL = math.pi * DISK_RADIUS**2 * DISK_HEIGHT

def scaleGalaxy():
    """Scale Galaxy dimension based on radio bubble size (scale)"""
    disk_radius_scaled = round(DISK_RADIUS / SCALE)
    bubble_vol = 4/3 * math.pi * (SCALE / 2)**3
    disk_vol_scaled = DISK_VOL/bubble_vol
    return disk_radius_scaled, disk_vol_scaled

def detectProb(disk_vol_scaled):
    """Calculate Probability ot galactic civs detecting each other."""
    ratio = NUM_CIVS / disk_vol_scaled #ratio of civs to scaled galaxy volume
    if ratio < 0.002:
        detection_prob = 0
    elif ratio >= 5:
        detection_prob = 1
    else:
        detection_prob = -0.004757 * ratio**4 + 0.06681 * ratio**3 - 0.3605 * \
                ratio**2 + 0.9215 * ratio + 0.00826
    return round(detection_prob, 3)

def randomPolarCoordinates(disk_radius_scaled):
    """Generate uniform random (x,y) point within a disk for 2d display"""
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * disk_radius_scaled)
    y = round(math.sqrt(r) * math.sin(theta) * disk_radius_scaled)
    return x, y

def spirals(b, r, rot_fac, fuz_fac, arm):
    """Build spiral arms for tkinter display ysing logorithmic spiral formula
    b = arbitrary constant logorithmic spiral equation
    r = scalled galactic disk radius
    rot_fac = rotation factor
    fuz_fac = random shift in star position in arm, applied to fuzz variable
    arm = spiral arm (0 = main arm, 1 = trailin stars)
    """

    spiral_stars = []
    fuzz = int(0.030 * abs(r)) #Randomly shift star locations
    theta_max_degrees = 520
    for i in range(theta_max_degrees):
        theta = math.radians(i)
        x = r * math.exp(b * theta) * math.cos(theta + math.pi * rot_fac)\
                + randint(-fuzz, fuzz) * fuz_fac
        y = r * math.exp(b * theta) * math.sin(theta + math.pi * rot_fac)\
                + randint(-fuzz, fuzz) * fuz_fac
        spiral_stars.append((x, y))

    for x, y in spiral_stars:
        if arm == 0 and int(x % 2) == 0:
            c.create_oval(x - 2, y - 2, x + 2, y + 2, fill = 'white', outline = '')
        elif arm == 0 and int(x % 2) == 0:
            c.create_oval(x - 1, y - 1, x + 1, y + 1, fill = 'white', outline = '')
        elif arm == 1:
            c.create_oval(x, y, x, y, fill = 'white', outline = '')

def star_haze(disk_radius_scaled, density):
    """Randomly distribute faint tkinter stars in galactic disk
    disk_radius_scaled = galactic disk radius scaled to radio bubble diameter
    density = multiplier to vary number of stars posted
    """
    for i in range(0, disk_radius_scaled * density):
        x, y = randomPolarCoordinates(disk_radius_scaled)
        c.create_text(x, y, fill = 'white', font = ('Helvetica', '7'), text='.')

def main():
    print("Generating output....")
    """Calculate detection probabiblity & Post galaxy display & statistics"""
    disk_radius_scaled, disk_vol_scaled = scaleGalaxy()
    detection_prob = detectProb(disk_vol_scaled)
    #build 4 main spiral arms & 4 trailing arms
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = 2, fuz_fac = 1.5, arm = 0)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = 1.91, fuz_fac = 1.5, arm = 1)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = 2, fuz_fac = 1.5, arm = 0)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = -2.09, fuz_fac = 1.5, arm = 1)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = 0.5, fuz_fac = 1.5, arm = 0)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = 0.4, fuz_fac = 1.5, arm = 1)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = -0.5, fuz_fac = 1.5, arm = 0)
    spirals(b = -0.3, r = disk_radius_scaled, rot_fac = -0.6, fuz_fac = 1.5, arm = 1)
    star_haze(disk_radius_scaled, density = 20)

    #display legend
    c.create_text(-455, -360, fill = 'white', anchor = 'w', text = 'One Pixel = {} LY'.format(SCALE))
    c.create_text(-455, -330, fill = 'white', anchor = 'w', text = 'Radio Bubble Diameter = {} LY'.format(SCALE))
    c.create_text(-455, -300, fill = 'white', anchor = 'w', text = 'Probablility of detection for {:,} civilizations = {}'.format(NUM_CIVS, detection_prob))

    #Post earths 225LY diameter bubble an annotate
    if SCALE == 225:
        c.create_rectangle(115, 75, 116, 76, fill = 'red', outline = '')
        c.create_text(118, 72, fill = 'red', anchor = 'w', text = "<---------- Earth's Radio Bubble")
    #Run Tkinter Loop
    root.mainloop()


if __name__ == '__main__':
    main()

