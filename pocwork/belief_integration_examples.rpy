# EXAMPLES: How to integrate beliefs into gameplay

# Example 1: Check if a belief is active before showing dialogue option
label example_conditional_dialogue:
    
    scene some_location
    
    # Check if player has the "self.is-fundamentally-flawed" belief active
    python:
        has_negative_self_belief = game_state.beliefs.get("self.is-fundamentally-flawed", 0) >= BELIEF_INTENSITY_SURFACE
        has_positive_self_belief = game_state.beliefs.get("self.is-worthy", 0) >= BELIEF_INTENSITY_SURFACE
    
    "Someone compliments you on your work."
    
    menu:
        "Thank you, I worked hard on it." if has_positive_self_belief:
            # Only available if player believes they're worthy
            $ game_state.adjust_emotions({"hope": 10, "connection": 5})
            mc "Thank you, I worked hard on it."
            "You feel proud. Grounded."
            
        "I don't deserve that. It's not that good." if has_negative_self_belief:
            # Only available if player believes they're flawed
            $ game_state.adjust_emotions({"anxiety": 10, "isolation": 5})
            mc "I don't deserve that. It's not that good."
            "The compliment bounces off you. Nothing sticks."
            
        "Oh, thanks." if not has_negative_self_belief and not has_positive_self_belief:
            # Neutral response if no strong beliefs
            mc "Oh, thanks."
            "You accept it politely, without much feeling either way."
    
    return

# Example 2: Trigger reality shift when acting against belief
label example_belief_violation:
    
    scene party
    
    "Your friend asks you to lie for them. Cover up something they did."
    
    python:
        values_honesty = game_state.beliefs.get("values.honesty-over-kindness", 0) >= BELIEF_INTENSITY_ACTIVE
    
    menu:
        "Okay, I'll lie for you.":
            if values_honesty:
                # Player believes in honesty but chose to lie - VIOLATION
                "As the lie leaves your mouth, your head throbs."
                
                call trigger_reality_shift("moderate", "lied for a friend")
                
                $ game_state.adjust_emotions({"anxiety": 20, "clarity": -15})
                
                "You feel sick. Wrong. This isn't who you are."
            else:
                # No strong honesty belief - no violation
                mc "Okay, I'll lie for you."
                "You tell the lie. It doesn't feel great, but it doesn't tear you apart either."
                
        "I can't lie for you. I'm sorry.":
            if values_honesty:
                # Acting in ALIGNMENT with belief
                mc "I can't lie for you. I'm sorry."
                
                play sound "soft_harmonic.mp3"
                "The world feels solid. Right."
                
                $ game_state.adjust_emotions({"clarity": 15, "hope": 10})
                
                "You stood by your values. It hurts to disappoint them, but you feel grounded."
            else:
                mc "I can't lie for you. I'm sorry."
                "You refuse. Your friend looks hurt."
    
    return

# Example 3: Introspection to examine and potentially resolve a belief
label example_introspection_resolve:
    
    scene introspection_space
    
    "You sit with the belief that has been haunting you:"
    
    python:
        negative_beliefs = game_state.get_active_negative_beliefs()
        
        if negative_beliefs:
            examining_belief = negative_beliefs[0]  # Get the first active negative belief
            belief_data = beliefs[examining_belief]
    
    if belief_data:
        "[belief_data['statement']]"
        
        "Is this really true? Has it ever been true?"
        
        menu:
            "Yes. It's the truth about me.":
                # Reinforce the belief
                $ game_state.activate_belief(examining_belief, BELIEF_INTENSITY_CORE)
                "You double down. The belief sinks deeper."
                
            "No. It's a story I've been telling myself.":
                # Begin resolution process
                "You see it clearly now. This isn't truth. It's a narrative."
                
                python:
                    resolution_belief = belief_data.get("resolution")
                    
                    if resolution_belief:
                        game_state.resolve_belief(examining_belief)
                        game_state.activate_belief(resolution_belief, BELIEF_INTENSITY_SURFACE)
                
                play sound "soft_harmonic.mp3"
                scene therapy_room_clear with dissolve
                
                "The old belief begins to dissolve. Something new takes its place."
                
                if resolution_belief:
                    "[beliefs[resolution_belief]['statement']]"
                    
                    "This feels... lighter. More true."
    
    return

# Example 4: Encounter that triggers different beliefs based on interpretation
label example_encounter_interpretation:
    
    scene park
    
    "You see someone sitting alone on a bench, crying."
    
    menu:
        "Approach them and offer help.":
            python:
                # This choice might activate different beliefs depending on worldview
                if game_state.beliefs.get("others.are-friendly", 0) >= BELIEF_INTENSITY_SURFACE:
                    game_state.adjust_emotions({"connection": 15, "hope": 10})
                    interpretation = "compassionate"
                elif game_state.beliefs.get("others.are-threatening", 0) >= BELIEF_INTENSITY_SURFACE:
                    game_state.adjust_emotions({"anxiety": 10})
                    interpretation = "cautious"
                else:
                    interpretation = "neutral"
            
            if interpretation == "compassionate":
                "You approach naturally. People need help sometimes. That's just being human."
                
            elif interpretation == "cautious":
                "You approach carefully, ready to back away if needed. You never know with strangers."
                
            else:
                "You approach. Seems like the right thing to do."
                
        "Walk past. Not your problem.":
            python:
                if game_state.beliefs.get("self.is-fundamentally-flawed", 0) >= BELIEF_INTENSITY_ACTIVE:
                    # If you believe you're flawed, you might feel guilty
                    game_state.adjust_emotions({"anxiety": 15, "isolation": 10})
                    interpretation = "guilty"
                else:
                    interpretation = "practical"
            
            if interpretation == "guilty":
                "You walk past. Of course you'd ignore someone in pain. That's just who you are. Selfish."
                
                call trigger_reality_shift("minor", "ignored someone suffering")
                
            else:
                "You walk past. You can't fix everyone's problems."
    
    return

# Example 5: Showing belief history in a reflection scene
label example_belief_reflection:
    
    scene introspection_space with fade
    
    "You reflect on how your beliefs have changed..."
    
    python:
        belief_journey = game_state.belief_history
        
        significant_changes = []
        for i in range(len(belief_journey) - 1):
            prev = belief_journey[i]
            curr = belief_journey[i + 1]
            
            # Check if a belief was resolved
            if curr.get("intensity") == BELIEF_INTENSITY_RESOLVED:
                significant_changes.append(curr)
    
    if significant_changes:
        "You've come a long way:"
        
        python:
            for change in significant_changes:
                belief_id = change["belief"]
                if belief_id in beliefs:
                    belief_statement = beliefs[belief_id]["statement"]
                    renpy.say(None, f"You used to believe: {belief_statement}")
                    
                    # Show what it was resolved to
                    resolved_to = beliefs[belief_id].get("resolution")
                    if resolved_to and resolved_to in beliefs:
                        new_statement = beliefs[resolved_to]["statement"]
                        renpy.say(None, f"Now you believe: {new_statement}")
    
    "This is who you're becoming."
    
    return
