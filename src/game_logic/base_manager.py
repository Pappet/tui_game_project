"""
base_manager.py

Contains the game logic for managing the base progression.
This module is stateless and operates on the game_state object
passed to it by the game_controller.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.game_state import GameState

# Define costs or rules for upgrades
UPGRADE_COSTS = {
    "barracks": {
        1: {"resource": "gold", "amount": 100},
        2: {"resource": "gold", "amount": 500},
    },
    "forge": {
        1: {"resource": "gold", "amount": 150},
    }
}

def can_upgrade_building(game_state: "GameState", building: str) -> bool:
    """
    Checks if a building can be upgraded (e.g., checks resources, prerequisites).
    """
    print(f"Stub: Checking if '{building}' can be upgraded...")
    # --- Future Logic ---
    # current_level = game_state.base_status.get(building, 0)
    # next_level = current_level + 1
    # 
    # if building not in UPGRADE_COSTS or next_level not in UPGRADE_COSTS[building]:
    #     print("Stub: Building is max level or does not exist.")
    #     return False
    #
    # cost = UPGRADE_COSTS[building][next_level]
    # # Check if player has resources in game_state.inventory
    # if game_state.inventory.get(cost["resource"], 0) >= cost["amount"]:
    #     return True
    #
    # print("Stub: Not enough resources.")
    return True # Stubbed to always allow

def apply_upgrade(game_state: "GameState", building: str) -> bool:
    """
    Applies the upgrade to the game_state if possible.
    Modifies game_state directly.
    """
    if not can_upgrade_building(game_state, building):
        print(f"Stub: Upgrade check failed for '{building}'.")
        return False
        
    print(f"Stub: Applying upgrade for '{building}'...")
    # --- Future Logic ---
    # 1. Deduct resources from game_state.inventory
    # 2. Increment level in game_state.base_status
    # 3. Apply effects (e.g., unlock items)
    
    # game_state.base_status[building] = game_state.base_status.get(building, 0) + 1
    
    return True

def get_base_effects(game_state: "GameState") -> dict:
    """
    Calculates the total effects provided by the base upgrades.
    (e.g., +5% hero HP, unlocks 'Steel Sword')
    """
    effects = {}
    # --- Future Logic ---
    # if game_state.base_status.get("forge", 0) >= 1:
    #     effects["unlocked_items"] = ["steel_sword"]
    
    print("Stub: Calculating base effects...")
    return effects