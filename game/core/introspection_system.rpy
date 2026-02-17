# ============================================================================
# INTROSPECTION TRIGGER SYSTEM
# Offers introspection after 2+ negative interpretations
# ============================================================================

label offer_introspection(game_state):
    # INTRO-01: Trigger after 2+ negative interpretations
    if not game_state.should_trigger_introspection():
        return
    
    # Show introspection offer
    scene dr_chen_office
    show dr_chen
    
    dr_chen "I notice you've been interpreting things quite negatively lately."
    dr_chen "Would you like to explore what's happening internally?"
    
    # Display current emotional state
    call show_emotion_dashboard(game_state)
    
    menu:
        "Yes, I want to understand":
            jump introspection_explore
        
        "I'm not ready to examine this":
            # Living in denial - enhanced negative emotions (INTRO-01)
            $ game_state.adjust_emotions({
                "loneliness": 2,
                "emptiness": 1,
                "detachment": 2
            })
            dr_chen "That's your choice. But these feelings won't resolve themselves."
            return

label show_emotion_dashboard(game_state):
    # Show both beliefs AND emotions (INTRO-01)
    "Current emotional state:"
    python:
        negative_emotions = {k: v for k, v in game_state.emotions.items() if v > 5}
    if negative_emotions:
        for emotion, value in sorted(negative_emotions.items(), key=lambda x: -x[1]):
            "- [emotion]: [value]/10"
    else:
        "- No dominant negative emotions"
    
    "Active beliefs:"
    python:
        active_beliefs = {k: v for k, v in game_state.beliefs.items() if v > 0}
    if active_beliefs:
        for belief_id, intensity in sorted(active_beliefs.items(), key=lambda x: -x[1]):
            if belief_id in beliefs:
                "- [beliefs[belief_id]['statement']]: intensity [intensity]"
    else:
        "- No active beliefs yet"
    
    return

# ============================================================================
# CONFLICT VISUALIZATION (INTRO-02)
# Detect contradictory beliefs and calculate severity
# ============================================================================

init python:
    def get_belief_conflicts(game_state):
        """Detect contradictory beliefs and calculate severity"""
        conflicts = []
        
        # Define contradictory pairs
        contradiction_pairs = [
            ("self.is-unworthy", "self.is-worthy"),
            ("self.is-failure", "self.is-capable"),
            ("world.is-dangerous", "world.is-safe"),
            ("others.are-cruel", "others.are-friendly"),
            ("existence.is-meaningless", "existence.is-meaningful")
        ]
        
        for neg, pos in contradiction_pairs:
            neg_intensity = game_state.beliefs.get(neg, 0)
            pos_intensity = game_state.beliefs.get(pos, 0)
            
            if neg_intensity > 0 and pos_intensity > 0:
                severity = (neg_intensity + pos_intensity) / 2
                conflicts.append({
                    "negative": neg,
                    "positive": pos,
                    "severity": severity,
                    "emotional_impact": severity * 2  # Maps to anxiety/overwhelm
                })
        
        return sorted(conflicts, key=lambda x: -x["severity"])

label show_conflict(game_state):
    # INTRO-02: Show both beliefs with severity
    python:
        conflicts = get_belief_conflicts(game_state)
    
    if not conflicts:
        dr_chen "I don't see any conflicting beliefs. That's good progress."
        return
    
    "Belief conflicts detected:"
    
    python:
        for i, conflict in enumerate(conflicts):
            neg_label = beliefs[conflict["negative"]]["statement"] if conflict["negative"] in beliefs else conflict["negative"]
            pos_label = beliefs[conflict["positive"]]["statement"] if conflict["positive"] in beliefs else conflict["positive"]
            severity_bar = "!" * int(conflict["severity"])
            emotional_impact = conflict["emotional_impact"]
    
    "[i+1]. [neg_label] vs [pos_label] [severity_bar]"
    "- Emotional impact: [emotional_impact]/10"
    
    python:
        return conflicts

label visualize_conflicts(game_state):
    # INTRO-02: Visualize conflicts with severity and emotional impact
    call show_conflict(game_state)
    return

# ============================================================================
# BELIEF EXAMINATION FLOW (INTRO-03)
# Allow player to choose which belief to keep
# ============================================================================

label introspection_explore:
    # INTRO-03: Let player choose which belief to examine
    call visualize_conflicts(game_state)
    
    dr_chen "Which belief would you like to examine?"
    
    menu:
        "Examine my negative belief":
            jump examine_negative_belief
        
        "Examine my positive belief":
            jump examine_positive_belief
        
        "Neither - show me a synthesis":
            jump offer_synthesis

label examine_negative_belief:
    # Show negative belief and its emotional consequences
    python:
        active_negatives = [b for b, i in game_state.beliefs.items() if i > 0 and b in beliefs and beliefs[b].get('type') == 'negative']
    
    if not active_negatives:
        dr_chen "You don't have any active negative beliefs to examine."
        return
    
    dr_chen "Which negative belief would you like to examine?"
    
    menu:
        for belief_id in active_negatives:
            "[beliefs[belief_id]['statement']]":
                $ selected_belief = belief_id
    
    # Show what emotions this belief creates
    python:
        if selected_belief in beliefs:
            related_emotions = beliefs[selected_belief].get("related_emotions", {})
            belief_statement = beliefs[selected_belief]["statement"]
    
    "Holding '[belief_statement]' creates:"
    python:
        if related_emotions:
            for emotion, weight in related_emotions.items():
                emotion_val = game_state.emotions.get(emotion, 0)
                impact = weight * game_state.beliefs.get(selected_belief, 1)
                "- [emotion]: +[impact] (current: [emotion_val]/10)"
        else:
            "- This belief has no direct emotional link"
    
    menu:
        "Release this belief":
            # INTRO-03: Examine and resolve
            $ game_state.resolve_belief(selected_belief, "self.is-worthy")
            jump belief_resolved
        
        "Keep this belief":
            dr_chen "That's okay. The belief is still serving you in some way."
            return

label examine_positive_belief:
    # Similar flow for positive beliefs
    python:
        active_positives = [b for b, i in game_state.beliefs.items() if i > 0 and b in beliefs and beliefs[b].get('type') == 'positive']
    
    if not active_positives:
        dr_chen "You don't have active positive beliefs yet. Let's work on that."
        return
    
    dr_chen "Which positive belief would you like to examine?"
    
    menu:
        for belief_id in active_positives:
            "[beliefs[belief_id]['statement']]":
                $ selected_belief = belief_id
    
    python:
        if selected_belief in beliefs:
            related_emotions = beliefs[selected_belief].get("related_emotions", {})
            belief_statement = beliefs[selected_belief]["statement"]
    
    "Believing '[belief_statement]' creates:"
    python:
        if related_emotions:
            for emotion, weight in related_emotions.items():
                emotion_val = game_state.emotions.get(emotion, 0)
                "- [emotion]: +[weight] (current: [emotion_val]/10)"
        else:
            "- This belief creates general positive emotional state"
    
    dr_chen "This belief is serving you well."
    return

label belief_resolved:
    dr_chen "You've released that belief. The emotional charge is reducing."
    "Feelings shift as old patterns dissolve."
    return

# ============================================================================
# BELIEF SYNTHESIS (INTRO-04)
# Option when neither belief feels true
# ============================================================================

label offer_synthesis:
    dr_chen "Sometimes neither belief feels completely true. There's another option."
    dr_chen "Let's find a way to hold both truths."
    
    # INTRO-04: Synthesis options
    menu:
        "I'm learning and growing":
            # Both negative and positive can coexist as "becoming"
            $ game_state.beliefs["self.is-unworthy"] = BELIEF_INTENSITY_EXAMINED  # Lower to examined
            $ game_state.beliefs["self.is-worthy"] = BELIEF_INTENSITY_ACTIVE
            $ game_state.adjust_emotions({"hope": 2, "clarity": 1})
            jump synthesis_complete
        
        "I can be both flawed and worthy":
            # Integrate both - imperfection doesn't negate worth
            $ game_state.beliefs["self.is-unworthy"] = BELIEF_INTENSITY_EXAMINED
            $ game_state.beliefs["self.is-worthy"] = BELIEF_INTENSITY_CORE
            $ game_state.adjust_emotions({"self_compassion": 2, "belonging": 1})
            jump synthesis_complete
        
        "My past doesn't define my future":
            # Temporal shift - past negative doesn't predict future
            $ game_state.beliefs["self.is-failure"] = BELIEF_INTENSITY_EXAMINED
            $ game_state.beliefs["self.is-capable"] = BELIEF_INTENSITY_ACTIVE
            $ game_state.adjust_emotions({"hope": 2, "connection": 1})
            jump synthesis_complete

label synthesis_complete:
    # INTRO-04: Belief synthesis applies positive emotions
    dr_chen "That's a healthy integration. You're not denying your experiences - you're transcending them."
    "Feelings shift as new understanding emerges."
    return

# ============================================================================
# PAUSE MECHANIC (original)
# ============================================================================

label introspect(reason=""):