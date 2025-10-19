"""
battle_system.py

Contains the game logic for handling combat mechanics.
This module is stateless and calculates the outcome of battle
actions based on the current game_state.
"""

from typing import TYPE_CHECKING, Dict, Any

if TYPE_CHECKING:
    from core.game_state import GameState

def start_battle(game_state: "GameState", enemy_encounter_id: str) -> Dict[str, Any]:
    """
    Initializes a battle state (but doesn't store it here).
    Returns the initial state of the battle participants.
    """
    print(f"Stub: Initializing battle with encounter '{enemy_encounter_id}'.")
    
    # --- Future Logic ---
    # 1. Load enemy data from data/enemies.json
    # 2. Get hero data from game_state.heroes
    # 3. Create a temporary 'battle_state' dictionary
    
    battle_state = {
        "heroes": [h for h in game_state.heroes if h.get("is_active", True)],
        "enemies": [{"id": "enemy_1", "hp": 50}, {"id": "enemy_2", "hp": 50}],
        "turn": 0
    }
    return battle_state

def calculate_attack_outcome(attacker: Dict[str, Any], defender: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculates the result of one entity attacking another.
    """
    print(f"Stub: Calculating attack: {attacker.get('id')} vs {defender.get('id')}")
    
    # --- Future Logic ---
    # damage = attacker.get("attack", 5) - defender.get("defense", 1)
    # if damage < 0:
    #     damage = 0
    # defender_hp = defender.get("hp", 100) - damage
    
    result = {
        "attacker_id": attacker.get("id"),
        "defender_id": defender.get("id"),
        "damage_dealt": 5, # Stub
        "defender_hp_remaining": defender.get("hp", 50) - 5
    }
    return result

def process_battle_turn(game_state: "GameState", battle_state: Dict[str, Any], player_action: Dict[str, Any]) -> Dict[str, Any]:
    """
    Processes one full turn of battle (player action + enemy actions)
    and modifies the battle_state.
    
    Note: This modifies the passed 'battle_state' dictionary, not the
    persistent 'game_state' (until the battle is over).
    """
    print(f"Stub: Processing turn {battle_state.get('turn')}.")
    
    # 1. Process Player Action
    if player_action.get("type") == "attack":
        # player_hero = battle_state["heroes"][player_action.get("actor_index", 0)]
        # target_enemy = battle_state["enemies"][player_action.get("target_index", 0)]
        # attack_result = calculate_attack_outcome(player_hero, target_enemy)
        # target_enemy["hp"] = attack_result["defender_hp_remaining"]
        print("Stub: Player attacks.")

    # 2. Process Enemy Actions
    # for enemy in battle_state["enemies"]:
    #     if enemy["hp"] > 0:
    #         # target_hero = ... (e.g., random hero)
    #         # enemy_attack_result = calculate_attack_outcome(enemy, target_hero)
    #         # target_hero["hp"] = enemy_attack_result["defender_hp_remaining"]
    #         print(f"Stub: {enemy['id']} attacks.")

    # 3. Check for battle end
    # ...
    
    battle_state["turn"] += 1
    return battle_state