init 10 python:
    class GameState:
        def __init__(self):
            # Core state
            self.phase = GAME_PHASE_STORY
            self.chapter = 1
            self.scene_count = 0
            
            # Emotional state (0-100)
            self.emotions = {
                "hope": 50,
                "anxiety": 30,
                "clarity": 50,
                "overwhelm": 20,
                "connection": 40,
                "isolation": 30
            }

            self.relationships = {
                "alex": {"trust": 50, "romance": 0, "shared_secrets": 0},
                "jordan": {"trust": 60, "romance": 0, "shared_secrets": 0}
            }

            # Belief tracking with intensity (using integers)
            self.beliefs = {}  # belief_id -> intensity (int)
            self.belief_history = []  # Track transformation journey
            
            # Encounter management
            self.current_encounter = None
            self.encounter_queue = []
            self.completed_encounters = []
            self.interpretation_streak = {"positive": 0, "negative": 0}
            
            # Game goals
            self.achievements = set()
            self.rewards_unlocked = []

            # Narrative state
            self.relationships = {}  # character_id -> trust_level
            self.story_flags = set()  # Unlocked story elements
            self.introspection_depth = 0  # How deep player has gone
            
            # Meta
            self.use_ai = False
            self.playtime_minutes = 0