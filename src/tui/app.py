"""
app.py

The main Textual App class for the TUI game.
This class is the entry point for the Textual framework and manages
the different screens.
"""

from textual.app import App, ComposeResult

# Import screens
from tui.screens.main_menu import MainMenuScreen
# from tui.screens.hero_screen import HeroScreen
# from tui.screens.base_screen import BaseScreen
# from tui.screens.battle_screen import BattleScreen

# Import the core logic
from core.game_controller import GameController

class GameApp(App):
    """
    The main TUI application class.
    """

    # CSS_PATH = "main.tcss" # Future styling

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = GameController() # Initialize the game controller
        # print("GameApp initialized (stub).")

    def compose(self) -> ComposeResult:
        """
        Called by Textual to create the initial widget tree.
        Initially, it might be empty as we push screens dynamically.
        """
        # We could yield global Header/Footer here
        # print("GameApp compose() called (stub).")
        yield from [] # Yield nothing for now

    def on_mount(self) -> None:
        """
        Called by Textual when the app is first mounted.
        This is the correct place to push the initial screen.
        """
        self.push_screen(MainMenuScreen())
        # print("Stub: App mounted. Pushing initial screen (e.g., MainMenuScreen).")

# This file is not run directly.
# It is imported by main.py which then calls .run()