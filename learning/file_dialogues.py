import sys, os
from pathlib import Path

def load_icons():
        icons_list = []
        for path, _, icons in os.walk('resources/icons'):
            for icon in icons:
                  icons_list.append(os.path.join(path, icon))
        return icons_list

print(load_icons())