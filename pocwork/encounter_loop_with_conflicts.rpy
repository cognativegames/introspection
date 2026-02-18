# UPDATED ENCOUNTER LOOP WITH CONFLICT DETECTION
# Replace the show_interpretation_consequence label with this version

label show_interpretation_consequence:
    """
    Show the player what their interpretation does
    NOW WITH CONFLICT DETECTION
    """
    
    $ game_state.phase = GAME_PHASE_CONSEQUENCE
    
    scene introspection_space with dissolve
    
    # Show internal thought
    if "internal_thought" in last_interpretation:
        "Your thought: {i}[last_interpretation['internal_thought']]{/i}"
    
    # CHECK FOR CONFLICTS FIRST
    python:
        conflict_data = game_state.apply_conflict_consequences()
        has_conflict = conflict_data and conflict_data["total_distress"] > 10
    
    # If there's a conflict, show it BEFORE the alignment feedback
    if has_conflict:
        play sound "dissonance.mp3"
        
        python:
            severe_conflict = game_state.get_most_severe_conflict()
        
        if severe_conflict:
            # Show the conflict
            "Wait. Something feels wrong."
            
            "Part of you just thought: '{i}[severe_conflict['belief_1']['statement']]{/i}'"
            
            "But you also believe: '{i}[severe_conflict['belief_2']['statement']]{/i}'"
            
            "They can't both be true. The contradiction... it hurts."
            
            show conflict_overlay with dissolve
            
            python:
                severity = severe_conflict["severity"]
                
                if severity == BELIEF_INTENSITY_CORE:
                    pain_description = "Your head pounds. This conflict is tearing you apart."
                elif severity == BELIEF_INTENSITY_ACTIVE:
                    pain_description = "A sharp tension. These beliefs are fighting inside you."
                else:
                    pain_description = "A subtle dissonance. Something doesn't quite fit."
            
            "[pain_description]"
            
            hide conflict_overlay with dissolve
            
            # Offer immediate introspection
            menu:
                "This conflict needs attention."
                
                "I need to resolve this now.":
                    call introspect_conflict
                    
                "Not now. I'll deal with it later.":
                    $ game_state.adjust_emotions({"overwhelm": 5})
                    "You push it down. The tension remains."
    
    # THEN show normal alignment feedback
    if last_interpretation["aligns"]:
        # Aligned with reality - world becomes clearer
        # But if there's a conflict, clarity is reduced
        if has_conflict:
            "The interpretation itself feels right, but the conflict clouds everything."
            play sound "soft_harmonic.mp3"
            show partial_clarity_overlay with dissolve
            hide partial_clarity_overlay with dissolve
        else:
            play sound "soft_harmonic.mp3"
            show clarity_overlay with dissolve
            "Everything feels right. Clear. True."
            hide clarity_overlay with dissolve
        
    else:
        # Misaligned with reality - world distorts
        # Conflict makes it worse
        if has_conflict:
            "Not only is the interpretation distorted, but the conflict amplifies everything."
            play sound "reality_glitch_harsh.mp3"
            show severe_distortion_overlay with dissolve
            hide severe_distortion_overlay with dissolve
        else:
            play sound "reality_glitch.mp3"
            show distortion_overlay with dissolve
            "Your head throbs. The world feels unstable."
            hide distortion_overlay with dissolve
    
    # Show emotional state changes
    python:
        dominant_emotion = game_state.get_dominant_emotion()
    
    if dominant_emotion:
        "You feel: {i}[dominant_emotion]{/i}"
    
    # Check for reality shift
    python:
        # Conflicts increase shift severity
        base_severity = None
        
        # If player has misinterpreted many times in a row
        if game_state.interpretation_streak["negative"] >= 3:
            base_severity = "moderate"
        # If overwhelmed
        elif game_state.emotions["overwhelm"] >= 70:
            base_severity = "severe"
        
        # Conflicts can escalate severity
        if has_conflict and conflict_data["total_distress"] >= 30:
            if base_severity == "moderate":
                shift_severity = "severe"
            elif base_severity is None:
                shift_severity = "moderate"
            else:
                shift_severity = base_severity
            should_shift = True
        elif base_severity:
            shift_severity = base_severity
            should_shift = True
        else:
            should_shift = False
    
    if should_shift:
        call trigger_reality_shift(shift_severity, "belief conflict and misinterpretation")
    
    return

# NEW: Encounter that specifically triggers conflicts
label encounter_conflicting_scenario:
    """
    Example encounter designed to activate conflicting beliefs
    Use this pattern to deliberately surface conflicts
    """
    
    scene cafe with fade
    
    "Someone you know sees you and waves enthusiastically. 'Hey! Come sit with us!'"
    
    menu:
        "Join them. They want to spend time with me.":
            # Activates: I'm worthy + others are friendly
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("others.are-friendly", BELIEF_INTENSITY_ACTIVE)
            
            # BUT if player also believes they're unworthy...
            python:
                if game_state.beliefs.get("self.is-unworthy", 0) >= BELIEF_INTENSITY_ACTIVE:
                    # CONFLICT! They just activated "worthy" but already believe "unworthy"
                    has_immediate_conflict = True
                else:
                    has_immediate_conflict = False
            
            mc "Yeah, I'd love to!"
            
            if has_immediate_conflict:
                "You walk over, but something feels wrong."
                "Part of you wants to believe they're glad to see you."
                "But another part whispers: 'They're just being polite. You're not really wanted.'"
                
                # Conflict will be detected in show_interpretation_consequence
            else:
                "You join them. It feels natural. Good."
            
        "Decline. They don't really want me there.":
            # Activates: I'm unworthy + others are threatening
            $ game_state.activate_belief("self.is-unworthy", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("others.are-threatening", BELIEF_INTENSITY_SURFACE)
            
            # BUT if player believes they're worthy...
            python:
                if game_state.beliefs.get("self.is-worthy", 0) >= BELIEF_INTENSITY_ACTIVE:
                    # CONFLICT!
                    has_immediate_conflict = True
                else:
                    has_immediate_conflict = False
            
            mc "Oh, I... I have to go. Sorry!"
            
            if has_immediate_conflict:
                "You walk away quickly."
                "Part of you knows you deserve connection."
                "But fear overrides it. 'Better safe than rejected.'"
            else:
                "You leave. Alone feels safer."
    
    # Store for consequence phase
    $ last_interpretation = {
        "aligns": True if has_immediate_conflict == False else False,
        "internal_thought": "I can trust this" if has_immediate_conflict == False else "I can't trust this"
    }
    
    # This will now detect and show conflicts
    call show_interpretation_consequence
    
    return

# Helper: Pre-check if a choice will create conflict
# Use this to show warnings to player if they have deep introspection
init python:
    def will_create_conflict(belief_ids_to_activate):
        """
        Check if activating these beliefs will create conflicts
        Returns True if conflict will occur
        """
        
        for new_belief in belief_ids_to_activate:
            if new_belief not in beliefs:
                continue
            
            conflicts_with = beliefs[new_belief].get("conflicts_with", [])
            
            for conflicting_id in conflicts_with:
                # Check if player already has the conflicting belief active
                if game_state.beliefs.get(conflicting_id, 0) >= BELIEF_INTENSITY_SURFACE:
                    return True
        
        return False

# Example usage in menu
label example_conflict_aware_choice:
    """
    Show conflict warning if player has high introspection depth
    """
    
    menu:
        "I deserve love." if game_state.introspection_depth < 4:
            # Normal - no warning
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
            
        "I deserve love. {color=#ffaa00}(!){/color}" if game_state.introspection_depth >= 4 and will_create_conflict(["self.is-worthy"]):
            # Warning shown - player knows this will conflict
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
            
            "You notice the conflict arising even as you think it."
            
        "I deserve love." if game_state.introspection_depth >= 4 and not will_create_conflict(["self.is-worthy"]):
            # High awareness, no conflict
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
    
    return
