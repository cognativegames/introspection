# ENCOUNTER SYSTEM UI AND HELPERS

# Custom screen for choosing interpretations
screen interpretation_choice_screen(choices):
    """
    Display interpretation choices with emotion/belief indicators
    """
    
    style_prefix "interpretation"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        
        vbox:
            spacing 20
            xfill True
            
            text "How do you interpret this?" style "interpretation_title"
            
            null height 20
            
            # Show each interpretation as a button
            for choice in choices:
                button:
                    xfill True
                    ysize 120
                    action Return(choice)  # Return the FULL choice dict, not just a string
                    
                    vbox:
                        spacing 5
                        xfill True
                        
                        # Main interpretation text
                        text choice["display"] style "interpretation_text"
                        
                        # Show which beliefs this activates (if player has awareness)
                        if game_state.introspection_depth >= 2:
                            hbox:
                                spacing 10
                                
                                for belief_id in choice.get("activates", []):
                                    if belief_id in beliefs:
                                        $ belief_type = beliefs[belief_id].get("type", "neutral")
                                        
                                        if belief_type == "positive":
                                            text "✓" color "#88ff88" size 20
                                        elif belief_type == "negative":
                                            text "✗" color "#ff8888" size 20
                        
                        # Show alignment indicator if deep enough
                        if game_state.introspection_depth >= 4:
                            if choice.get("aligns"):
                                text "{i}(Aligned with reality){/i}" style "interpretation_hint" color "#88ff88"
                            else:
                                text "{i}(Distortion){/i}" style "interpretation_hint" color "#ff8888"

style interpretation_frame:
    background Solid("#1a1a1a")
    padding (40, 40)

style interpretation_title:
    size 32
    color "#ffffff"
    xalign 0.5

style interpretation_text:
    size 24
    color "#dddddd"

style interpretation_hint:
    size 18
    color "#888888"

# Enhanced EncounterRouter selection logic
init 20 python:
    def enhanced_select_encounter(self, state):
        """
        Enhanced encounter selection based on emotions and belief patterns
        """
        
        candidates = []
        dominant_emotion = state.get_dominant_emotion()
        active_negatives = state.get_active_negative_beliefs()
        
        # PRIORITY 1: Address overwhelming emotions
        if state.emotions.get("anxiety", 0) >= 70:
            # High anxiety - offer calming encounters
            candidates = [e for e in self.encounter_vault.values() 
                            if "calming" in e.get("tags", [])]
            
        elif state.emotions.get("overwhelm", 0) >= 70:
            # Too overwhelmed - simple, grounding encounters
            candidates = [e for e in self.encounter_vault.values() 
                            if "grounding" in e.get("tags", [])]
            
        elif state.emotions.get("isolation", 0) >= 70:
            # High isolation - connection-focused encounters
            candidates = [e for e in self.encounter_vault.values() 
                            if "connection" in e.get("tags", [])]
        
        # PRIORITY 2: Address specific negative beliefs
        elif active_negatives:
            # Pick the most intense negative belief
            belief_intensities = [(b, state.beliefs.get(b, 0)) 
                                    for b in active_negatives]
            belief_intensities.sort(key=lambda x: x[1], reverse=True)
            
            if belief_intensities:
                target_belief = belief_intensities[0][0]
                
                # Find encounters that address this belief
                candidates = [e for e in self.encounter_vault.values()
                                if target_belief in e.get("addresses_beliefs", [])]
        
        # PRIORITY 3: Build on positive momentum
        elif state.interpretation_streak.get("positive", 0) >= 3:
            # They're on a roll - offer deeper encounters
            candidates = [e for e in self.encounter_vault.values()
                            if e.get("requires_depth", 0) <= state.introspection_depth
                            and "deepening" in e.get("tags", [])]
        
        # PRIORITY 4: Mix things up if stuck in negative pattern
        elif state.interpretation_streak.get("negative", 0) >= 3:
            # Stuck in distortion - offer very clear, unambiguous encounters
            candidates = [e for e in self.encounter_vault.values()
                            if e.get("type") == "clear"
                            and "grounding" in e.get("tags", [])]
        
        # PRIORITY 5: Default selection
        else:
            candidates = [e for e in self.encounter_vault.values()
                            if e.get("is_default")]
        
        # Filter out recently used
        candidates = [e for e in candidates 
                        if e['id'] not in self.used_encounters]
        
        # If no candidates, reset and pick from defaults
        if not candidates:
            self.used_encounters = set()
            candidates = [e for e in self.encounter_vault.values()
                            if e.get("is_default")]
        
        if candidates:
            return random.choice(candidates)
        else:
            # Absolute fallback
            return random.choice(list(self.encounter_vault.values()))
    
    EncounterRouter.select_encounter = enhanced_select_encounter

# Helper: Determine if introspection should be offered
init 20 python:
    def is_ready_for_introspection(self):
        """
        Determine if player should be offered introspection
        """
        
        # Always offer after resolving beliefs
        if any(intensity == BELIEF_INTENSITY_EXAMINED 
            for intensity in self.beliefs.values()):
                return True
        
        # Offer if stuck in negative pattern
        if self.interpretation_streak.get("negative", 0) >= 2:
            return True
        
        # Offer if high negative emotions
        if (self.emotions.get("anxiety", 0) >= 60 or 
            self.emotions.get("overwhelm", 0) >= 60):
            return True
        
        # Offer if they've activated multiple negative beliefs
        negative_count = len(self.get_active_negative_beliefs())
        if negative_count >= 2:
            return True
        
        # Don't offer too frequently if they're doing well
        return False
    
    GameState.is_ready_for_introspection = is_ready_for_introspection

# Helper: Get dominant emotion
init 20 python:
    def get_dominant_emotion(self):
        """
        Return the currently dominant emotion
        """
        if not self.emotions:
            return None
        
        dominant = max(self.emotions.items(), key=lambda x: x[1])
        
        # Only return if significantly high
        if dominant[1] >= 40:
            return dominant[0]
        
        return None
    
    GameState.get_dominant_emotion = get_dominant_emotion

# Emotion-specific dialogue modifiers
# These can be used in encounters to change dialogue based on emotions

init python:
    def get_emotion_modifier(emotion_name, intensity):
        """
        Get dialogue modifier text based on emotion and intensity
        """
        
        modifiers = {
            "anxiety": {
                "low": "",
                "medium": "Your hands tremble slightly. ",
                "high": "Your heart pounds. Everything feels unstable. "
            },
            "hope": {
                "low": "",
                "medium": "A small spark of possibility. ",
                "high": "You feel something shift. A lightness. "
            },
            "clarity": {
                "low": "Everything is foggy, uncertain. ",
                "medium": "",
                "high": "The world feels crisp, clear, real. "
            },
            "overwhelm": {
                "low": "",
                "medium": "It's a lot to process. ",
                "high": "Too much. Everything is too much. "
            },
            "connection": {
                "low": "Distant. Separated by glass. ",
                "medium": "",
                "high": "You feel seen. Present. Connected. "
            },
            "isolation": {
                "low": "",
                "medium": "Alone, even in company. ",
                "high": "Utterly alone. No one can reach you. "
            }
        }
        
        if emotion_name not in modifiers:
            return ""
        
        if intensity < 40:
            level = "low"
        elif intensity < 70:
            level = "medium"
        else:
            level = "high"
        
        return modifiers[emotion_name][level]

# Use in encounters like this:
# $ anxiety_text = get_emotion_modifier("anxiety", game_state.emotions["anxiety"])
# "[anxiety_text]You approach the stranger."
