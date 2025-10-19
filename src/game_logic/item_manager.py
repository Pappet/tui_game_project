"""
item_manager.py

Contains the game logic for managing items, inventory, and equipment effects.
This module is stateless and operates on the game_state object.
"""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from core.game_state import GameState

# This data would eventually be loaded from data/items.json
ITEM_DEFINITIONS = {
    "sword": {"name": "Sword", "slot": "weapon", "stats": {"attack": 5}},
    "leather_armor": {"name": "Leather Armor", "slot": "armor", "stats": {"defense": 3}},
}

def get_item_stats(item_id: str) -> Dict[str, Any]:
    """
    Retrieves the stat bonuses for a given item_id.
    """
    item = ITEM_DEFINITIONS.get(item_id)
    if item:
        return item.get("stats", {})
    return {}

def can_equip_item(game_state: "GameState", hero: Dict[str, Any], item_id: str) -> bool:
    """
    Checks if a hero can equip a specific item.
    (e.g., checks class requirements, level requirements)
    """
    print(f"Stub: Checking if hero can equip {item_id}...")
    
    if item_id not in ITEM_DEFINITIONS:
        print(f"Stub: Item {item_id} does not exist.")
        return False
        
    # Stub: For now, all heroes can equip all items
    return True

def apply_item(game_state: "GameState", hero_id: Any, item_id: Any) -> bool:
    """
    Equips an item onto a hero, updating the game_state.
    This function implements the logic described in the
    architecture's "Data Flow Example".
    
    Modifies game_state directly.
    """
    print(f"Stub: 'apply_item' called for Hero {hero_id} and Item {item_id}.")
    
    # --- Future Logic ---
    # 1. Find the hero in game_state.heroes
    # hero = next((h for h in game_state.heroes if h["id"] == hero_id), None)
    # if not hero:
    #     print(f"Stub: Hero {hero_id} not found.")
    #     return False
    #
    # 2. Check if item is in game_state.inventory
    # if game_state.inventory.get(item_id, 0) <= 0:
    #     print(f"Stub: Item {item_id} not in inventory.")
    #     return False
    #
    # 3. Check if hero can equip it
    # if not can_equip_item(game_state, hero, item_id):
    #     print(f"Stub: Hero {hero_id} cannot equip {item_id}.")
    #     return False
    #
    # 4. Perform the swap
    # item_def = ITEM_DEFINITIONS[item_id]
    # slot = item_def["slot"]
    #
    # # Unequip old item (if any)
    # old_item_id = hero.get("equipment", {}).get(slot)
    # if old_item_id:
    #     game_state.inventory[old_item_id] = game_state.inventory.get(old_item_id, 0) + 1
    #
    # # Equip new item
    # hero.get("equipment", {})[slot] = item_id
    # game_state.inventory[item_id] -= 1
    #
    # print(f"Stub: Hero {hero_id} equipped {item_id}.")
    return True