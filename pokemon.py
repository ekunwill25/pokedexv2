"""
Exercise 3.2.v2: Simulate a Turn-Based Battle (Updated Stub)
"""

import requests

def calculate_stat(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's stat at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + 5)

def calculate_hp(base_stat, level=50, iv=15, ev=85):
    """Calculate Pokémon's HP at given level."""
    return int(((2 * base_stat + iv + (ev / 4)) * level / 100) + level + 10)

def calculate_damage(attacker_stats, defender_stats, level=50, base_power=60):
    """Calculate battle damage using standard formula."""
    return int((((2 * level * 0.4 + 2) * attacker_stats['attack'] * base_power) 
                / (defender_stats['defense'] * 50)) + 2)

def simulate_battle(pokemon1, pokemon2):
    """Simulate a battle between two Pokémon."""
    # TODO: Fetch Pokémon Data
    # - Create lowercase URLs for both Pokémon
    # - Make GET requests and check response codes
    # - Extract JSON data if successful

    # TODO: Calculate Initial Stats
    # - Use calculate_stat() for attack/defense/speed
    # - Use calculate_hp() for HP stats
    # - Store in dictionaries

    # TODO: Initialise Battle Display
    # - Show battle start message
    # - Display initial HP values

    # TODO: Determine First Attacker
    # - Compare speed stats
    # - Set up attacker/defender variables
    # - Store corresponding stats

    # TODO: Battle Loop
    # - Track round numbers
    # - While both have HP > 0:
    #   - Show current round
    #   - Calculate and deal damage
    #   - Check for fainting (==< 0)
    #   - Show remaining HP
    #   - Swap roles
    #   - Increment round

    # TODO: End Battle
    # - Show victory message
    # - Display winner

if __name__ == "__main__":
    simulate_battle("pikachu", "bulbasaur")

"""
Helper Info:
- Use calculate_damage() for proper battle mechanics
- Remember to handle API response errors
- Keep battle display clear and informative
"""