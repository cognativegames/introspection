# ============================================================================
# NPC INITIALIZATION DATA
# Define starting states for all NPCs
# ============================================================================

# Example NPCs initialization
# Add your specific NPCs here with their starting beliefs and emotions

label initialize_npcs:
    # Initialize all NPCs with their starting states
    
    python:
        # Sarah - has trauma around being used
        initialize_npc(
            "sarah",
            "Sarah",
            starting_beliefs={
                "self.is-unworthy": BELIEF_INTENSITY_CORE,
                "others.use-me": BELIEF_INTENSITY_ACTIVE,
                "self.is-vulnerable": BELIEF_INTENSITY_ACTIVE
            },
            starting_emotions={
                "anxiety": 60,
                "trust": 30,
                "safety": 40,
                "isolation": 70
            }
        )
        
        # Mark - healthier boundaries, working on self-worth
        initialize_npc(
            "mark",
            "Mark",
            starting_beliefs={
                "self.deserves-respect": BELIEF_INTENSITY_ACTIVE,
                "self.is-capable": BELIEF_INTENSITY_ACTIVE,
                "others.are-complex": BELIEF_INTENSITY_SURFACE
            },
            starting_emotions={
                "clarity": 60,
                "trust": 50,
                "safety": 65
            }
        )
        
        # Add more NPCs as needed
    
    return
