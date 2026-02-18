# ============================================================================
# CHARACTER DEFINITIONS
# All character objects and NPC initialization
# ============================================================================

# ============================================================================
# CHARACTER OBJECTS
# ============================================================================

define mc = Character("[player_name]", color="#ffffff")
define jill = Character("Jill", color="#cc28cc")
define dr_chen = Character("Dr. Chen", color="#4a90e2")
define therapist = dr_chen # alias
define nurse_reyes = Character("Nurse Reyes", color="#50c878")
define nurse = nurse_reyes #alias
define becky = Character("Becky", color="#ff6b9d")

# ============================================================================
# NPC INITIALIZATION
# Call this to set up all NPCs with their belief systems
# ============================================================================

init python:
    def initialize_all_npcs():
        """Initialize all NPCs with their starting states"""
        
        # Initialize each NPC
        # (NPC initialization code would go here once the NPC system is fully implemented)
        initialize_npc_therapist();
        initialize_npc_becky();
        initialize_npc_jill();
        pass
