# ENCOUNTER LOOP - The Core Introspection Mini-Game
# This is where players navigate hypothetical scenarios to discover their beliefs

label encounter_loop_start:
    # Main entry point for the encounter mini-game.
    # Called from therapy sessions or between story chapters.
    
    python:
        if game_state is None:
            game_state = GameState()

    # Set game phase
    $ game_state.phase = GAME_PHASE_ENCOUNTER
    
    # Visual transition to introspection space
    scene introspection_space with fade
    play music "introspection_ambient.mp3" fadein 2.0
    
    # Dr. Chen guides the player
    show therapist_guide at center with dissolve
    
    therapist "Let's explore some scenarios together, [player_name]."
    
    therapist "I'm going to describe situations. Just... notice how you react. What you feel. What you believe."
    
    therapist "There are no wrong answers here. Only discoveries."
    
    hide therapist_guide with dissolve
    
    # Start the encounter loop
    jump encounter_loop

label encounter_loop:
    # Main loop - select and present encounters based on game state
    
    # Check if we should end the session
    python:
        # End conditions
        should_end = False
        
        # End after 5 encounters
        if game_state.scene_count >= 5:
            should_end = True
        
        # End if player is too overwhelmed
        if game_state.emotions["overwhelm"] >= 80:
            should_end = True
        
        # End if significant breakthrough happened
        if game_state.introspection_depth >= 5:
            should_end = True
    
    if should_end:
        jump encounter_loop_end
    
    # Select next encounter
    python:
        # DEBUG: Check what we have
        print(f"DEBUG: encounters dict has {len(encounters)} entries")
        print(f"DEBUG: encounters keys: {list(encounters.keys())}")

        encounter_router = EncounterRouter()
        # Populate the vault with all encounters
        # TODO maybe filter out based on an encounter property like "only_once"
        encounter_router.encounter_vault = encounters

        # DEBUG: Check vault
        print(f"DEBUG: vault has {len(encounter_router.encounter_vault)} entries")

        encounter_router.used_encounters = game_state.completed_encounters
        
        # Select based on current emotional state and beliefs
        selected = encounter_router.select_encounter(game_state)
        
        if selected:
            game_state.current_encounter = selected
            game_state.scene_count += 1
    
    # Present the encounter
    if game_state.current_encounter:
        call present_encounter(game_state.current_encounter)
    
    # Loop back
    jump encounter_loop

label present_encounter(encounter):
    # Present a single encounter to the player
    
    # Set the scene
    python:
        scene_bg = encounter.get("scene", "introspection_space")
    
    scene expression scene_bg with fade
    
    # Show context
    if "context" in encounter:
        "[encounter['context']]"
    
    # The observation - what actually happens
    "[encounter['observation']]"
    
    # INTERPRETATION PHASE
    $ game_state.phase = GAME_PHASE_INTERPRET
    
    # Pause for player to notice their reaction
    menu:
        "How does this make you feel?"
        
        "I feel anxious.":
            $ game_state.adjust_emotions({"anxiety": 5})
            
        "I feel curious.":
            $ game_state.adjust_emotions({"clarity": 5})
            
        "I feel nothing really.":
            $ game_state.adjust_emotions({"isolation": 5})
        
        "I'm not sure yet.":
            pass
    
    # Now present interpretation options
    # Each interpretation activates different beliefs
    call choose_interpretation(encounter)
    
    # Show consequence of interpretation
    call show_interpretation_consequence
    
    # Offer introspection if warranted
    python:
        should_introspect = game_state.is_ready_for_introspection()
    
    if should_introspect:
        menu:
            "Do you want to examine what just happened?"
            
            "Yes, let me reflect on this.":
                call introspection_examine
                
            "No, keep going.":
                pass
    
    # Mark encounter as completed
    $ game_state.completed_encounters.append(encounter["id"])
    
    return

label choose_interpretation(encounter):
    # Player chooses how to interpret the encounter
    # This is where beliefs get activated
    
    scene introspection_space with dissolve
    
    # Show encounter image if it exists
    if "image" in encounter:
        show expression encounter["image"] at center with dissolve
    
    # Show observation
    "[encounter['observation']]"
    
    if "context" in encounter:
        "{i}[encounter['context']]{/i}"
    
    # BUILD MENU FROM INTERPRETATIONS
    python:
        # Build menu items from interpretations
        menu_items = []
        interpretations = encounter.get("interpretations", [])
        
        for interp in interpretations:
            # Add display text and the full interpretation dict
            menu_items.append((interp["display"], interp))
    
    # Present as standard RenPy menu (buttons at bottom)
    python:
        chosen_interpretation = renpy.display_menu(menu_items, interact=True)
    
    # Update image based on choice if needed
    if chosen_interpretation and "result_image" in chosen_interpretation:
        show expression chosen_interpretation["result_image"] at center with dissolve
    
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
            
            # Track interpretation type
            if chosen_interpretation.get("aligns", True):
                game_state.interpretation_streak["positive"] += 1
                game_state.interpretation_streak["negative"] = 0
            else:
                game_state.interpretation_streak["negative"] += 1
                game_state.interpretation_streak["positive"] = 0
            
            # Store for consequence display
            last_interpretation = chosen_interpretation

    python:
        needs_therapy = False
        therapy_label = None
        
        if chosen_interpretation and not chosen_interpretation.get("aligns", True):
            # Negative choice - check if we should intervene
            if "therapy_label" in chosen_interpretation:
                # Check if emotion high enough to warrant intervention
                dominant = game_state.get_dominant_emotion()
                if dominant and game_state.emotions.get(dominant, 0) >= 50:
                    needs_therapy = True
                    therapy_label = chosen_interpretation["therapy_label"]
    
    # Call therapy if needed
    if needs_therapy and therapy_label:
        call expression therapy_label
    
    return

label show_interpretation_consequence:
    # Show the player what their interpretation does
    
    $ game_state.phase = GAME_PHASE_CONSEQUENCE
    
    scene introspection_space with dissolve
    
    # Show internal thought
    if "internal_thought" in last_interpretation:
        "Your thought: {i}[last_interpretation['internal_thought']]{/i}"
    
    # Visual feedback based on alignment
    if last_interpretation["aligns"]:
        # Aligned with reality - world becomes clearer
        play sound "soft_harmonic.mp3"
        show clarity_overlay with dissolve
        
        "Something feels... right. Like pieces clicking into place."
        
        hide clarity_overlay with dissolve
        
    else:
        # Misaligned with reality - world distorts
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
        # If player has misinterpreted many times in a row
        if game_state.interpretation_streak["negative"] >= 3:
            # Trigger moderate reality shift
            should_shift = True
            shift_severity = "moderate"
        # If overwhelmed
        elif game_state.emotions["overwhelm"] >= 70:
            should_shift = True
            shift_severity = "severe"
        else:
            should_shift = False
    
    if should_shift:
        call trigger_reality_shift(shift_severity, "repeated misinterpretation")
    
    return

label introspection_examine:
    # Deep introspection - player examines the beliefs that were activated
    
    $ game_state.phase = GAME_PHASE_INTROSPECT
    $ game_state.introspection_depth += 1
    
    scene introspection_deep with fade
    play music "introspection_deep.mp3" fadein 2.0
    
    "You sit with what just happened."
    
    "Not judging. Not justifying. Just... observing."
    
    # Show the beliefs that were just activated
    python:
        activated_beliefs = []
        
        if last_interpretation and "activates" in last_interpretation:
            for belief_id in last_interpretation["activates"]:
                if belief_id in beliefs:
                    activated_beliefs.append(beliefs[belief_id])
    
    if activated_beliefs:
        "You notice these thoughts:"
        
        python:
            for belief in activated_beliefs:
                renpy.say(None, f"• {belief['statement']}")
    
    menu:
        "What do you see when you look at these thoughts?"
        
        "These thoughts define me. They're the truth.":
            "You accept them fully. They sink deeper."
            
            python:
                # Strengthen the beliefs
                for belief_id in last_interpretation["activates"]:
                    current = game_state.beliefs.get(belief_id, 0)
                    if current < BELIEF_INTENSITY_CORE:
                        game_state.activate_belief(belief_id, current + 1)
            
        "These are just thoughts. They might not be true.":
            $ game_state.introspection_depth += 1
            
            "A shift. Subtle but profound. You're separating yourself from your thoughts."
            
            play sound "soft_harmonic.mp3"
            
            "These beliefs... they're not YOU. They're just patterns you've been running."
            
            menu:
                "What do you want to do with them?"
                
                "Examine them more closely.":
                    call introspection_examine_deeper
                    
                "Let them go for now.":
                    $ game_state.adjust_emotions({"clarity": 10, "overwhelm": -10})
                    "You release them. Not forcing anything. Just... letting go."
        
        "I don't know. This is confusing.":
            $ game_state.adjust_emotions({"overwhelm": 5})
            "That's okay. Understanding takes time."
    
    scene introspection_space with fade
    stop music fadeout 2.0
    play music "introspection_ambient.mp3" fadein 2.0
    
    return

label introspection_examine_deeper:
    # Deep examination of a specific belief - potential resolution
    
    $ game_state.phase = GAME_PHASE_RESOLUTION
    
    scene introspection_deep_focus with fade
    
    # Get active negative beliefs
    python:
        negative_beliefs_active = game_state.get_active_negative_beliefs()
        
        examining_belief = None
        
        if negative_beliefs_active:
            # Pick the most intense one
            belief_intensities = [(b, game_state.beliefs.get(b, 0)) 
                                for b in negative_beliefs_active]
            belief_intensities.sort(key=lambda x: x[1], reverse=True)
            
            if belief_intensities:
                examining_belief_id = belief_intensities[0][0]
                examining_belief = beliefs.get(examining_belief_id)
    
    if examining_belief:
        "You focus on one belief in particular:"
        
        "'{i}[examining_belief['statement']]{/i}'"
        
        "Where did this come from? Has it always been true?"
        
        menu:
            "When did you first start believing this?"
            
            "I can't remember. It's always been there.":
                "So deep you can't see its origin. That's how core beliefs work."
                
                "But just because something has been there a long time..."
                "...doesn't mean it's true."
                
            "I remember. Someone told me this, or showed me.":
                "An old wound. An old voice."
                
                "But that was then. Is it still true now?"
                
            "I'm not sure.":
                "That uncertainty? That's the first crack in the belief."
        
        menu:
            "What would happen if this belief wasn't true?"
            
            "I don't know. It's scary to imagine.":
                $ game_state.adjust_emotions({"anxiety": 10})
                "Fear. The belief's last defense."
                
            "I think... I might feel lighter. Freer.":
                $ game_state.adjust_emotions({"hope": 15, "clarity": 10})
                
                "Yes. You see it now."
                
                "This belief has been a weight. Not a truth."
                
                # Check if resolution is available
                python:
                    resolution_belief_id = examining_belief.get("resolution")
                    
                    if resolution_belief_id and resolution_belief_id in beliefs:
                        resolution_belief = beliefs[resolution_belief_id]
                
                if resolution_belief:
                    "What if instead, you believed:"
                    
                    "'{i}[resolution_belief['statement']]{/i}'"
                    
                    menu:
                        "Does this feel more true?"
                        
                        "Yes. This resonates.":
                            # RESOLUTION HAPPENS
                            play sound "resolution_harmonic.mp3"
                            scene introspection_resolution with flash
                            
                            $ game_state.resolve_belief(examining_belief["id"], None)
                            $ game_state.activate_belief(resolution_belief_id, BELIEF_INTENSITY_EXAMINED)
                            $ game_state.introspection_depth += 2
                            
                            "The old belief dissolves."
                            "The new belief takes root."
                            
                            "Not forced. Not fake. Just... true."
                            
                            $ game_state.adjust_emotions({"hope": 20, "clarity": 20, "anxiety": -15, "overwhelm": -10})
                            
                            "Reality stabilizes. Everything becomes clearer."
                            
                        "I want to, but I'm not ready yet.":
                            "That's okay. Seeds have been planted."
                            
                            # Mark belief as examined
                            $ game_state.beliefs[examining_belief["id"]] = BELIEF_INTENSITY_EXAMINED
                            
                            "When you're ready, it will be here waiting."
            
            "I need more time to think about this.":
                "Take all the time you need."
                
                # Mark as examined
                $ game_state.beliefs[examining_belief["id"]] = BELIEF_INTENSITY_EXAMINED
    
    scene introspection_space with fade
    
    return

label encounter_loop_end:
    # End the encounter session - return to therapy or story
    
    $ game_state.phase = GAME_PHASE_REFLECTION
    
    scene introspection_space with fade
    show therapist_guide at center with dissolve
    
    therapist "Let's pause there for today."
    
    # Reflection based on performance
    python:
        total_positive = game_state.interpretation_streak.get("positive", 0)
        total_resolved = sum(1 for intensity in game_state.beliefs.values() 
                            if intensity == BELIEF_INTENSITY_RESOLVED)
    
    if total_resolved > 0:
        therapist "You've made real progress, [player_name]. You resolved [total_resolved] belief[s] today."
        
        therapist "That's not easy work. That takes courage."
        
    elif game_state.emotions["overwhelm"] >= 70:
        therapist "I can see you're overwhelmed. That's okay. This is hard work."
        
        therapist "We'll take it slower next time."
        
        $ game_state.adjust_emotions({"overwhelm": -20})
        
    else:
        therapist "You're learning to observe your thoughts. To question them."
        
        therapist "That's the first step toward freedom."
    
    therapist "How do you feel?"
    
    menu:
        "Exhausted but... good.":
            $ game_state.adjust_emotions({"hope": 5})
            mc "Exhausted but... good. Like I learned something."
            
            therapist "Good exhaustion. The kind that comes from real work."
            
        "Confused. I don't understand what we're doing.":
            therapist "That's natural. Understanding comes slowly."
            
            therapist "For now, just trust the process."
            
        "Ready to do more.":
            $ game_state.adjust_emotions({"hope": 10, "clarity": 5})
            mc "Ready to do more. I want to keep going."
            
            therapist "I admire your determination. But rest is important too."
    
    hide therapist_guide with dissolve
    scene black with fade
    stop music fadeout 2.0
    
    # Reset for next session
    $ game_state.scene_count = 0
    $ game_state.phase = GAME_PHASE_STORY
    
    return
