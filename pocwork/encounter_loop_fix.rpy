# FIX FOR ENCOUNTER LOOP - Dynamic Menu Issue

# The problem: RenPy menus can't be empty
# Solution: Build menu items dynamically using Python

# Replace the problematic section in your encounter_loop_system.rpy with this:

label show_interpretation_choice:
    # Show interpretation choices to player
    
    $ game_state.phase = GAME_PHASE_INTERPRET
    
    # Get current encounter
    python:
        encounter = game_state.current_encounter
        
        if not encounter:
            renpy.say(None, "Error: No encounter loaded")
            return
    
    # Show the observation
    "[encounter['observation']]"
    
    # Show context if available
    if "context" in encounter:
        "{i}[encounter['context']]{/i}"
    
    # BUILD DYNAMIC MENU
    # RenPy requires we construct menu items programmatically
    
    python:
        # Create menu items list
        menu_items = []
        
        for interp in encounter["interpretations"]:
            # Each item is a tuple: (display_text, interpretation_data)
            menu_items.append((interp["display"], interp))
        
        # Use renpy.display_menu to show dynamic choices
        # This returns the chosen item
        chosen_interpretation = renpy.display_menu(menu_items)
        
        # If user didn't choose (shouldn't happen), pick first
        if chosen_interpretation is None:
            chosen_interpretation = encounter["interpretations"][0]
    
    # Show player's internal thought
    if "internal_thought" in chosen_interpretation:
        mc "{i}[chosen_interpretation['internal_thought']]{/i}"
    
    # Apply the interpretation
    python:
        # Activate beliefs
        for belief_id in chosen_interpretation["activates"]:
            intensity = chosen_interpretation.get("intensity", BELIEF_INTENSITY_ACTIVE)
            game_state.activate_belief(belief_id, intensity)
        
        # Adjust emotions
        emotion_shifts = chosen_interpretation.get("emotion_shift", {})
        game_state.adjust_emotions(emotion_shifts)
        
        # Track interpretation streak
        if chosen_interpretation.get("aligns", True):
            game_state.interpretation_streak["positive"] += 1
            game_state.interpretation_streak["negative"] = 0
        else:
            game_state.interpretation_streak["negative"] += 1
            game_state.interpretation_streak["positive"] = 0
        
        # Store for consequence display
        last_interpretation = chosen_interpretation
    
    # Show consequences
    call show_interpretation_consequence
    
    return


# ALTERNATIVE APPROACH: Use a custom screen instead of menu
# This is more flexible and avoids the menu limitation entirely

screen interpretation_choice_screen(interpretations):
    """
    Custom screen for choosing interpretations
    More control than menu
    """
    
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        background Solid("#000000dd")
        padding (30, 30)
        
        vbox:
            spacing 20
            
            text "How do you interpret this?" size 24 color "#ffffff" bold True
            
            null height 20
            
            # Show each interpretation as a button
            for i, interp in enumerate(interpretations):
                button:
                    xsize 740
                    ysize None
                    padding (20, 15)
                    background Frame("gui/button/choice_idle_background.png", 10, 10)
                    hover_background Frame("gui/button/choice_hover_background.png", 10, 10)
                    
                    action Return(interp)
                    
                    text interp["display"] size 18 color "#ffffff" xalign 0.0


# USAGE: Replace the menu section with this call

label show_interpretation_choice_v2:
    """
    Alternative version using custom screen
    """
    
    $ game_state.phase = GAME_PHASE_INTERPRET
    
    python:
        encounter = game_state.current_encounter
    
    "[encounter['observation']]"
    
    if "context" in encounter:
        "{i}[encounter['context']]{/i}"
    
    # Use custom screen instead of menu
    call screen interpretation_choice_screen(encounter["interpretations"])
    
    # Result is in _return
    $ chosen_interpretation = _return
    
    # Rest of the logic...
    if "internal_thought" in chosen_interpretation:
        mc "{i}[chosen_interpretation['internal_thought']]{/i}"
    
    python:
        for belief_id in chosen_interpretation["activates"]:
            intensity = chosen_interpretation.get("intensity", BELIEF_INTENSITY_ACTIVE)
            game_state.activate_belief(belief_id, intensity)
        
        game_state.adjust_emotions(chosen_interpretation.get("emotion_shift", {}))
        
        if chosen_interpretation.get("aligns", True):
            game_state.interpretation_streak["positive"] += 1
            game_state.interpretation_streak["negative"] = 0
        else:
            game_state.interpretation_streak["negative"] += 1
            game_state.interpretation_streak["positive"] = 0
        
        last_interpretation = chosen_interpretation
    
    call show_interpretation_consequence
    
    return


# RECOMMENDED: Use renpy.display_menu (cleanest solution)

label show_interpretation_choice_final:
    """
    RECOMMENDED VERSION - Clean and simple
    """
    
    $ game_state.phase = GAME_PHASE_INTERPRET
    
    python:
        encounter = game_state.current_encounter
    
    # Show observation
    "[encounter['observation']]"
    
    if "context" in encounter:
        "{i}[encounter['context']]{/i}"
    
    # BUILD AND SHOW MENU
    python:
        # Build menu items
        menu_items = []
        for interp in encounter["interpretations"]:
            menu_items.append((interp["display"], interp))
        
        # Show menu and get choice
        chosen_interpretation = renpy.display_menu(menu_items)
    
    # Show internal thought
    if chosen_interpretation and "internal_thought" in chosen_interpretation:
        mc "{i}[chosen_interpretation['internal_thought']]{/i}"
    
    # Apply effects
    python:
        if chosen_interpretation:
            # Activate beliefs
            for belief_id in chosen_interpretation.get("activates", []):
                intensity = chosen_interpretation.get("intensity", BELIEF_INTENSITY_ACTIVE)
                game_state.activate_belief(belief_id, intensity)
            
            # Adjust emotions
            game_state.adjust_emotions(chosen_interpretation.get("emotion_shift", {}))
            
            # Track streak
            if chosen_interpretation.get("aligns", True):
                game_state.interpretation_streak["positive"] += 1
                game_state.interpretation_streak["negative"] = 0
            else:
                game_state.interpretation_streak["negative"] += 1
                game_state.interpretation_streak["positive"] = 0
            
            # Store for later
            last_interpretation = chosen_interpretation
    
    # Show consequences
    call show_interpretation_consequence
    
    return


# INSTRUCTIONS FOR FIXING YOUR FILE:
# 
# 1. Find the label show_interpretation_choice in encounter_loop_system.rpy
# 2. Replace the entire label with show_interpretation_choice_final above
# 3. Or add the custom screen and use show_interpretation_choice_v2
# 
# The key issue: You had menu: with no choices defined inline
# RenPy requires at least one choice in a menu block
# Solution: Use renpy.display_menu() or a custom screen instead
