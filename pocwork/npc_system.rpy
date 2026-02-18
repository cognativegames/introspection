# NPC SYSTEM - Mirror of Player System
# Each NPC has their own beliefs, emotions, and interpretation patterns

init 10 python:
    class NPCState:
        """
        Each NPC has the same internal system as the player
        They interpret events, hold beliefs, experience conflicts
        """
        
        def __init__(self, npc_id, name):
            self.npc_id = npc_id
            self.name = name
            
            # Same emotional system as player
            self.emotions = {
                "hope": 50,
                "anxiety": 30,
                "clarity": 50,
                "overwhelm": 20,
                "connection": 40,
                "isolation": 30,
                "trust": 50,  # NPC-specific: trust in general
                "safety": 50   # NPC-specific: feeling of safety
            }
            
            # Same belief system as player
            self.beliefs = {}  # belief_id -> intensity
            self.belief_history = []
            
            # Relationship tracking
            self.relationships = {}  # Other character_id -> relationship_data
            
            # Memory of encounters with player and others
            self.memories = []  # List of significant events
            
            # Trauma and healing tracking
            self.trauma_active = []  # Active trauma responses
            self.healing_progress = 0  # 0-100
            
            # NPC-specific: Therapy participation
            self.sessions_attended = 0
            self.breakthroughs = []
            self.ready_to_confront = []  # Topics they're ready to discuss
            
            # Current state
            self.introspection_depth = 0
            self.openness = 50  # How open they are to player (0-100)
        
        # Mirror player methods
        def activate_belief(self, belief_id, intensity):
            """Same as player"""
            current = self.beliefs.get(belief_id, BELIEF_INTENSITY_DORMANT)
            new_intensity = max(current, intensity)
            self.beliefs[belief_id] = new_intensity
            self.belief_history.append({
                "belief": belief_id,
                "intensity": new_intensity,
                "context": "interaction"
            })
        
        def detect_belief_conflicts(self):
            """Same conflict detection as player"""
            conflicts = []
            active_beliefs = [b_id for b_id, intensity in self.beliefs.items() 
                                if intensity >= BELIEF_INTENSITY_SURFACE]
            
            for belief_id in active_beliefs:
                if belief_id not in beliefs:
                    continue
                    
                belief = beliefs[belief_id]
                
                if "conflicts_with" in belief:
                    for conflicting_id in belief["conflicts_with"]:
                        if conflicting_id in active_beliefs:
                            intensity_1 = self.beliefs.get(belief_id, 0)
                            intensity_2 = self.beliefs.get(conflicting_id, 0)
                            severity = min(intensity_1, intensity_2)
                            
                            conflict_tuple = tuple(sorted([belief_id, conflicting_id]))
                            if (conflict_tuple, severity) not in [(tuple(sorted([c[0], c[1]])), c[2]) for c in conflicts]:
                                conflicts.append((belief_id, conflicting_id, severity))
            
            return conflicts
        
        def adjust_emotions(self, changes):
            """Same as player"""
            for emotion, change in changes.items():
                if emotion in self.emotions:
                    self.emotions[emotion] = max(0, min(100, self.emotions[emotion] + change))
        
        def get_relationship_with(self, character_id):
            """Get relationship data with specific character"""
            if character_id not in self.relationships:
                self.relationships[character_id] = {
                    "trust": 50,
                    "attraction": 0,
                    "resentment": 0,
                    "intimacy": 0,
                    "boundary_violations": 0,
                    "healing_moments": 0,
                    "last_interaction": None
                }
            return self.relationships[character_id]
        
        def remember_event(self, event_type, other_character_id, description, emotional_impact):
            """Store a significant event"""
            memory = {
                "type": event_type,  # "boundary_violation", "healing", "connection", "trauma_trigger"
                "with": other_character_id,
                "description": description,
                "emotional_impact": emotional_impact,
                "beliefs_activated": list(self.beliefs.keys())[-3:],  # Last 3 activated
                "timestamp": "scene_" + str(len(self.memories))
            }
            self.memories.append(memory)
            
            # Update relationship
            rel = self.get_relationship_with(other_character_id)
            rel["last_interaction"] = memory
        
        def interpret_player_action(self, action_type, action_context):
            """
            NPC interprets player's action through their own belief lens
            Returns their internal response
            """
            
            # Get NPC's active beliefs
            active_beliefs = [b_id for b_id, intensity in self.beliefs.items() 
                                if intensity >= BELIEF_INTENSITY_ACTIVE]
            
            # Different interpretations based on beliefs
            if action_type == "seduction" and action_context.get("vulnerable", False):
                
                # If NPC believes they're unworthy
                if "self.is-unworthy" in active_beliefs:
                    interpretation = {
                        "thought": "They want me? Maybe I'm not as worthless as I thought.",
                        "emotion_shift": {"hope": 15, "anxiety": -10},
                        "belief_impact": [("self.is-unworthy", -1)]  # Weakens slightly
                    }
                
                # If NPC believes others are predatory
                elif "others.are-threatening" in active_beliefs or "others.use-me" in active_beliefs:
                    interpretation = {
                        "thought": "Here we go again. They want to use me.",
                        "emotion_shift": {"anxiety": 20, "trust": -15, "safety": -20},
                        "belief_impact": [("others.use-me", 1)]  # Strengthens
                    }
                
                # If NPC has healthy boundaries
                elif "self.deserves-respect" in active_beliefs:
                    interpretation = {
                        "thought": "This feels wrong. They're taking advantage of my vulnerability.",
                        "emotion_shift": {"clarity": 10, "trust": -25},
                        "belief_impact": [("self.deserves-respect", 1)]  # Strengthens
                    }
                
                else:
                    # Neutral/confused
                    interpretation = {
                        "thought": "I don't know what to make of this.",
                        "emotion_shift": {"overwhelm": 10},
                        "belief_impact": []
                    }
                
                return interpretation
            
            # Add more action types as needed
            return None
        
        def will_bring_up_in_therapy(self, memory):
            """
            Decide if NPC will bring up this memory in group therapy
            Based on: healing progress, severity, time passed, safety level
            """
            
            if not memory:
                return False
            
            # High healing progress = more likely to share
            healing_factor = self.healing_progress / 100.0
            
            # High safety = more likely to share
            safety_factor = self.emotions.get("safety", 50) / 100.0
            
            # Severe events more likely to need processing
            severity = 0
            if memory["type"] == "boundary_violation":
                severity = 0.8
            elif memory["type"] == "trauma_trigger":
                severity = 0.9
            elif memory["type"] == "healing":
                severity = 0.3
            
            # Time passed (more recent = more urgent)
            recency = 1.0  # For now, assume recent
            
            # Calculate probability
            probability = (healing_factor * 0.3 + safety_factor * 0.3 + severity * 0.3 + recency * 0.1)
            
            import random
            return random.random() < probability
        
        def get_therapy_topic(self):
            """
            What will this NPC bring up in therapy?
            Returns a memory and their framing of it
            """
            
            # Check memories for unprocessed events
            unprocessed = [m for m in self.memories if m["type"] in ["boundary_violation", "trauma_trigger"]]
            
            if not unprocessed:
                return None
            
            # Pick most recent or most severe
            for memory in reversed(unprocessed):  # Most recent first
                if self.will_bring_up_in_therapy(memory):
                    
                    # Frame it based on their beliefs
                    if "self.is-unworthy" in self.beliefs and self.beliefs["self.is-unworthy"] >= BELIEF_INTENSITY_ACTIVE:
                        framing = "maybe_my_fault"
                    elif "others.are-threatening" in self.beliefs and self.beliefs["others.are-threatening"] >= BELIEF_INTENSITY_ACTIVE:
                        framing = "they_hurt_me"
                    else:
                        framing = "confused_processing"
                    
                    return {
                        "memory": memory,
                        "framing": framing,
                        "ready_to_share": self.emotions["safety"] >= 60
                    }
            
            return None


    npc_states = {}
    
    def get_npc(npc_id):
        """Get or create NPC state"""
        if npc_id not in npc_states:
            # Create default NPC
            npc_states[npc_id] = NPCState(npc_id, npc_id.title())
        return npc_states[npc_id]
    
    def initialize_npc(npc_id, name, starting_beliefs, starting_emotions=None):
        """Initialize an NPC with specific beliefs and emotions"""
        npc = NPCState(npc_id, name)
        
        # Set starting beliefs
        for belief_id, intensity in starting_beliefs.items():
            npc.activate_belief(belief_id, intensity)
        
        # Set starting emotions if provided
        if starting_emotions:
            for emotion, value in starting_emotions.items():
                npc.emotions[emotion] = value
        
        npc_states[npc_id] = npc
        return npc

# Example: Initialize a vulnerable NPC
init 20 python:
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
