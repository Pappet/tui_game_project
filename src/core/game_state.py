"""
game_state.py

Holds all persistent data for the game.
This includes hero rosters, inventory, and base progression.
Also responsible for loading and saving the game state.
"""

import json
from typing import List, Dict, Any

class GameState:
    """
    Represents the complete persistent state of the game.
    """
    def __init__(self):
        # Placeholder for the 5-hero team
        self.heroes: List[Dict[str, Any]] = []

        # Placeholder for player's inventory
        self.inventory: Dict[str, int] = {} # e.g., {"health_potion": 5}

        # Placeholder for base progression
        self.base_status: Dict[str, int] = {} # e.g., {"barracks_level": 1}

        print("GameState initialized.") # Removed (stub)

    def load_state(self, filepath: str = "savegame.json"):
        """
        Loads the game state from a file (e.g., JSON).
        """
        # --- Future Logic ---
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                # Basic validation: Check if keys exist before assigning
                self.heroes = data.get("heroes", [])
                self.inventory = data.get("inventory", {})
                self.base_status = data.get("base_status", {})
            print(f"Game state loaded from {filepath}")
        except FileNotFoundError:
            print(f"No save file found at {filepath}. Starting new game (state remains default).")
            # Keep default empty state if file not found
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filepath}. Starting new game (state remains default).")
            # Handle corrupted save file
            self.heroes = []
            self.inventory = {}
            self.base_status = {}
        except Exception as e:
            # Catch other potential errors (permissions, etc.)
            print(f"An unexpected error occurred loading game state: {e}. Starting new game (state remains default).")
            self.heroes = []
            self.inventory = {}
            self.base_status = {}
        # print(f"Stub: Attempting to load state from {filepath}...")

    def save_state(self, filepath: str = "savegame.json"):
        """
        Saves the current game state to a file (e.g., JSON).
        """
        # --- Future Logic ---
        data = {
            "heroes": self.heroes,
            "inventory": self.inventory,
            "base_status": self.base_status
        }
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Game state saved to {filepath}")
        except Exception as e:
            # Catch potential errors like permission issues
            print(f"Error saving game state to {filepath}: {e}")
        # print(f"Stub: Attempting to save state to {filepath}...")

# This file defines the class. It won't be run directly.