# ============================================================================
# THERAPY ENCOUNTERS
# Dr. Chen offers encounters - player cannot access directly
# ============================================================================

# Dr. Chen character definition
define dr_chen = Character("Dr. Chen", color="#8B4513", who_alt="Dr. Chen")

# ============================================================================
# VISUAL ADAPTATION
# ============================================================================

init python:
    # Visual states for encounters based on active beliefs
    ENCOUNTER_VISUAL_STATES = {
        "default": "imagination_neutral",
        "self.is-unworthy": "imagination_dimmed",
        "self.is-fundamentally-flawed": "imagination_dimmed",
        "abandonment.is-inevitable": "imagination_empty",
        "others.are-threatening": "imagination_empty",
        "self.is-failure": "imagination_foggy",
        "others.are-better": "imagination_foggy",
        "self.is-worthy": "imagination_bright",
        "others.are-friendly": "imagination_warm",
        "self.is-capable": "imagination_bright"
    }
    
    def get_encounter_visual(beliefs):
        """
        Determine visual state based on active beliefs.
        
        Returns the appropriate background/visual for encounter scenes
        based on the player's strongest active belief.
        
        Args:
            beliefs: dict of belief_id -> intensity
            
        Returns:
            String identifier for the visual state
        """
        # Check for strongest negative belief
        strongest_negative = None
        max_intensity = 0
        
        for belief_id, intensity in beliefs.items():
            if intensity > max_intensity:
                max_intensity = intensity
                strongest_negative = belief_id
        
        if strongest_negative and strongest_negative in ENCOUNTER_VISUAL_STATES:
            return ENCOUNTER_VISUAL_STATES[strongest_negative]
        
        # Check for positive beliefs
        positive_beliefs = ["self.is-worthy", "self.is-capable", "others.are-friendly"]
        for belief_id in positive_beliefs:
            if beliefs.get(belief_id, 0) > 2:
                return ENCOUNTER_VISUAL_STATES[belief_id]
        
        return ENCOUNTER_VISUAL_STATES["default"]

# ============================================================================
# ENCOUNTER OFFER FLOW
# ============================================================================

label offer_encounter(game_state):
    """
    Dr. Chen offers an encounter to the player.
    Player cannot access encounters directly - must be offered.
    """
    $ router = EncounterRouter()
    $ encounter = router.select_encounter(game_state)
    
    if encounter is None:
        dr_chen "I don't have anything specific to work on today. Let's just talk."
        return
    
    # Show therapist offer
    dr_chen "I'd like to try something with you today."
    
    # Show encounter preview (could be implemented with a screen)
    "[encounter['title']]"
    "[encounter['description']]"
    
    menu:
        "Accept the encounter":
            jump run_encounter
        
        "I'm not ready for this":
            # Living in denial - enhanced negative emotions
            $ game_state.adjust_emotions({
                "loneliness": 2,
                "emptiness": 1,
                "detachment": 1
            })
            dr_chen "That's okay. Take your time. But avoiding these feelings doesn't make them go away."
            return

label run_encounter(encounter):
    """
    Run an encounter with interpretation choices.
    """
    # Determine visual based on beliefs
    $ visual_state = get_encounter_visual(game_state.beliefs)
    
    # Present the encounter scenario with interpretations
    scene expression visual_state
    
    "[encounter['description']]"
    
    dr_chen "How do you interpret this?"
    
    menu:
        "What do you see here?"
        
        # Generate menu items from interpretations
        "Focus on the negative aspect":
            $ _result = execute_interpretation(game_state, encounter, "negative")
            jump encounter_after_interpretation
            
        "Look at this neutrally":
            $ _result = execute_interpretation(game_state, encounter, "neutral")
            jump encounter_after_interpretation
        
        "Find something positive":
            $ _result = execute_interpretation(game_state, encounter, "positive")
            jump encounter_after_interpretation

label encounter_after_interpretation:
    # Check if introspection should trigger
    if game_state.should_trigger_introspection():
        jump offer_deep_introspection
    
    dr_chen "Let's continue processing this."
    return

label execute_interpretation(game_state, encounter, interpretation_type):
    """
    Execute an interpretation choice and apply its effects.
    
    Returns:
        The interpretation that was applied
    """
    # Find the interpretation
    python:
        interpretation = None
        for interp in encounter["interpretations"]:
            if interp["type"] == interpretation_type:
                interpretation = interp
                break
    
    if interpretation is None:
        return None
    
    # Record the interpretation
    $ game_state.record_interpretation(interpretation_type)
    
    # Apply belief change if applicable
    if interpretation.get("belief"):
        $ game_state.activate_belief(interpretation["belief"], BELIEF_INTENSITY_ACTIVE)
    
    # Apply emotion deltas
    if interpretation.get("delta"):
        $ game_state.adjust_emotions(interpretation["delta"])
    
    return interpretation

# ============================================================================
# DEEP INTROSPECTION OFFER
# Alternative introspection path (not the main one)
# ============================================================================

label offer_deep_introspection:
    """
    Offer deep introspection after multiple negative interpretations.
    """
    dr_chen "I notice you've been having a difficult time lately."
    dr_chen "Would you like to explore what's happening beneath the surface?"
    
    menu:
        "Yes, I want to understand":
            jump begin_introspection
        
        "Not right now":
            dr_chen "That's okay. We can try another time."
            return

label begin_introspection:
    """
    Begin the deep introspection process.
    """
    # This would link to existing introspection system
    dr_chen "Let's look at what beliefs might be driving these feelings..."
    # Placeholder for introspection system integration
    return
