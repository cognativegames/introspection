# Reality shift function - called when player acts against beliefs
# Now integrated with game_state belief system

label trigger_reality_shift(severity="moderate", reason=""):
    # Determine shift level based on belief conflicts and reality_stability
    python:
        # First check for active belief conflicts
        has_conflicts = False
        conflict_count = 0
        
        if game_state:
            conflicts = game_state.detect_belief_conflicts()
            has_conflicts = len(conflicts) > 0
            conflict_count = len(conflicts)
        
        # Calculate base shift level from reality_stability
        if reality_stability <= 2:
            base_shift = "catastrophic"
        elif reality_stability <= 4:
            base_shift = "severe"
        elif reality_stability <= 6:
            base_shift = "moderate"
        elif reality_stability <= 8:
            base_shift = "minor"
        else:
            base_shift = "harmony"
        
        # Override with severity parameter OR use belief conflict severity
        if severity in shift_severity:
            shift_level = severity
        elif has_conflicts and conflict_count >= 2:
            # Multiple conflicts = more severe shift
            shift_level = "severe"
        elif has_conflicts:
            shift_level = "moderate"
        else:
            shift_level = base_shift
        
        shift_data = shift_severity[shift_level]
    
    # Visual effect
    if shift_level == "catastrophic":
        play sound "reality_shatter.mp3"
        scene void_nightmare with flash
        pause 0.5
        scene geometric_impossible with dissolve
        show pain_overlay with dissolve
        
    elif shift_level == "severe":
        play sound "reality_glitch_harsh.mp3"
        scene white with flash
        pause 0.3
        # Room transforms dramatically
        
    elif shift_level == "moderate":
        play sound "reality_glitch.mp3"
        # Flicker effect, details change
        
    elif shift_level == "minor":
        play sound "soft_glitch.mp3"
        # Subtle visual shift only
    
    # Physical pain response
    if shift_data["physical"] == "severe_headpain":
        mc "AHHH!"
        "[shift_data['message']]"
        "You collapse to your knees, hands clutching your skull. Behind your eyes, something fundamental is breaking."
        pause shift_data["duration"]
        
    elif shift_data["physical"] == "sharp_headpain":
        mc "Agh!"
        "[shift_data['message']]"
        "You stagger, vision swimming. The pain is sharp, accusatory."
        pause shift_data["duration"]
        
    elif shift_data["physical"] == "dull_throb":
        "[shift_data['message']]"
        pause shift_data["duration"]
        
    elif shift_data["physical"] == "brief_discomfort":
        "[shift_data['message']]"
        pause shift_data["duration"]
    
    # Optional introspection prompt for severe shifts
    if shift_level in ["catastrophic", "severe"]:
        menu:
            "What's happening to me?"
            
            "Stop. Breathe. Think about what you just did.":
                $ game_state.introspection_depth += 1
                call introspect(reason)
                
            "Push through the pain.":
                $ game_state.adjust_emotions({"anxiety": 5, "overwhelm": 3})
                "You grit your teeth and force yourself forward. The pain doesn't care about your determination."
                
            "I don't care. Keep going.":
                $ game_state.adjust_emotions({"clarity": -3})
                $ reality_stability -= 1
                "You ignore the warning. Your brain screams at you. You don't listen."
    
    return