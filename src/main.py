# Import arcade library
import arcade
# Import module with constants
from constants import *

# Set game attributes
arcade.open_window(MAIN_MENU_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.set_background_color(BACKGROUND_COLOR)

# Start rendering
arcade.start_render()

main_menu_background()

# Finish rendering
arcade.finish_render()
# Keep the window up until someone closes it.
arcade.run()