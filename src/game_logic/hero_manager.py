"""
hero_manager.py

Contains the game logic for managing heroes, including stats,
leveling, and status effects.
This module is stateless and operates on the game_state object.
"""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from core.game_state import GameState

# Experience points required for next level (example)
XP_PER_LEVEL = {
    1: 100,
    2: 300,
    3: 700,
}

def calculate_hero_stats(hero: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculates the final derived stats of a hero based on
    base stats, level, and equipped items.
    
    This function *returns* the calculated stats, it does not
    modify the hero directly unless intended.
    """
    print(f"Stub: Calculating stats for {hero.get('name', 'Unknown Hero')}")
    
    # --- Future Logic ---
    # 1. Start with base stats
    # final_stats = hero.get("base_stats", {}).copy()
    #
    # 2. Add stats from level
    # level = hero.get("level", 1)
    # final_stats["hp"] += level * 10
    #
    # 3. Add stats from equipment
    # (This logic might be in item_manager.py, or looped here)
    # for item_id in hero.get("equipment", {}).values():
    #     item_stats = item_manager.get_item_stats(item_id)
    #     for stat, value in item_stats.items():
    #         final_stats[stat] = final_stats.get(stat, 0) + value
            
    # For now, just return a stub
    final_stats = {
        "hp": 100,
        "attack": 10,
        "defense": 5
    }
    
    return final_stats


def add_experience(hero: Dict[str, Any], xp_amount: int) -> bool:
    """
    Adds experience to a hero and checks for level-up.
    Modifies the hero dictionary directly.
    Returns True if the hero leveled up, False otherwise.
    """
    print(f"Stub: Adding {xp_amount} XP to {hero.get('name')}")
    
    # --- Future Logic ---
    # hero["current_xp"] = hero.get("current_xp", 0) + xp_amount
    # current_level = hero.get("level", 1)
    # 
    # required_xp = XP_PER_LEVEL.get(current_level)
    # 
    # if required_xp and hero["current_xp"] >= required_xp:
    #     # Level up!
    #     hero["level"] += 1
    #     hero["current_xp"] -= required_xp
    #     apply_level_up_stats(hero)
    #     print(f"Stub: {hero.get('name')} leveled up to {hero['level']}!")
    #     return True
        
    return False

def apply_level_up_stats(hero: Dict[str, Any]):
    """
    Applies the base stat increases for a hero leveling up.
    Modifies the hero dictionary directly.
    """
    print(f"Stub: Applying level-up stats to {hero.get('name')}")
    # --- Future Logic ---
    # hero["base_stats"]["hp"] += 10
    # hero["base_stats"]["attack"] += 2
    # hero["base_stats"]["defense"] += 1
    pass