from asciimatics.effects import Print
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import FigletText
from asciimatics.screen import Screen
from asciimatics.scene import Scene 
from asciimatics.widgets import Frame, Layout, DropdownList, Background
import sys



def demo(screen, scene):
    scenes = [
       # add some scenes
       # Scene()
    ]
    screen.play(scenes, stop_on_resize=True, start_scene=scene)

if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)
        except ResizeScreenError as e:
            pass