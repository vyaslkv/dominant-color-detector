from colorthief import ColorThief
import webcolors

color_thief = ColorThief('cropped_image/15_2.jpg')
# get the dominant color
dominant_color = color_thief.get_color(quality=1)
# build a color palette
palette = color_thief.get_palette(color_count=6)
print(dominant_color)
print(palette)
colors = {'red': (255,0,0),
          'green': (0,255,0),
          'blue': (0,0,255),
          'beige': (245,245,220),
          'peach': (255,229,180),
          'yellow': (255,255,0),
          'orange': (255,127,0),
          'buff': (240,220,130),
          'white': (255,255,255),
          'lavender': (230,230,250),
          'brown': (150,75,0),
          'ivory': (255,255,240),
          'gray':  (171, 161, 161),
          'black': (0,0,0),
          'maroon': (128,0,0),
          'pink': (255,127,127),
          'purple': (127,0,255),
          'skyblue': (0,255,255),
          }
def distance(left, right):
    print(left,right)
    return sum((l-r)**2 for l, r in zip(left, right))**0.5

class NearestColorKey(object):
    def __init__(self, goal):
        self.goal = goal
    def __call__(self, item):
        return distance(self.goal, item[1])
print(min(colors.items(), key=NearestColorKey(palette[0])))
