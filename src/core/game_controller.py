"""
game_controller.py

The main "conductor" of the game.
Manages game state transitions and coordinates between the TUI
and the game logic modules.
"""

from core.game_state import GameState
# from game_logic import hero_manager, item_manager, battle_system, base_manager
from typing import Any # Using 'Any' for stubs

class GameController:
    """
    Manages the game's core state and logic flow.
    """
    def __init__(self):
        # The game_state will hold all persistent data (heroes, inventory, base)
        self.game_state: GameState = GameState()

        # The controller will also manage the current high-level game state
        # e.g., "MAIN_MENU", "BATTLE", "BASE_MANAGEMENT"
        self.current_screen: str = "MAIN_MENU"

        print("GameController initialized.")

    def new_game(self):
        """
        Initializes a new game state with starting values.
        (Called from MainMenuScreen)
        """
        print("Initializing new game state...")
        # 1. Create a fresh GameState object
        self.game_state = GameState()

        # 2. Add starting heroes (example structure)
        # In a real implementation, load archetypes from heroes.json
        self.game_state.heroes.append({
            "id": "hero_0",
            "name": "Warrior Hero",
            "class": "warrior",
            "level": 1,
            "current_xp": 0,
            "base_stats": {"hp": 120, "attack": 12, "defense": 8},
            "equipment": {}, # e.g., {"weapon": "sword_basic"}
            "is_active": True
        })
        self.game_state.heroes.append({
            "id": "hero_1",
            "name": "Mage Hero",
            "class": "mage",
            "level": 1,
            "current_xp": 0,
            "base_stats": {"hp": 80, "attack": 5, "defense": 3},
            "equipment": {},
            "is_active": True
        })
        # Add up to 5 heroes as needed

        # 3. Add starting items
        self.game_state.inventory["health_potion"] = 3
        self.game_state.inventory["sword_basic"] = 1 # Example starting item

        # 4. Set initial base status
        self.game_state.base_status["barracks"] = 0
        self.game_state.base_status["forge"] = 0

        print("New game state initialized with starting heroes, items, and base status.")


    def load_game(self):
        """
        Loads the game state from a file.
        (Responsibility is in game_state.py, but controller triggers it)
        """
        # Re-initialize GameState before loading to clear any old data
        self.game_state = GameState()
        self.game_state.load_state() # load_state handles FileNotFoundError etc.
        print("Controller triggered game load.")


    def save_game(self):
        """
        Saves the current game state to a file.
        (Responsibility is in game_state.py, but controller triggers it)
        """
        self.game_state.save_state()
        print("Controller triggered game save.")

    def switch_screen(self, new_screen: str):
        """
        Handles the logic for switching between major UI screens.
        (e.g., from 'BASE' to 'BATTLE')
        """
        # Future: Add logic here if needed before/after screen switch
        self.current_screen = new_screen
        print(f"Stub: Switching screen to {new_screen}")
        # Actual screen switching is handled by TUI app's push_screen/pop_screen

    def equip_item(self, hero_id: Any, item_id: Any):
        """
        Coordinates the logic for equipping an item to a hero.
        (Based on architecture.md data flow example)
        """
        print(f"Controller: Attempting to equip item {item_id} on hero {hero_id}...")
        # --- Future Logic ---
        # 1. Get game_state
        state = self.game_state
        # 2. Call logic module (Placeholder - item_manager not imported yet)
        # success = item_manager.apply_item(state, hero_id, item_id)
        success = True # Stub
        # 3. Handle result
        if success:
            print(f"Controller: Item {item_id} equipped on hero {hero_id}.")
        else:
            print(f"Controller: Failed to equip item {item_id} on hero {hero_id}.")
        # 4. (TUI will be notified via event or state watch - handled by Textual)
        pass

# This file defines the class. It won't be run directly.