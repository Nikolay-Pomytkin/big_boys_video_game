"""
This is the file containing all constants used in the video game
Ex. Window width, window height, background color, etc.
"""

# Import arcade library
import arcade

# Main Menu Requirements
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.WHITE
MAIN_MENU_TITLE = "Big Boys Video Game: Main Menu"

# Texture imports
def main_menu_backround():
	arcade.load_texture("images/main_menu.png", 0, 0, 600, 800, 1)