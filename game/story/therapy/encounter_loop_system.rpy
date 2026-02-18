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
    # FIXED: Removed double presentation - flow now goes smoothly from
    # context → observation → feeling → interpretation in one sequence
    
    # Set the scene
    python:
        scene_bg = encounter.get("scene", "introspection_space")
    
    scene expression scene_bg with fade
    
    # Show context (sets up the scenario)
    if "context" in encounter:
        "[encounter['context']]"
    
    # The observation - what actually happens
    "[encounter['observation']]"
    
    # INTERPRETATION PHASE
    $ game_state.phase = GAME_PHASE_INTERPRET
    
    # Show encounter image if it exists
    if "image" in encounter:
        show expression encounter["image"] at center with dissolve
    
    # Combined feeling + interpretation flow
    # Player notices their reaction, then immediately chooses how to interpret
    "You notice your reaction to this..."
    
    menu:
        "What's your first instinct about what this means?"
        
        "I feel anxious about this.":
            $ game_state.adjust_emotions({"anxiety": 5})
            # Now show interpretation options with anxiety tint
            call choose_interpretation(encounter, "anxious")
            
        "I feel curious about this.":
            $ game_state.adjust_emotions({"clarity": 5})
            # Show interpretation options with curiosity
            call choose_interpretation(encounter, "curious")
            
        "I feel nothing really.":
            $ game_state.adjust_emotions({"isolation": 5})
            # Show interpretation options with detachment
            call choose_interpretation(encounter, "detached")
        
        "I'm not sure yet. Let me think.":
            # Show interpretation options neutrally
            call choose_interpretation(encounter, "neutral")
    
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

label choose_interpretation(encounter, feeling_tone="neutral"):
    # Player chooses how to interpret the encounter
    # This is where beliefs get activated
    # FIXED: No longer re-displays context/observation (already shown in present_encounter)
    
    # Build menu from interpretations with feeling-tone appropriate framing
    python:
        menu_items = []
        interpretations = encounter.get("interpretations", [])
        
        # Add feeling-tone specific intro text
        feeling_intro = {
            "anxious": "Your anxiety makes certain interpretations feel more likely...",
            "curious": "Your curiosity opens up different possibilities...",
            "detached": "Your detachment makes it hard to connect, but you try...",
            "neutral": "You consider what this might mean..."
        }
    
    # Show feeling-appropriate intro
    "[feeling_intro.get(feeling_tone, feeling_intro['neutral'])]"
    
    # Build menu items from interpretations
    python:
        for interp in interpretations:
            # Add display text and the full interpretation dict
            menu_items.append((interp["display"], interp))
    
    # Present as standard RenPy menu
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
            store.last_interpretation = chosen_interpretation

    # THERAPY INTERVENTION CHECK
    # Wire up therapy interventions for negative interpretations
    python:
        needs_therapy = False
        therapy_label = None
        
        if chosen_interpretation and not chosen_interpretation.get("aligns", True):
            # Negative choice - ALWAYS offer therapy guidance
            # This is the key fix: therapy guides the player to insight
            if "therapy_label" in chosen_interpretation:
                needs_therapy = True
                therapy_label = chosen_interpretation["therapy_label"]
            else:
                # Auto-generate therapy label from belief if not specified
                activated_beliefs = chosen_interpretation.get("activates", [])
                if activated_beliefs:
                    # Map common beliefs to therapy labels
                    # All negative beliefs are misaligned - therapy helps realign
                    belief_to_therapy = {
                        "self.is-unworthy": "encounter_therapy_self_unworthy",
                        "self.is-fundamentally-flawed": "encounter_mirror_moment_see_flaws",
                        "self.must-earn-love": "encounter_therapy_breathing_room_feel_guilty",
                        "others.are-threatening": "encounter_therapy_stray_dog_fear",
                        "others.use-me": "encounter_therapy_shared_grief_withdraw",
                        "abandonment.is-inevitable": "encounter_therapy_abandonment",
                        "world.is-dangerous": "encounter_therapy_stray_dog_fear",
                        "existence.is-meaningless-negative": "encounter_therapy_random_kindness_meaningless",
                        "self.is-failure": "encounter_therapy_self_failure",
                        "others.are-better": "encounter_therapy_others_better",
                    }
                    for belief_id in activated_beliefs:
                        if belief_id in belief_to_therapy:
                            therapy_label = belief_to_therapy[belief_id]
                            needs_therapy = True
                            break
    
    # Call therapy if needed - this is the guided conversation
    if needs_therapy and therapy_label:
        # Check if the therapy label actually exists before calling
        $ has_label = renpy.has_label(therapy_label)
        if has_label:
            call expression therapy_label
        else:
            # Fallback: show a generic therapy moment
            call therapy_generic_negative
    
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
    # IMPROVED: More gradual, guided conversation before offering resolution
    # The player should feel "oh wow I never saw it that way" not "ya ya I know"
    
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
        
        # PHASE 1: Gentle exploration - not confronting, just curious
        "Let's approach this gently. No judgment. Just curiosity."
        
        "When this belief shows up in your life, what does it feel like in your body?"
        
        menu:
            "It feels like a weight. Heavy. Pressing down.":
                $ game_state.adjust_emotions({"awareness": 10})
                "Interesting. Where do you feel that weight most?"
                
                menu:
                    "In my chest. Like I can't breathe fully.":
                        "The chest. The center of vulnerability. This belief has been protecting something there."
                        
                    "In my stomach. A knot I can't untie.":
                        "The gut. Where we process what we can't digest. This belief has been holding something undigested."
                        
                    "In my shoulders. Tension I can't release.":
                        "The shoulders. Where we carry what we think is ours to bear alone. This belief has been isolating you."
            
            "It feels like a tightness. Contracted. Small.":
                $ game_state.adjust_emotions({"awareness": 10})
                "Contracted. As if making yourself smaller keeps you safer."
                "What would happen if you expanded instead?"
            
            "It feels like numbness. Blank. Empty.":
                $ game_state.adjust_emotions({"awareness": 10})
                "Numbness is protection. It means the original pain was too much to feel."
                "The belief is guarding you from something. What might that be?"
        
        # PHASE 2: Trace the belief's origin with compassion
        "Now, let's get curious about where this belief came from."
        
        "Not to blame anyone. Just to understand."
        
        menu:
            "It feels like it's always been there. I can't remember a time without it.":
                "Then it was planted very young. Before you had words for it."
                
                "Children absorb the emotional atmosphere around them like sponges."
                
                "If the people around you believed something about themselves..."
                "...you would have inherited that belief without question."
                
                "It's not your fault for having it. It's just what happened."
            
            "I remember when it started. A specific moment or person.":
                "That moment was real. The pain was real."
                
                "But here's what's interesting: a child's mind doesn't understand complexity."
                
                "When something hurt, the child's mind decided: 'This must mean something about ME.'"
                
                "Because if it's about you, you can try to fix it. If it's about them... you're powerless."
                
                "So the belief was a kind of control. A way to make sense of something senseless."
            
            "I think I learned it from watching others. The way they treated themselves.":
                "We learn by watching. By absorbing what's normal."
                
                "If the people around you carried this belief like a shadow..."
                "...you would have thought: 'This is just how people are.'"
                
                "But it wasn't how people ARE. It was how THEY were."
        
        # PHASE 3: Examine what the belief has been trying to do
        "Every belief, even the painful ones, started as an attempt to help."
        
        "What do you think this belief has been trying to do for you?"
        
        menu:
            "It's been trying to keep me safe from rejection.":
                "Yes. By making you smaller, quieter, less visible... it thought it could protect you."
                
                "But here's the question: has it actually worked?"
                
                menu:
                    "No. I still feel rejected. Just... preemptively.":
                        "Exactly. The belief rejects you before anyone else can."
                        
                        "It's been rejecting you on their behalf. For years."
                        
                        "You've been carrying their potential rejection as if it already happened."
                        
                        $ game_state.adjust_emotions({"clarity": 15, "grief": 5})
                    
                    "Sometimes. But the cost has been too high.":
                        "And what has that cost been?"
                        
                        menu:
                            "I've hidden parts of myself. Never let anyone see the real me.":
                                "So you've been safe from their rejection of a false self..."
                                "...but isolated from ever being truly known."
                                
                                "That's not safety. That's exile."
                            
                            "I've missed opportunities. Chances to connect. To grow.":
                                "The belief closed doors before you could even knock."
                                
                                "It thought it was protecting you from failure."
                                "But it was protecting you from life."
            
            "It's been trying to make me better. Push me to improve.":
                "Ah, the belief that criticism creates growth."
                
                "But let me ask you: would you treat a child this way to help them learn?"
                
                menu:
                    "No... I'd be gentle. Encouraging.":
                        "Exactly. The belief that shame motivates is a lie."
                        
                        "Shame contracts. It makes us hide. It makes us small."
                        
                        "Growth requires safety. Encouragement. The room to make mistakes."
                        
                        "This belief has been holding you back while pretending to push you forward."
                        
                        $ game_state.adjust_emotions({"clarity": 15})
                    
                    "Yes. Pain is a teacher.":
                        "Pain teaches us that something is wrong."
                        
                        "But it doesn't teach us what's right."
                        
                        "A child who touches a hot stove learns not to touch it again."
                        
                        "But that doesn't teach them how to cook."
        
        # PHASE 4: Now ask if they're ready to see it differently
        "Here's what I want you to consider:"
        
        "This belief was a child's solution to a grown-up problem."
        
        "It made sense when you were small. When you had no power. When you were just trying to survive."
        
        "But you're not that child anymore."
        
        "And the world is not the same threatening place it was then."
        
        menu:
            "I'm starting to see it differently.":
                $ game_state.adjust_emotions({"hope": 15, "clarity": 20})
                
                "That shift you feel? That's the belief loosening its grip."
                
                # Check if resolution is available
                python:
                    resolution_belief_id = examining_belief.get("resolution")
                    resolution_belief = None
                    
                    if resolution_belief_id and resolution_belief_id in beliefs:
                        resolution_belief = beliefs[resolution_belief_id]
                
                if resolution_belief:
                    "What if you could believe something new instead?"
                    
                    "Not because I'm telling you to. But because it feels more true to who you are now."
                    
                    "What if:"
                    
                    "'{i}[resolution_belief['statement']]{/i}'"
                    
                    menu:
                        "That... actually feels like a relief. Like something I needed to hear.":
                            # RESOLUTION HAPPENS
                            play sound "resolution_harmonic.mp3"
                            scene introspection_resolution with flash
                            
                            $ game_state.resolve_belief(examining_belief["id"], None)
                            $ game_state.activate_belief(resolution_belief_id, BELIEF_INTENSITY_EXAMINED)
                            $ game_state.introspection_depth += 2
                            
                            "The old belief dissolves."
                            "The new belief takes root."
                            
                            "Not forced. Not fake. Just... finally true."
                            
                            $ game_state.adjust_emotions({"hope": 20, "clarity": 20, "anxiety": -15, "overwhelm": -10})
                            
                            "Reality stabilizes. Everything becomes clearer."
                            
                        "I want to believe it, but I'm not quite there yet.":
                            "That's okay. Real change isn't about flipping a switch."
                            
                            "You've seen the old belief for what it is: a child's protection that's no longer needed."
                            
                            # Mark belief as examined
                            $ game_state.beliefs[examining_belief["id"]] = BELIEF_INTENSITY_EXAMINED
                            
                            "The seed has been planted. Let it grow in its own time."
                    
                else:
                    # No resolution belief defined - just mark as examined
                    $ game_state.beliefs[examining_belief["id"]] = BELIEF_INTENSITY_EXAMINED
                    $ game_state.adjust_emotions({"hope": 10, "clarity": 10})
                    
                    "You've seen through the belief. That's the first step."
                    
                    "In time, you'll discover what wants to take its place."
            
            "I understand what you're saying, but I'm not ready to let go yet.":
                "That's okay. Beliefs are stubborn. They don't surrender easily."
                
                "But you've done something important today: you've SEEN it."
                
                "You can't unsee it now. Every time this belief shows up..."
                "...you'll recognize it. Question it. Choose differently."
                
                # Mark as examined
                $ game_state.beliefs[examining_belief["id"]] = BELIEF_INTENSITY_EXAMINED
                $ game_state.adjust_emotions({"clarity": 5})
                
                "That's how change happens. Not in a single moment. In a thousand small recognitions."
    
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

# ============================================================================
# GENERIC THERAPY INTERVENTION
# Fallback when no specific therapy label exists for a belief
# ============================================================================

label therapy_generic_negative:
    # Generic therapy intervention for negative interpretations
    # Used when no specific therapy_label is defined
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "I noticed something just now. Something in how you interpreted that."
    
    dr_chen "The meaning you gave to that situation... it came from somewhere inside you."
    
    dr_chen "Not from the situation itself."
    
    python:
        # Get the belief that was just activated
        activated = []
        if last_interpretation and "activates" in last_interpretation:
            activated = last_interpretation.get("activates", [])
        
        belief_statement = "a negative belief about yourself"
        if activated and activated[0] in beliefs:
            belief_statement = beliefs[activated[0]]["statement"]
    
    dr_chen "You just activated: '{i}[belief_statement]{/i}'"
    
    dr_chen "Is that really true? Or is it just... familiar?"
    
    menu:
        "It feels true. I've believed it for so long.":
            dr_chen "Familiar feels like true. But they're not the same thing."
            
            dr_chen "You've been practicing this thought for years. Of course it feels natural."
            
            dr_chen "But what if it's just a habit? Not a truth?"
            
            menu:
                "A habit I could change?":
                    $ game_state.adjust_emotions({"hope": 10, "clarity": 10})
                    $ game_state.introspection_depth += 1
                    
                    dr_chen "Exactly. Habits can be changed. They take time, but they're not permanent."
                    
                    dr_chen "Every time you notice this belief and question it..."
                    dr_chen "...you weaken its grip."
                    
                    scene therapy_office_clear with dissolve
                    
                    dr_chen "That's the work. Not forcing yourself to believe something different."
                    dr_chen "Just noticing. Questioning. Choosing differently, one moment at a time."
                
                "But what if it IS true?":
                    dr_chen "Then let it be true. But let it be examined."
                    
                    dr_chen "If it survives your honest scrutiny, it will be stronger for it."
                    
                    dr_chen "But most beliefs like this... they crumble when we really look at them."
                    
                    dr_chen "Not because we force them to. Because they were never solid to begin with."
        
        "I'm not sure anymore. You're making me question it.":
            $ game_state.adjust_emotions({"clarity": 15, "hope": 5})
            $ game_state.introspection_depth += 1
            
            dr_chen "Good. That questioning? That's the beginning of freedom."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "The belief has been running on autopilot. Now you've seen it."
            
            dr_chen "You can't unsee it. And that changes everything."
    
    return
