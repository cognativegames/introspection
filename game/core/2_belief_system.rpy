# ============================================================================
# BELIEF SYSTEM
# Core belief mechanics including conflicts, resolution, and synthesis
# ============================================================================

init python:
    # Additional GameState methods for beliefs (extending the class)
    def get_most_severe_conflict_method(self):
        """
        Get the single most severe active belief conflict
        Used to focus introspection
        """
        conflicts = self.detect_belief_conflicts()
        
        if not conflicts:
            return None
        
        # Sort by severity (highest first)
        conflicts.sort(key=lambda x: x[2], reverse=True)
        
        belief_1_id, belief_2_id, severity = conflicts[0]
        
        if belief_1_id in beliefs and belief_2_id in beliefs:
            return {
                "belief_1_id": belief_1_id,
                "belief_2_id": belief_2_id,
                "belief_1": beliefs[belief_1_id],
                "belief_2": beliefs[belief_2_id],
                "severity": severity
            }
        
        return None
    
    # Add method to GameState class
    GameState.get_most_severe_conflict = get_most_severe_conflict_method

# ============================================================================
# BELIEF ALIGNMENT CHECK
# Call before major choices to check alignment with core beliefs
# ============================================================================

label check_belief_alignment(action_belief, action_description):
    # Check if action aligns with core beliefs and trigger reality shifts
    
    python:
        alignment_score = 0
        is_aligned = False
        
        # Calculate alignment between action and core beliefs using game_state.beliefs
        if action_belief in game_state.beliefs:
            belief_strength = game_state.beliefs[action_belief]
            
            if belief_strength >= BELIEF_INTENSITY_CORE:  # 3+ = strong belief
                is_aligned = True
                alignment_score = 10
            elif belief_strength >= BELIEF_INTENSITY_ACTIVE:  # 2+ = moderate belief
                is_aligned = True
                alignment_score = 5
            else:  # Weak belief (SURFACE or below)
                is_aligned = False
                alignment_score = -5
        else:
            # Acting on belief not yet in system - treat as neutral
            alignment_score = 0
    
    if is_aligned:
        # Acting in alignment - positive feeling
        "As you [action_description], something clicks into place. This feels right. Natural."
        $ reality_stability = min(10, reality_stability + 1)
        
        if reality_stability >= 9:
            call trigger_reality_shift("harmony", action_description)
        
    else:
        # Acting against beliefs - negative feeling  
        "As you [action_description], something inside you recoils. This isn't who you are. Is it?"
        
        python:
            # Determine severity based on how opposed the action is
            if alignment_score <= -5:
                shift_severity_level = "severe"
            else:
                shift_severity_level = "moderate"
        
        call trigger_reality_shift(shift_severity_level, action_description)
    
    return

# ============================================================================
# BELIEF ACTION TRIGGER CONVENIENCE FUNCTION
# Call this from dialogue/actions to trigger belief activation
# ============================================================================

init python:
    def trigger_belief_from_action(belief_id, intensity=BELIEF_INTENSITY_SURFACE):
        """
        Convenience function to trigger belief activation from dialogue/actions.
        
        Args:
            belief_id: The belief ID to activate (e.g., "self.is-worthy")
            intensity: Belief intensity (default SURFACE=1)
                       Use BELIEF_INTENSITY_ACTIVE (2) for significant actions
                       Use BELIEF_INTENSITY_CORE (3) for major story moments
        
        Returns:
            bool: True if belief was activated, False if belief doesn't exist
        
        Example usage in dialogue:
            $ trigger_belief_from_action("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
        """
        if belief_id not in beliefs:
            return False
        
        return game_state.activate_from_action(belief_id, intensity)

# ============================================================================
# BELIEF CONFLICT VISUALIZATION
# ============================================================================

label show_belief_conflict:
    # Visualize the internal conflict to the player
    
    python:
        conflict_data = game_state.apply_conflict_consequences()
    
    if conflict_data and conflict_data.get("total_distress", 0) > 10:
        
        scene introspection_conflict with dissolve
        
        "Something feels... wrong. Contradictory."
        
        python:
            severe = game_state.get_most_severe_conflict()
        
        if severe:
            "Part of you believes:"
            "'{i}[severe['belief_1']['statement']]{/i}'"
            
            "But another part believes:"
            "'{i}[severe['belief_2']['statement']]{/i}'"
            
            "They can't both be true. The dissonance is... painful."

            python:
                severity = severe["severity"]
            
                if severity == BELIEF_INTENSITY_CORE:
                    pain_level = "Your head throbs. This conflict runs deep."
                elif severity == BELIEF_INTENSITY_ACTIVE:
                    pain_level = "The contradiction creates tension. Discomfort."
                else:
                    pain_level = "A subtle unease. Something doesn't fit."
        
            "[pain_level]"
        
            menu:
                "What do you do with this conflict?"
                
                "Ignore it. Push it down.":
                    $ game_state.adjust_emotions({"overwhelm":10, "anxiety":5})
                    "You force yourself not to think about it. The tension remains, buried."
                    
                "Notice it. Just observe.":
                    $ game_state.adjust_emotions({"clarity":10, "overwhelm":-5})
                    $ game_state.introspection_depth += 1
                    "You don't try to solve it. Just... see that it's there."
                    "Sometimes awareness is the first step."
                    
                "I need to examine this more closely.":
                    $ game_state.adjust_emotions({"clarity":15})
                    $ game_state.introspection_depth += 1
                    "This conflict is important. It's telling you something."
                    call introspect_conflict
        
        scene introspection_space with dissolve
    
    return

# ============================================================================
# DEEP CONFLICT INTROSPECTION
# ============================================================================

label introspect_conflict:
    # Deep examination of a specific belief conflict
    
    $ game_state.phase = GAME_PHASE_INTROSPECT
    scene introspection_deep with fade
    
    python:
        conflict = game_state.get_most_severe_conflict()
    
    if not conflict:
        "The conflict has resolved itself."
        return
    
    "You sit with the contradiction:"
    "Belief A: '{i}[conflict['belief_1']['statement']]{/i}'"
    "Belief B: '{i}[conflict['belief_2']['statement']]{/i}'"
    "They're fighting for dominance in your mind."
    
    menu:
        "Which one feels more true?"
        
        "Belief A feels true. Belief B is the lie.":
            python:
                keep_belief = conflict["belief_1_id"]
                examine_belief = conflict["belief_2_id"]
            "You feel Belief A settle in. Familiar. Solid."
            "Belief B starts to feel... questionable."
            call examine_conflicting_belief(examine_belief, keep_belief)
            
        "Belief B feels true. Belief A is the lie.":
            python:
                keep_belief = conflict["belief_2_id"]
                examine_belief = conflict["belief_1_id"]
            "Belief B resonates. Belief A feels... imposed from outside."
            call examine_conflicting_belief(examine_belief, keep_belief)
            
        "Neither feels completely true.":
            $ game_state.introspection_depth += 2
            $ game_state.adjust_emotions({"clarity":20})
            "A breakthrough. Neither belief is absolute truth."
            "They're both just... thoughts. Patterns. Stories you've been telling yourself."
            
            python:
                # Mark both as examined - player is transcending the binary
                game_state.beliefs[conflict["belief_1_id"]] = BELIEF_INTENSITY_EXAMINED
                game_state.beliefs[conflict["belief_2_id"]] = BELIEF_INTENSITY_EXAMINED
            
            "What if there's a third way? Something beyond this conflict?"
            call offer_belief_synthesis(conflict["belief_1_id"], conflict["belief_2_id"])
        
        "I can't tell yet. This is too confusing.":
            $ game_state.adjust_emotions({"overwhelm":5})
            "That's okay. Some conflicts take time to unravel."
            
            python:
                game_state.beliefs[conflict["belief_1_id"]] = BELIEF_INTENSITY_EXAMINED
                game_state.beliefs[conflict["belief_2_id"]] = BELIEF_INTENSITY_EXAMINED
    
    scene introspection_space with fade
    return

# ============================================================================
# EXAMINE SPECIFIC BELIEF
# ============================================================================

label examine_conflicting_belief(examine_id, keep_id):
    # Player has chosen which belief to keep, now examine the other one
    
    python:
        examine_belief = beliefs.get(examine_id)
        keep_belief = beliefs.get(keep_id)
    
    if not examine_belief:
        return
    
    "So you believe: '{i}[keep_belief['statement']]{/i}'"
    "Which means: '{i}[examine_belief['statement']]{/i}' must be false."
    "Where did this false belief come from?"
    
    menu:
        "Someone told me this. An old voice.":
            "An internalized message. Not your truth. Someone else's."
            
        "An experience taught me this.":
            "One experience became a universal rule. But was it the only truth?"
            
        "I don't know. It's just always been there.":
            "The beliefs we don't question are often the most powerful."
    
    "What if you let it go?"
    
    menu:
        "Yes. I'm ready to release this belief.":
            $ game_state.beliefs[examine_id] = BELIEF_INTENSITY_RESOLVED
            $ game_state.adjust_emotions({"clarity":20, "anxiety":-15, "overwhelm":-10})
            "The belief dissolves. The conflict eases."
            "'{i}[keep_belief['statement']]{/i}' stands alone now. Uncontested."
            
            python:
                current = game_state.beliefs.get(keep_id, 0)
                if current < BELIEF_INTENSITY_CORE:
                    game_state.beliefs[keep_id] = current + 1
            
        "Not yet. I need more time.":
            "The conflict remains. But you're more aware of it now."
            
            python:
                current = game_state.beliefs.get(examine_id, 0)
                if current > BELIEF_INTENSITY_SURFACE:
                    game_state.beliefs[examine_id] = current - 1
    
    return

# ============================================================================
# BELIEF SYNTHESIS
# ============================================================================

label offer_belief_synthesis(belief_1_id, belief_2_id):
    # Offer a third belief that transcends the conflict (if available)
    
    python:
        belief_1 = beliefs.get(belief_1_id)
        belief_2 = beliefs.get(belief_2_id)
        synthesis_id = None
        
        if belief_1 and "synthesis" in belief_1:
            synthesis_id = belief_1["synthesis"]
        elif belief_2 and "synthesis" in belief_2:
            synthesis_id = belief_2["synthesis"]
        
        if synthesis_id and synthesis_id in beliefs:
            synthesis_belief = beliefs[synthesis_id]
        else:
            synthesis_belief = None
    
    if synthesis_belief:
        "What if instead of choosing between them..."
        "You could believe something that includes both truths?"
        "'{i}[synthesis_belief['statement']]{/i}'"
        
        menu:
            "Does this feel true?"
            
            "Yes. This transcends the conflict.":
                scene introspection_resolution with flash
                
                python:
                    game_state.beliefs[belief_1_id] = BELIEF_INTENSITY_RESOLVED
                    game_state.beliefs[belief_2_id] = BELIEF_INTENSITY_RESOLVED
                    game_state.activate_belief(synthesis_id, BELIEF_INTENSITY_ACTIVE)
                    game_state.adjust_emotions({"clarity":30, "hope":25, "anxiety":-20, "overwhelm":-15})
                    game_state.introspection_depth += 3
                
                "Both beliefs dissolve. The synthesis remains."
                "Not a compromise. A transcendence."
                "This is integration."
                
            "I'm not ready for this yet.":
                "The synthesis is there when you need it."
                "Seeds planted."
    else:
        "The conflict remains. But you see it clearly now."
        "Sometimes that's enough to start the shift."
    
    return

# ============================================================================
# CONFLICT CHECK HOOK
# ============================================================================

label check_for_conflicts:
    # Call this after player makes an interpretation choice
    
    python:
        conflicts = game_state.detect_belief_conflicts()
        should_show = False
        
        for b1, b2, severity in conflicts:
            if severity >= BELIEF_INTENSITY_ACTIVE:
                should_show = True
                break
    
    if should_show:
        call show_belief_conflict
    
    return
