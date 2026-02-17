# ============================================================================
# GAME STATE CLASS
# Central state management for the game
# All methods defined inline - no monkey-patching
# ============================================================================

init python:
    class GameState:
        """
        Manages all game state including emotions, beliefs, relationships,
        and progression. This is the single source of truth for the player's
        journey through the game.
        """
        
        def __init__(self):
            # Core state
            self.phase = GAME_PHASE_STORY
            self.chapter = 1
            self.scene_count = 0
            
#            Emotional state (0-100) - Brené Brown's Atlas of the Heart
            self.emotions = self.initialize_emotions_brene()
            
            # Relationships
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
            self.story_flags = set()  # Unlocked story elements
            self.introspection_depth = 0  # How deep player has gone
            
            # Meta
            self.use_ai = False
            self.playtime_minutes = 0
        
        # ====================================================================
        # BELIEF METHODS
        # ====================================================================
        
        def activate_belief(self, belief_id, intensity=BELIEF_INTENSITY_SURFACE):
            """Activate or intensify a belief"""
            current = self.beliefs.get(belief_id, BELIEF_INTENSITY_DORMANT)
            new_intensity = max(current, intensity)
            self.beliefs[belief_id] = new_intensity
            self.belief_history.append({
                "belief": belief_id,
                "intensity": new_intensity,
                "scene": self.scene_count
            })
        
        def resolve_belief(self, negative_id, positive_id):
            """Transform negative belief into positive"""
            self.beliefs[negative_id] = BELIEF_INTENSITY_RESOLVED
            self.beliefs[positive_id] = BELIEF_INTENSITY_CORE
            self.introspection_depth += 1
        
        def get_active_negative_beliefs(self):
            """Get all active negative beliefs"""
            result = []
            for bid, intensity in self.beliefs.items():
                if intensity in [BELIEF_INTENSITY_ACTIVE, BELIEF_INTENSITY_CORE]:
                    if bid in beliefs:
                        if beliefs[bid]['type'] == 'negative':
                            result.append(bid)
            return result
        
        def detect_belief_conflicts(self):
            """
            Detect active beliefs that contradict each other
            Returns list of conflict tuples: (belief_id_1, belief_id_2, severity)
            """
            conflicts = []
            active_beliefs = [b_id for b_id, intensity in self.beliefs.items() 
                                if intensity >= BELIEF_INTENSITY_SURFACE]
            
            for belief_id in active_beliefs:
                if belief_id not in beliefs:
                    continue
                    
                belief = beliefs[belief_id]
                
                # Check if this belief has defined conflicts
                if "conflicts_with" in belief:
                    for conflicting_id in belief["conflicts_with"]:
                        if conflicting_id in active_beliefs:
                            # Calculate severity based on intensity difference
                            intensity_1 = self.beliefs.get(belief_id, 0)
                            intensity_2 = self.beliefs.get(conflicting_id, 0)
                            
                            # Higher intensity beliefs create more severe conflicts
                            severity = min(intensity_1, intensity_2)
                            
                            # Don't duplicate (A conflicts B is same as B conflicts A)
                            conflict_tuple = tuple(sorted([belief_id, conflicting_id]))
                            if (conflict_tuple, severity) not in [(tuple(sorted([c[0], c[1]])), c[2]) for c in conflicts]:
                                conflicts.append((belief_id, conflicting_id, severity))
            
            return conflicts
        
        def apply_conflict_consequences(self):
            """
            Apply emotional distress based on active belief conflicts
            Called after beliefs are activated
            """
            conflicts = self.detect_belief_conflicts()
            
            if not conflicts:
                return None
            
            # Calculate total emotional distress
            distress_amount = 0
            for _, _, severity in conflicts:
                if severity >= BELIEF_INTENSITY_CORE:
                    distress_amount += 20
                elif severity >= BELIEF_INTENSITY_ACTIVE:
                    distress_amount += 10
                else:
                    distress_amount += 5
            
            # Apply to emotions
            self.adjust_emotions(
                anxiety=distress_amount,
                overwhelm=distress_amount // 2,
                clarity=-distress_amount // 2
            )
            
            return conflicts
        
        # ====================================================================
        # EMOTION METHODS
        # ====================================================================
        
        def adjust_emotions(self, changes):
            """Adjust emotional state with bounds (0-10 scale)"""
            for emotion, delta in changes.items():
                if emotion in self.emotions:
                    self.emotions[emotion] = max(0, min(10, 
                        self.emotions[emotion] + delta))
        
        def get_dominant_emotion(self):
            """Return the strongest current emotion"""
            return max(self.emotions.items(), key=lambda x: x[1])[0]
        
        def initialize_emotions_brene(self):
            """
            Initialize emotions based on Brené Brown's taxonomy
            Returns dict with all emotions at baseline
            """
            emotions = {}
            for emotion_name, data in EMOTION_TAXONOMY.items():
                emotions[emotion_name] = data["baseline"]
            return emotions
        
        def get_emotion_group(self, emotion_name):
            """Get the group/family an emotion belongs to"""
            if emotion_name in EMOTION_TAXONOMY:
                return EMOTION_TAXONOMY[emotion_name].get("group")
            return None
        
        def get_related_beliefs(self, emotion_name):
            """Get beliefs commonly associated with this emotion"""
            if emotion_name in EMOTION_TAXONOMY:
                return EMOTION_TAXONOMY[emotion_name].get("related_beliefs", [])
            return []
        
        def get_emotion_definition(self, emotion_name):
            """Get Brené Brown's definition of this emotion"""
            if emotion_name in EMOTION_TAXONOMY:
                return EMOTION_TAXONOMY[emotion_name].get("definition", "")
            return ""

        def get_emotion_belief_feedback(self):
            """
            Analyze emotions and suggest which beliefs might be active
            This is for player awareness/introspection
            """
            feedback = []
            
            # High shame + belief checking
            if self.emotions.get("shame", 0) >= 6:
                if "self.is-fundamentally-flawed" in self.beliefs:
                    feedback.append("Your shame suggests you believe you're fundamentally flawed")
            
            # High loneliness + belief checking
            if self.emotions.get("loneliness", 0) >= 6:
                if "self.is-unworthy" in self.beliefs:
                    feedback.append("Your loneliness connects to believing you're unworthy of connection")
            
            # High anxiety + belief checking  
            if self.emotions.get("anxiety", 0) >= 6:
                if "world.is-dangerous" in self.beliefs:
                    feedback.append("Your anxiety stems from seeing the world as dangerous")
            
            # High clarity + hope = integration
            if self.emotions.get("clarity", 0) >= 6 and self.emotions.get("hope", 0) >= 6:
                feedback.append("Your clarity and hope show you're integrating new meanings")
            
            return feedback

        # ====================================================================
        # RELATIONSHIP METHODS
        # ====================================================================
        
        def adjust_relationship(self, character, **changes):
            """Change relationship values"""
            if character not in self.relationships:
                self.relationships[character] = {"trust": 50, "romance": 0}
            
            for stat, delta in changes.items():
                current = self.relationships[character].get(stat, 0)
                self.relationships[character][stat] = max(0, min(100, current + delta))
        
        def get_relationship_level(self, character, stat="trust"):
            """Get relationship tier: stranger, friend, close, intimate"""
            value = self.relationships.get(character, {}).get(stat, 0)
            if value < 25: return "stranger"
            elif value < 50: return "acquaintance"
            elif value < 75: return "friend"
            else: return "close"
        
        # ====================================================================
        # PROGRESSION METHODS
        # ====================================================================
        
        def check_achievements(self):
            """Check for unlockable achievements"""
            # First breakthrough
            if (self.introspection_depth == 1 and 
                "first_breakthrough" not in self.achievements):
                self.achievements.add("first_breakthrough")
                self.rewards_unlocked.append({
                    "type": "achievement",
                    "name": "The First Crack",
                    "description": "You saw through a limiting belief"
                })
            
            # Resolved 5 beliefs
            resolved = len([b for b, i in self.beliefs.items() 
                        if i == BELIEF_INTENSITY_RESOLVED])

            if resolved >= 5 and "five_beliefs" not in self.achievements:
                self.achievements.add("five_beliefs")
                self.rewards_unlocked.append({
                    "type": "achievement",
                    "name": "Metamorphosis",
                    "description": "Transformed 5 limiting beliefs"
                })
                # Unlock special encounter
                self.story_flags.add("metamorphosis_unlocked")
        
            # Perfect positive streak
            if (self.interpretation_streak['positive'] >= 5 and
                "clarity_streak" not in self.achievements):
                self.achievements.add("clarity_streak")
                # Unlock bonus content
                self.story_flags.add("clarity_master")
        
        def is_ready_for_introspection(self):
            """Check if player should be offered introspection"""
            # Offer after 2+ negative interpretations
            if self.interpretation_streak['negative'] >= 2:
                return True
            # Or if emotional distress is high
            if self.emotions['anxiety'] > 7 or self.emotions['overwhelm'] > 7:
                return True
            return False

init 1 python:
    game_state = GameState()