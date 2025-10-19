"""
base_screen.py

Implements the Textual Screen for the base management view.
This UI allows the player to see their base status and interact
with upgrades.
"""

from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import VerticalScroll

# from core.game_controller import GameController

class BaseScreen(Screen):
    """
    The screen for managing the player's base.
    """
    
    def compose(self) -> "ComposeResult":
        """
        Create the child widgets for the base screen.
        """
        yield Header(name="My Base")
        
        with VerticalScroll(id="base_layout"):
            yield Static("Base Management Screen (Stub)")
            yield Static("Current Upgrades:")
            # Future: Dynamically add widgets based on game_state.base_status
            yield Static("[Barracks - Lvl 1]", classes="upgrade_item")
            yield Static("[Forge - Lvl 0]", classes="upgrade_item")
            
            yield Button("Upgrade Barracks", id="btn_upgrade_barracks")
            yield Button("Return to Main Menu", id="btn_main_menu")
        
        yield Footer()

    def on_mount(self) -> None:
        """
        Called when the screen is mounted.
        """
        print("BaseScreen mounted (stub).")
        # Future: Load current base status from controller/game_state
        # self.app.controller.game_state.base_status

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.
        """
        if event.button.id == "btn_upgrade_barracks":
            print("Stub: 'Upgrade Barracks' button pressed.")
            # Future: Call controller to handle logic
            # self.app.controller.upgrade_building("barracks")
            
        elif event.button.id == "btn_main_menu":
            print("Stub: 'Return to Main Menu' button pressed.")
            # Future: Pop screen or switch via controller
            # self.app.pop_screen()
            pass