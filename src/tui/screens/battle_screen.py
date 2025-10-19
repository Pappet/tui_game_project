"""
battle_screen.py

Implements the Textual Screen for the combat view.
This UI displays the hero team, the enemies, and the actions
that can be taken during a battle.
"""

from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical, Horizontal
from textual.app import ComposeResult

# from core.game_controller import GameController

class BattleScreen(Screen):
    """
    The screen for handling combat.
    """
    
    def compose(self) -> ComposeResult:
        """
        Create the child widgets for the battle screen.
        """
        yield Header(name="Battle!")
        
        with Horizontal(id="battle_layout"):
            # Left side: Hero team
            with Vertical(id="hero_pane"):
                yield Static("Hero Team (Stub)")
                yield Static("Hero 1: 100/100 HP")
                yield Static("Hero 2: 100/100 HP")
                yield Static("Hero 3: 100/100 HP")
                yield Static("Hero 4: 100/100 HP")
                yield Static("Hero 5: 100/100 HP")

            # Right side: Enemy team
            with Vertical(id="enemy_pane"):
                yield Static("Enemies (Stub)")
                yield Static("Enemy 1: 50/50 HP")
                yield Static("Enemy 2: 50/50 HP")
        
        with Horizontal(id="action_bar"):
            yield Button("Attack", id="btn_attack")
            yield Button("Ability", id="btn_ability")
            yield Button("Item", id="btn_item")
            yield Button("Flee", id="btn_flee")
            
        yield Footer()

    def on_mount(self) -> None:
        """
        Called when the screen is mounted.
        """
        print("BattleScreen mounted (stub).")
        # Future: Load battle participants from controller/game_state
        # self.app.controller.start_battle()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """
        Handle button press events for battle actions.
        """
        if event.button.id == "btn_attack":
            print("Stub: 'Attack' button pressed.")
            # Future: Call controller
            # self.app.controller.execute_battle_turn("attack")
            
        elif event.button.id == "btn_flee":
            print("Stub: 'Flee' button pressed.")
            # Future: Call controller
            # self.app.controller.execute_battle_turn("flee")
            # self.app.pop_screen()
            pass