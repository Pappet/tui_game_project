"""
hero_screen.py

Implements the Textual Screen for the hero management view.
This UI displays the 5-hero team, allows viewing stats, 
and equipping items.
"""

from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical, Horizontal
from textual.app import ComposeResult

# from core.game_controller import GameController

class HeroScreen(Screen):
    """
    The screen for managing the player's 5-hero team.
    """
    
    def compose(self) -> ComposeResult:
        """
        Create the child widgets for the hero screen.
        """
        yield Header(name="Hero Management")
        
        with Horizontal(id="hero_team_layout"):
            # Stub for 5 hero portraits/summaries
            yield Static("Hero 1 [Selected]", id="hero_1")
            yield Static("Hero 2", id="hero_2")
            yield Static("Hero 3", id="hero_3")
            yield Static("Hero 4", id="hero_4")
            yield Static("Hero 5", id="hero_5")
            
        with Horizontal(id="hero_details_layout"):
            # Left: Selected hero stats
            with Vertical(id="hero_stats"):
                yield Static("Selected Hero Stats (Stub)")
                yield Static("Name: Hero 1")
                yield Static("HP: 100/100")
                yield Static("Attack: 10")
                yield Static("Defense: 5")
                yield Static("Weapon: [Empty]")
                yield Static("Armor: [Empty]")
            
            # Right: Inventory for equipping
            with Vertical(id="hero_inventory"):
                yield Static("Inventory (Stub)")
                yield Static("[Sword]")
                yield Static("[Leather Armor]")
                yield Button("Equip Selected Item", id="btn_equip")

        yield Button("Return to Main Menu", id="btn_main_menu")
        yield Footer()

    def on_mount(self) -> None:
        """
        Called when the screen is mounted.
        """
        print("HeroScreen mounted (stub).")
        # Future: Load hero data from controller/game_state
        # self.heroes = self.app.controller.game_state.heroes

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events.
        """
        if event.button.id == "btn_equip":
            print("Stub: 'Equip' button pressed.")
            # Future: Call controller (as per data flow example)
            # hero_id = ...
            # item_id = ...
            # self.app.controller.equip_item(hero_id, item_id)
            
        elif event.button.id == "btn_main_menu":
            print("Stub: 'Return to Main Menu' button pressed.")
            # self.app.pop_screen()
            pass