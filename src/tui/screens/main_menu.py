"""
main_menu.py

Implements the Textual Screen for the main menu.
This is the initial screen the player sees, providing options
to start, load, or quit the game.
"""

from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical
from textual.app import ComposeResult

# Import other screens to switch to
from tui.screens.hero_screen import HeroScreen
from tui.screens.base_screen import BaseScreen
from tui.screens.battle_screen import BattleScreen

class MainMenuScreen(Screen):
    """
    The main menu and starting screen for the game.
    """

    def compose(self) -> ComposeResult:
        """
         Create the child widgets for the main menu.
        """
        yield Header(name="Main Menu")

        with Vertical(id="menu_options"):
            yield Static("TUI RPG GAME (Title Stub)", id="title")
            yield Button("Start New Game", id="btn_new_game")
            yield Button("Load Game", id="btn_load_game")

            # --- Quick navigation buttons for development ---
            yield Button("Go to Base (Dev)", id="btn_goto_base")
            yield Button("Go to Heroes (Dev)", id="btn_goto_heroes")
            yield Button("Go to Battle (Dev)", id="btn_goto_battle")
            # --- End Dev Buttons ---

            yield Button("Quit", id="btn_quit")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events on the main menu.
        """
        if event.button.id == "btn_new_game":
            # print("Stub: 'New Game' pressed.")
            # Future: Call controller to initialize a new game state
            self.app.controller.new_game() # Call controller
            self.app.push_screen(BaseScreen()) # e.g., go to base

        elif event.button.id == "btn_load_game":
            # print("Stub: 'Load Game' pressed.")
            # Future: Call controller to load game state
            self.app.controller.load_game() # Call controller
            self.app.push_screen(BaseScreen()) # e.g., go to base

        elif event.button.id == "btn_goto_base":
            # print("Stub: 'Go to Base' pressed.")
            self.app.push_screen(BaseScreen())

        elif event.button.id == "btn_goto_heroes":
            # print("Stub: 'Go to Heroes' pressed.")
            self.app.push_screen(HeroScreen())

        elif event.button.id == "btn_goto_battle":
             # print("Stub: 'Go to Battle' pressed.")
             self.app.push_screen(BattleScreen())

        elif event.button.id == "btn_quit":
            # print("Stub: 'Quit' pressed.")
            self.app.exit()